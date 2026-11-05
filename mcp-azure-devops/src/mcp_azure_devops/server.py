"""
Azure DevOps MCP Server

A simple MCP server that exposes Azure DevOps capabilities.
"""
import argparse

from macaw_adapters.mcp import SecureMCP

from mcp_azure_devops.features import register_all
from mcp_azure_devops.utils import register_all_prompts

mcp = SecureMCP("azure-devops")

# Register all features
register_all(mcp)
register_all_prompts(mcp)

def main():
    """Entry point for the command-line script."""
    parser = argparse.ArgumentParser(
        description="Run the Azure DevOps MCP server")
    # Add more command-line arguments as needed
    
    parser.parse_args()  # Store args if needed later
    
    # Start the server
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
