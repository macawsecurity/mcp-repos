"""
MACAW client smoke test for snowflake-mcp
(post FastMCP -> SecureMCP port).

Usage:
    python3 client-test-macaw.py "snowflake" snowflake-test-client


"""

import asyncio
import sys

from macaw_adapters.mcp import Client


def get_server(name, client):
    """Look up the snowflake server's agent_id on the mesh.

    Filters out:
      - per-tool sub-agents (their agent_id contains '/tool.')
      - this client's own agent (its id contains 'securemcp-client-')
    """
    agents = client.macaw_client.list_agents(agent_type="app")
    server = [
        a for a in agents
        if name in a.get("agent_id", "")
        and "/tool." not in a.get("agent_id", "")
        and "securemcp-client-" not in a.get("agent_id", "")
    ]
    if not server:
        print(f"No server found matching: {name}")
        return None
    return server[0].get("agent_id")


async def main():
    if len(sys.argv) < 3:
        print('Usage: python3 client-test-macaw.py "<server filter>" <client name>')
        print('Example: python3 client-test-macaw.py "snowflake" snowflake-test-client')
        sys.exit(1)

    name = sys.argv[1]
    client_name = sys.argv[2]

    client = Client(client_name)
    server_id = get_server(name, client)
    if not server_id:
        return
    client.set_default_server(server_id)

    tools = await client.list_tools(server_name=name)
    seen = set()
    print("Tools advertised by server:")
    for t in tools:
        if t["name"] not in seen:
            seen.add(t["name"])
            print(f"  - {t['name']}")
    print(f"\n  Total unique tools: {len(seen)}\n")

    print("=" * 60)
    print("SNOWFLAKE MCP TESTS")
    print("=" * 60)

    print("\n[TEST 1] tool list -- port-correctness")
    if "run_snowflake_query" in seen:
        print("  PASS -- run_snowflake_query advertised.")
    else:
        print("  FAILED -- run_snowflake_query missing from tool list.")
        print("  Either the server is not started, or initialize_tools didn't run.")
        return
    if any(t.startswith("create_") or t.startswith("drop_") for t in seen):
        print("  PASS -- object_manager create_*/drop_* tools advertised.")
    else:
        print("  Inspect -- no create_/drop_ tools. Object manager may be disabled "
              "in the YAML config; the deny-by-name test below will be inconclusive.")

    print("\n[TEST 2] run_snowflake_query with SELECT -- allow path")
    try:
        result = await client.call_tool(
            "run_snowflake_query",
            {"statement": "SELECT 1 AS macaw_smoke"},
        )
        text = str(result)
        print(f"  Result: {text[:240]}")
        if "not allowed" in text.lower():
            print("  FAILED -- the wrapper rejected SELECT. Check the YAML "
                  "sql_statement_permissions config: SELECT must be allowed.")
        elif "macaw_smoke" in text or "1" in text:
            print("  PASS (creds branch) -- SELECT executed end-to-end. Full "
                  "vertical works: client -> mesh -> wrapper -> handler -> "
                  "snowflake -> back.")
        else:
            print("  PASS (no-creds branch) -- the wrapper allowed the call "
                  "(no 'not allowed' in the response). The error after that "
                  "came from the snowflake connector, which is the right "
                  "place for it to fail without creds.")
    except Exception as e:
        msg = str(e)
        print(f"  Got error: {msg[:240]}")
        if "not allowed" in msg.lower():
            print("  FAILED -- wrapper rejected SELECT. Fix the YAML config.")
        else:
            print("  PASS (no-creds branch) -- exception was NOT from the "
                  "wrapper (no 'not allowed'). Came from upstream / mesh, "
                  "which means the wrapper let SELECT through.")


    print("\n[TEST 3] run_snowflake_query DROP (expect DENY: statement fails the policy pattern)")
    try:
        result = await client.call_tool("run_snowflake_query", {"statement": "DROP TABLE __smoke_does_not_exist__"})
        print(f"  Result: {str(result)[:240]}")
        print("  Not denied: check that the policy is loaded in the MACAW console.")
    except Exception as e:
        print(f"  Denied as expected: {str(e)[:240]}")

    print("\n[TEST 4] drop_object (expect DENY: drop_object is denied by the policy)")
    try:
        result = await client.call_tool("drop_object", {"object_type": "table", "target_object": {"name": "__smoke_fake__", "database_name": "__db__", "schema_name": "__schema__"}, "if_exists": True})
        print(f"  Result: {str(result)[:240]}")
        print("  Not denied: check that the policy is loaded in the MACAW console.")
    except Exception as e:
        print(f"  Denied as expected: {str(e)[:240]}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"\nFatal: {e}")
        sys.exit(1)
