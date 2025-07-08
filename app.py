import os
from fastmcp import FastMCP
from fastapi.middleware.cors import CORSMiddleware

# Create a FastMCP instance
mcp = FastMCP("Demo Server 🚀")

# Add CORS middleware if needed
@mcp.server.middleware("cors")
async def add_cors_middleware(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

# Define tools using decorators
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}!"

@mcp.tool
def calculate_square(number: float) -> float:
    """Calculate the square of a number"""
    return number ** 2

# Health check endpoint
@mcp.server.get("/health")
async def health_check():
    return {"status": "healthy", "tools": ["add", "greet", "calculate_square"]}

# Run the server
if __name__ == "__main__":
    # Get port from environment variable (Render sets this automatically)
    port = int(os.environ.get("PORT", 8000))
    # Use HTTP transport for web deployment
    mcp.run(transport="http", host="0.0.0.0", port=port)
