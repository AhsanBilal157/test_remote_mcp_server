from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple calculator")

@mcp.tool
def add(a:int,b:int):
    """ Add two integars
    Args:
        a: first number
        b: second number
    Retursn:
        The sum of a and b"""
    return a+b

@mcp.tool
def random_number(min_val:int =1, max_val:int = 100):
    """ Generate a random number withint range
    Args:
        min_val: Minimum value (default:1)
        max_val: Maximum value (default:1000)
    
    Returns:
        A random number between min and max value"""
    
    return random.randint(min_val,max_val)

@mcp.resource("info://server")
def server_info() -> str:
    """ Get information about this server"""
    info = {
        "name":"Simple Calculator",
        "version":"1.0.0",
        "description":"A basi MCP server with math tools",
        "tools": ["add","random_number"],
        "author": "Your Name"
    }

    return json.dumps(info,indent=2)



if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0", port=8000)