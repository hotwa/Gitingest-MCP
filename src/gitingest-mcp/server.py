import httpx
from typing import Any, Dict, Union, List, Optional
from ingest import GitIngester
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("gitingest-mcp")

@mcp.tool()
async def git_repo_summary(
	owner: str, 
	repo: str, 
	branch: Optional[str] = None
) -> Union[str, Dict[str, str]]:
	"""
	Get a summary of a GitHub repository that includes repo name, files in repo and number of tokens in repo

	Args:
		owner: The GitHub organization or username
		repo: The repository name
		branch: Optional branch name (default: None)
	"""
	url = f"https://github.com/{owner}/{repo}"

	try:
		# Create GitIngester and fetch data asynchronously
		ingester = GitIngester(url, branch=branch)
		await ingester.fetch_repo_data()
		return ingester.get_summary()
	except Exception as e:
		return {
			"error": f"Failed to get repository summary: {str(e)}. Try https://gitingest.com/{url} instead"
		}

@mcp.tool()
async def git_tree(
	owner: str, 
	repo: str, 
	branch: Optional[str] = None
) -> Union[str, Dict[str, str]]:
	"""
	Get the tree structure of a GitHub repository

	Args:
		owner: The GitHub organization or username
		repo: The repository name
		branch: Optional branch name (default: None)
	"""
	url = f"https://github.com/{owner}/{repo}"

	try:
		# Create GitIngester and fetch data asynchronously
		ingester = GitIngester(url, branch=branch)
		await ingester.fetch_repo_data()
		return ingester.get_tree()
	except Exception as e:
		return {
			"error": f"Failed to get repository tree: {str(e)}. Try https://gitingest.com/{url} instead"
		}

@mcp.tool()
async def git_files(
	owner: str,
	repo: str, 
	file_paths: List[str],
	branch: Optional[str] = None
) -> Union[str, Dict[str, str]]:
	"""
	Get the content of specific files from a GitHub repository

	Args:
		owner: The GitHub organization or username
		repo: The repository name
		file_paths: List of paths to files within the repository
		branch: Optional branch name (default: None)
	"""
	url = f"https://github.com/{owner}/{repo}"

	try:
		# Create GitIngester and fetch data asynchronously
		ingester = GitIngester(url, branch=branch)
		await ingester.fetch_repo_data()
		
		# Get the requested file contents
		files_content = ingester.get_content(file_paths)
		if not files_content:
			return {
				"error": f"None of the requested files were found in the repository"
			}
		return files_content
		
	except Exception as e:
		return {
			"error": f"Failed to get file content: {str(e)}. Try https://gitingest.com/{url} instead"
		}

if __name__ == "__main__":
	# Initialize and run the server
	mcp.run(transport='stdio')