import os
from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
import uvicorn

# Initialize FastMCP instance
mcp = FastMCP("supoclip-mcp")

@mcp.tool()
def get_status() -> str:
    """Check SupoClip server status"""
    return "SupoClip MCP server is running successfully on Render!"

# Health check route for Claude Web's handshake
async def health_check(request):
    return JSONResponse({"status": "ok", "auth": "none"})

# Create Starlette app combining health check and FastMCP SSE application
app = Starlette(
    routes=[
        Route("/", endpoint=health_check, methods=["GET", "POST", "HEAD", "OPTIONS"]),
        Route("/sse", endpoint=health_check, methods=["GET", "POST", "HEAD", "OPTIONS"]),
        Mount("/", app=mcp._mcp_server),
    ]
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
