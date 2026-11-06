import os
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("supoclip-mcp")

if __name__ == "__main__":
    # Get dynamic port assigned by Render (defaults to 10000)
    port = int(os.environ.get("PORT", 10000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
