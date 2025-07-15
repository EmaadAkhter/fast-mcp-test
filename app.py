import os
from fastmcp import FastMCP

# Create a FastMCP instance
mcp = FastMCP("Demo Server")

# Define tools
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
    port = int(os.environ.get("PORT", 8000))
    
    # Try with explicit configuration for Dify compatibility
    mcp.run(
        transport="http",
        host="0.0.0.0", 
        port=port,
        debug=True,
        # Additional parameters for better compatibility
        cors_allow_origins=["*"],
        cors_allow_methods=["GET", "POST", "OPTIONS"],
        cors_allow_headers=["*"]
    )
