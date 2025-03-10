import re
import asyncio
from gitingest import ingest
from typing import Any, Dict, List, Optional

class GitIngester:
	def __init__(self, url: str, branch: str):
		"""Initialize the GitIngester with a repository URL."""
		self.url: str = url
		self.branch: Optional[str] = branch
		if branch:
			self.url = f"{url}/tree/{branch}"
		self.summary: Optional[Dict[str, Any]] = None
		self.tree: Optional[Any] = None
		self.content: Optional[Any] = None

	async def fetch_repo_data(self) -> None:
		"""Asynchronously fetch and process repository data."""
		# Run the synchronous ingest function in a thread pool
		loop = asyncio.get_event_loop()
		summary, self.tree, self.content = await loop.run_in_executor(
			None, lambda: ingest(self.url)
		)
		self.summary = self._parse_summary(summary)

	def _parse_summary(self, summary_str: str) -> Dict[str, Any]:
		"""Parse the summary string into a structured dictionary."""
		summary_dict = {}

		try:
			# Extract repository name
			repo_match = re.search(r"Repository: (.+)", summary_str)
			if repo_match:
				summary_dict["repository"] = repo_match.group(1).strip()
			else:
				summary_dict["repository"] = ""

			# Extract files analyzed
			files_match = re.search(r"Files analyzed: (\d+)", summary_str)
			if files_match:
				summary_dict["num_files"] = int(files_match.group(1))
			else:
				summary_dict["num_files"] = None

			# Extract estimated tokens
			tokens_match = re.search(r"Estimated tokens: (.+)", summary_str)
			if tokens_match:
				summary_dict["token_count"] = tokens_match.group(1).strip()
			else:
				summary_dict["token_count"] = ""
								
		except Exception:
			# If any regex operation fails, set default values
			summary_dict["repository"] = ""
			summary_dict["num_files"] = None
			summary_dict["token_count"] = ""

		# Store the original string as well
		summary_dict["raw"] = summary_str
		return summary_dict

	def get_summary(self) -> str:
		"""Returns the repository summary."""
		return self.summary["raw"]

	def get_tree(self) -> Any:
		"""Returns the repository tree structure."""
		return self.tree

	def get_content(self) -> Any:
		"""Returns the repository content."""
		return self.content