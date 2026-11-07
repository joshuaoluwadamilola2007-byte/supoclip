import os
from supoclip_mcp.server import mcp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    # Run the official SupoClip MCP server via SSE transport
    mcp.run(transport="sse", host="0.0.0.0", port=port)
