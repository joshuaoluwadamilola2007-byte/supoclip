import os
import uvicorn
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("supoclip-mcp")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
