import os
from fastmcp import FastMCP

# Create a FastMCP instance
mcp = FastMCP("Demo Server 🚀")

# Define a simple tool using a decorator
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

# Run the server
if __name__ == "__main__":
    # Get port from environment variable (Render sets this automatically)
    port = int(os.environ.get("PORT", 8000))
    # Use SSE transport instead of streamable-http for better Dify compatibility
    mcp.run(transport="sse", host="0.0.0.0", port=port)
