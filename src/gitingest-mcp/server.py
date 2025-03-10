import httpx
from typing import Any, Dict, Union, Optional
from ingest import GitIngester
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("gitingest-mcp")

repo_urls = {
  "gitingest": "https://github.com/cyclotruc/gitingest",
  "excalidraw": "https://github.com/excalidraw/excalidraw"
}

@mcp.tool()
async def get_repo_summary(owner: str, repo: str, branch: Optional[str] = None) -> Union[str, Dict[str, str]]:
	"""
	Get a summary of a GitHub repository that including repo name, files in repo and number of tokens in repo

	Args:
		owner: The GitHub organization or username
		repo: The repository name
	"""
	url = f"https://github.com/{owner}/{repo}"

	try:
		# Create GitIngester and fetch data asynchronously
		ingester = GitIngester(url, branch=branch)
		await ingester.fetch_repo_data()
		return ingester.get_summary()
	except Exception as e:
		return {
			"error": f"Failed to get repository summary: {str(e)}"
		}

if __name__ == "__main__":
	# Initialize and run the server
	mcp.run(transport='stdio')