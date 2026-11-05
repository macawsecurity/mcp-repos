# MCP repos

Popular MCP servers, secured with MACAW. Each folder holds a `SecureMCPProxy` that fronts the upstream MCP server unchanged, and a MAPL policy for it. MACAW checks every tool call against the policy before it reaches the upstream.

## Servers

| Server | Folder |
|---|---|
| [Airtable MCP](airtable/) | `airtable/` |
| [Alibaba Cloud RDS MCP](alibaba-rds/) | `alibaba-rds/` |
| [arXiv MCP](arxiv/) | `arxiv/` |
| [Atlassian MCP](atlassian/) | `atlassian/` |
| [Azure MCP](azure/) | `azure/` |
| [Brave Search MCP](brave-search/) | `brave-search/` |
| [Chrome DevTools MCP](chrome-devtools/) | `chrome-devtools/` |
| [Cloudflare MCP](cloudflare/) | `cloudflare/` |
| [Databricks MCP](databricks/) | `databricks/` |
| [dbt MCP](dbt/) | `dbt/` |
| [Dingo MCP](dingo/) | `dingo/` |
| [Dispatch Agents (operator) MCP](dispatch/) | `dispatch/` |
| [Excel MCP](excel/) | `excel/` |
| [CrowdStrike Falcon MCP](falcon/) | `falcon/` |
| [GitHub MCP](github/) | `github/` |
| [Grafana MCP](grafana/) | `grafana/` |
| [Jupyter MCP](jupyter/) | `jupyter/` |
| [MongoDB MCP](mongodb/) | `mongodb/` |
| [MySQL MCP](mysql/) | `mysql/` |
| [Neon MCP](neon/) | `neon/` |
| [Notion MCP](notion/) | `notion/` |
| [Postman MCP](postman/) | `postman/` |
| [Qdrant MCP](qdrant/) | `qdrant/` |
| [Redis MCP](redis/) | `redis/` |
| [Salesforce Agentforce MCP](salesforce-agentforce/) | `salesforce-agentforce/` |
| [Snyk MCP](snyk/) | `snyk/` |
| [Stripe MCP](stripe/) | `stripe/` |
| [Supabase MCP](supabase/) | `supabase/` |
| [Terraform MCP](terraform/) | `terraform/` |

## SecureMCP servers

> **SecureMCP:** These servers are an experimental prototype for public review. Get in touch with the team at hello@macawsecurity.com.

Open-source MCP servers ported to `SecureMCP`: the server itself runs inside MACAW, so every tool call is checked against its MAPL policy (in the folder's `Policy/`). Each folder's README covers setup.

| Server | Folder |
|---|---|
| [BICScan MCP](securemcp/bicscan-mcp/) | `securemcp/bicscan-mcp/` |
| [Chroma MCP](securemcp/chroma-mcp/) | `securemcp/chroma-mcp/` |
| [Conan MCP](securemcp/conan-mcp/) | `securemcp/conan-mcp/` |
| [Salesforce Data Cloud MCP](securemcp/datacloud-mcp-query/) | `securemcp/datacloud-mcp-query/` |
| [ESP RainMaker MCP](securemcp/esp-rainmaker-mcp/) | `securemcp/esp-rainmaker-mcp/` |
| [Excalidraw Architect MCP](securemcp/excalidraw-architect-mcp/) | `securemcp/excalidraw-architect-mcp/` |
| [Cloudera Iceberg (Impala) MCP](securemcp/iceberg-mcp-server/) | `securemcp/iceberg-mcp-server/` |
| [Apache IoTDB MCP](securemcp/iotdb-mcp-server/) | `securemcp/iotdb-mcp-server/` |
| [Jira Reporter MCP](securemcp/jira_reporter/) | `securemcp/jira_reporter/` |
| [Kubernetes MCP](securemcp/k8s-mcp-server/) | `securemcp/k8s-mcp-server/` |
| [PostgreSQL MCP](securemcp/MCP-server-postgres/) | `securemcp/MCP-server-postgres/` |
| [Azure DevOps MCP](securemcp/mcp-azure-devops/) | `securemcp/mcp-azure-devops/` |
| [Obsidian MCP](securemcp/mcp-obsidian/) | `securemcp/mcp-obsidian/` |
| [Apache Pinot MCP](securemcp/mcp-pinot/) | `securemcp/mcp-pinot/` |
| [Couchbase MCP](securemcp/mcp-server-couchbase/) | `securemcp/mcp-server-couchbase/` |
| [MongoDB Memory MCP](securemcp/memory-mcp/) | `securemcp/memory-mcp/` |
| [Optuna MCP](securemcp/optuna-mcp/) | `securemcp/optuna-mcp/` |
| [Snowflake MCP](securemcp/snowflake-mcp/) | `securemcp/snowflake-mcp/` |
| [Splunk MCP](securemcp/splunk-mcp/) | `securemcp/splunk-mcp/` |
| [Spotify MCP](securemcp/spotify-mcp/) | `securemcp/spotify-mcp/` |
| [Telegram MCP](securemcp/telegram-mcp/) | `securemcp/telegram-mcp/` |
| [YDB MCP](securemcp/ydb-mcp/) | `securemcp/ydb-mcp/` |

## Use a proxy

Each folder's README lists what that server needs (environment variables, upstream tools) and how to register it with Claude Code. The pattern is the same for all of them:

```bash
claude mcp add <name>-macaw -- bash -lc 'source /path/to/.venv/bin/activate && \
  export MACAW_HOME=/path/to/macaw-client-<version>-Linux-x86_64-py3.12 && \
  python /path/to/<folder>/proxy_<name>.py'
```

Add the folder's policy file to your MACAW console before the first call.

## License

Apache 2.0. See [LICENSE](LICENSE). The SecureMCP servers are based on open-source projects and keep their original license where the project has one (the `LICENSE` in that folder).
