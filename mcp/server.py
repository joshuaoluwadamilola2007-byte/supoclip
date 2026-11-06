from mcp.server.fastmcp import FastMCP

# Import your existing mcp setup or initialize FastMCP SSE transport
mcp = FastMCP("supoclip-mcp")

if __name__ == "__main__":
    # Runs the FastMCP server over HTTP/SSE on port 8000
    mcp.run(transport="sse")
