import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("supoclip-mcp")

if __name__ == "__main__":
    # Render assigns a dynamic PORT; retrieve it or default to 8000
    port = int(os.environ.get("PORT", 8000))
    
    # Run using SSE transport bound to all network interfaces for cloud hosting
    mcp.run(transport="sse", host="0.0.0.0", port=port)
