import os
from fastmcp import FastMCP

# 1. Initialize FastMCP server
mcp = FastMCP("supoclip-mcp")

@mcp.tool()
def get_status() -> str:
    """Check SupoClip server status"""
    return "SupoClip MCP server is running successfully on Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    # Run using streamable HTTP transport on Render's assigned port
    mcp.run(transport="http", host="0.0.0.0", port=port)
