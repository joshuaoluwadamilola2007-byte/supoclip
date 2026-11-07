import os
from fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("supoclip-mcp")

@mcp.tool()
def get_status() -> str:
    """Check SupoClip server status"""
    return "SupoClip MCP server is running successfully on Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
