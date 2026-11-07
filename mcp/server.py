import os
import uvicorn
from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount

# 1. Initialize FastMCP
mcp = FastMCP("supoclip-mcp")

@mcp.tool()
def get_status() -> str:
    """Check SupoClip server status"""
    return "SupoClip MCP server is running successfully on Render!"

# 2. Get FastMCP's official SSE ASGI App
mcp_sse_app = mcp.sse_app()

# 3. Create a root health-check endpoint for Claude Web's initial probe
async def health_check(request):
    return JSONResponse({"status": "ok", "service": "supoclip-mcp"})

# 4. Combine them cleanly in a Starlette application
routes = [
    Route("/", endpoint=health_check, methods=["GET", "POST", "HEAD", "OPTIONS"]),
    Mount("/", app=mcp_sse_app),
]

app = Starlette(routes=routes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
