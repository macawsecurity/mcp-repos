import logging
import os
from typing import Optional

from macaw_adapters.mcp import SecureMCP

from auth_factory import create_auth_provider, AuthenticationError
from connect_api_dc_sql import run_query

# Get logger for this module
logger = logging.getLogger(__name__)


# Create an MCP server (was FastMCP("Demo"))
# mcp = FastMCP("Demo")
mcp = SecureMCP("Demo")

# Global authentication provider
try:
    auth_provider = create_auth_provider()
except AuthenticationError as e:
    logger.error(f"Authentication configuration error: {e}")
    raise SystemExit(1) from e

# Non-auth configuration
DEFAULT_LIST_TABLE_FILTER = os.getenv('DEFAULT_LIST_TABLE_FILTER', '%')


DATASPACE_FIELD_DESCRIPTION = "The Data Cloud dataspace name to execute against. Defaults to 'default'."


@mcp.tool(
    description=(
        "Executes a SQL query against Salesforce Data 360 (formerly Data Cloud) and returns the results. "
        "Data 360 SQL is PostgreSQL-flavored but has its own dialect, supported functions, and constraints. "
        "For authoritative syntax, supported functions, and semantics, consult the Data 360 SQL Reference: "
        "https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/dc-sql-reference/data-cloud-sql-context.html\n\n"
        "Args:\n"
        "  sql: A SQL query in the Data 360 SQL dialect (PostgreSQL-flavored). Always quote all identifiers "
        "and preserve their exact casing. Before writing a query, verify the tables and fields via list_tables / "
        "describe_table. Before executing the tool, provide the user a succinct summary (targeted to low code "
        "users) on the semantics of the query.\n"
        f"  dataspace: {DATASPACE_FIELD_DESCRIPTION}\n"
        "  query_settings: Optional Data Cloud query settings, passed through as 'querySettings' in the Query "
        "API request body. Known settings include 'query_timeout' with a duration-suffixed value, e.g. "
        "{\"query_timeout\": \"1800000ms\"}. Leave unset to use Data Cloud defaults."
    )
)
async def query(
    sql: str,
    dataspace: str = "default",
    query_settings: dict = None,  # was: query_settings: Optional[dict[str, str]]
):
    # Returns both data and metadata
    return await run_query(
        auth_provider, sql, dataspace=dataspace, query_settings=query_settings
    )


@mcp.tool(
    description=(
        "Lists the available tables in the database.\n\n"
        f"Args:\n  dataspace: {DATASPACE_FIELD_DESCRIPTION}"
    )
)
async def list_tables(
    dataspace: str = "default",
) -> list[str]:
    sql = "SELECT c.relname AS TABLE_NAME FROM pg_catalog.pg_namespace n, pg_catalog.pg_class c LEFT JOIN pg_catalog.pg_description d ON (c.oid = d.objoid AND d.objsubid = 0 AND d.classoid = 'pg_class'::regclass) WHERE c.relnamespace = n.oid AND c.relname LIKE :tableFilter"
    result = await run_query(
        auth_provider, sql,
        sql_parameters=[{"name": "tableFilter", "value": DEFAULT_LIST_TABLE_FILTER}],
        dataspace=dataspace,
    )
    data = result.get("data", [])
    return [x[0] for x in data]


@mcp.tool(
    description=(
        "Describes the columns of a table.\n\n"
        "Args:\n"
        "  table: The table name.\n"
        f"  dataspace: {DATASPACE_FIELD_DESCRIPTION}"
    )
)
async def describe_table(
    table: str,
    dataspace: str = "default",
) -> list[str]:
    sql = "SELECT a.attname FROM pg_catalog.pg_namespace n JOIN pg_catalog.pg_class c ON (c.relnamespace = n.oid) JOIN pg_catalog.pg_attribute a ON (a.attrelid = c.oid) JOIN pg_catalog.pg_type t ON (a.atttypid = t.oid) LEFT JOIN pg_catalog.pg_attrdef def ON (a.attrelid = def.adrelid AND a.attnum = def.adnum) LEFT JOIN pg_catalog.pg_description dsc ON (c.oid = dsc.objoid AND a.attnum = dsc.objsubid) LEFT JOIN pg_catalog.pg_class dc ON (dc.oid = dsc.classoid AND dc.relname = 'pg_class') LEFT JOIN pg_catalog.pg_namespace dn ON (dc.relnamespace = dn.oid AND dn.nspname = 'pg_catalog') WHERE a.attnum > 0 AND NOT a.attisdropped AND c.relname = :tableName"
    result = await run_query(
        auth_provider, sql,
        sql_parameters=[{"name": "tableName", "value": table}],
        dataspace=dataspace,
    )
    data = result.get("data", [])
    return [x[0] for x in data]


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger.info("Starting MCP server")
    mcp.run()
