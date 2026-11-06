# MCP repos

Popular MCP servers, secured with MACAW, in two forms: proxies that front the upstream MCP server unchanged, and SecureMCP servers ported to run inside MACAW. Each folder has a MAPL policy, and MACAW checks every tool call against it.

## Proxies

> **SecureMCP:** These proxies are an experimental prototype for public review. Get in touch with the team at hello@macawsecurity.com.

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

Open-source MCP servers ported to `SecureMCP`: the server itself runs inside MACAW, so every tool call is checked against its MAPL policy (in each folder's `Policy/`). Each folder's README covers setup.

### Official

Published by the company or project behind the product.

| Server | Folder | Based on |
|---|---|---|
| [Apache IoTDB MCP](iotdb-mcp-server/) | `iotdb-mcp-server/` | [apache/iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server) |
| [Apache Pinot MCP](mcp-pinot/) | `mcp-pinot/` | [startreedata/mcp-pinot](https://github.com/startreedata/mcp-pinot) |
| [BICScan MCP](bicscan-mcp/) | `bicscan-mcp/` | [ahnlabio/bicscan-mcp](https://github.com/ahnlabio/bicscan-mcp) |
| [Chroma MCP](chroma-mcp/) | `chroma-mcp/` | [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) |
| [Cloudera Iceberg (Impala) MCP](iceberg-mcp-server/) | `iceberg-mcp-server/` | [cloudera/iceberg-mcp-server](https://github.com/cloudera/iceberg-mcp-server) |
| [Conan MCP](conan-mcp/) | `conan-mcp/` | [conan-io/conan-mcp](https://github.com/conan-io/conan-mcp) |
| [Couchbase MCP](mcp-server-couchbase/) | `mcp-server-couchbase/` | [couchbase/mcp-server-couchbase](https://github.com/couchbase/mcp-server-couchbase) |
| [ESP RainMaker MCP](esp-rainmaker-mcp/) | `esp-rainmaker-mcp/` | [espressif/esp-rainmaker-mcp](https://github.com/espressif/esp-rainmaker-mcp) |
| [MongoDB Memory MCP](memory-mcp/) | `memory-mcp/` | [mongodb-partners/memory-mcp](https://github.com/mongodb-partners/memory-mcp) |
| [Optuna MCP](optuna-mcp/) | `optuna-mcp/` | [optuna/optuna-mcp](https://github.com/optuna/optuna-mcp) |
| [Salesforce Data Cloud MCP](datacloud-mcp-query/) | `datacloud-mcp-query/` | [forcedotcom/datacloud-mcp-query](https://github.com/forcedotcom/datacloud-mcp-query) |
| [Snowflake MCP](snowflake-mcp/) | `snowflake-mcp/` | [Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp) |
| [YDB MCP](ydb-mcp/) | `ydb-mcp/` | [ydb-platform/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) |

### Community

Written by independent developers.

| Server | Folder | Based on |
|---|---|---|
| [Azure DevOps MCP](mcp-azure-devops/) | `mcp-azure-devops/` | [Vortiago/mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops) |
| [Excalidraw Architect MCP](excalidraw-architect-mcp/) | `excalidraw-architect-mcp/` | [BV-Venky/excalidraw-architect-mcp](https://github.com/BV-Venky/excalidraw-architect-mcp) |
| [Jira Reporter MCP](jira_reporter/) | `jira_reporter/` | [Jongryong/jira_reporter](https://github.com/Jongryong/jira_reporter) |
| [Kubernetes MCP](k8s-mcp-server/) | `k8s-mcp-server/` | [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) |
| [Obsidian MCP](mcp-obsidian/) | `mcp-obsidian/` | [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) |
| [PostgreSQL MCP](MCP-server-postgres/) | `MCP-server-postgres/` | [CyprianFusi/MCP-server-postgres](https://github.com/CyprianFusi/MCP-server-postgres) |
| [Splunk MCP](splunk-mcp/) | `splunk-mcp/` | [livehybrid/splunk-mcp](https://github.com/livehybrid/splunk-mcp) |
| [Spotify MCP](spotify-mcp/) | `spotify-mcp/` | [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) |
| [Telegram MCP](telegram-mcp/) | `telegram-mcp/` | [chigwell/telegram-mcp](https://github.com/chigwell/telegram-mcp) |

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
