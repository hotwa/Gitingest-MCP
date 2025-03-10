import httpx
from typing import Any, Dict, Union
from ingest import GitIngester
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("gitingest-mcp")

repo_urls = {
  "gitingest": "https://github.com/cyclotruc/gitingest",
  "excalidraw": "https://github.com/excalidraw/excalidraw"
}

@mcp.tool()
async def get_repo_summary(org_or_username: str, repo_name: str) -> Union[str, Dict[str, str]]:
	"""
	Get a summary of a GitHub repository that including repo name, files in repo and number of tokens in repo

	Args:
		org_or_username: The GitHub organization or username
		repo_name: The repository name
	"""
	url = f"https://github.com/{org_or_username}/{repo_name}"

	try:
		# Create GitIngester and fetch data asynchronously
		ingester = GitIngester(url)
		await ingester.fetch_repo_data()
		return ingester.get_summary()
	except Exception as e:
		return {
			"error": f"Failed to get repository summary: {str(e)}"
		}

if __name__ == "__main__":
	# Initialize and run the server
	mcp.run(transport='stdio')