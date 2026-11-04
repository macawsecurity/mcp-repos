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

## Use one

Each folder's README lists what that server needs (environment variables, upstream tools) and how to register it with Claude Code. The pattern is the same for all of them:

```bash
claude mcp add <name>-macaw -- bash -lc 'source /path/to/.venv/bin/activate && \
  export MACAW_HOME=/path/to/macaw-client-<version>-Linux-x86_64-py3.12 && \
  python /path/to/<folder>/proxy_<name>.py'
```

Add the folder's policy file to your MACAW console before the first call.

## License

Apache 2.0. See [LICENSE](LICENSE).
