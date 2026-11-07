import os
import uvicorn
from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

mcp = FastMCP("supoclip-mcp")

# FastMCP SSE app
mcp_app = mcp._mcp_server

# Simple health/auth probe handler for Claude Web
async def health_check(request):
    return JSONResponse({"status": "ok", "auth": "none"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
