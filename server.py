from mcp.server import MCPServer
import requests

# Create the Technical SEO MCP server
mcp = MCPServer("Technical SEO MCP Server")


@mcp.tool()
def check_status_code(url: str) -> dict:
    """Check the HTTP status code and final destination of a URL."""
    try:
        response = requests.get(
            url,
            timeout=15,
            allow_redirects=True
        )

        return {
            "url": url,
            "final_url": response.url,
            "status_code": response.status_code,
            "redirected": url != response.url
        }

    except requests.RequestException as error:
        return {
            "url": url,
            "error": str(error)
        }


if __name__ == "__main__":
    mcp.run()
