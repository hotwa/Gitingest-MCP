# Gitingest-MCP ![smithery badge](https://smithery.ai/badge/@puravparab/gitingest-mcp)

An MCP server for [gitingest](https://github.com/cyclotruc/gitingest). This allows MCP clients like Claude Desktop, Cline, Cursor, etc to quickly extract information about Github repositories including

- Repository summaries
- Project directory structure
- File content

[View demo](https://twitter.com/notpurav/status/1898955689030193485)

## Installation

### Installing via Smithery

To install gitingest-mcp via [Smithery](https://smithery.ai/server/@puravparab/gitingest-mcp):

- Claude Desktop
	```bash
	npx -y @smithery/cli install @puravparab/gitingest-mcp --client claude
	```

### Installing Manually

1. Clone the repo
	```bash
	git clone https://https://github.com/puravparab/Gitingest-MCP
	cd Gitingest-MCP
	```

2. Install dependencies
	```bash
	uv sync
	```

3. Add to Claude Desktop

	Open config file in your IDE
	```bash
	cursor ~/Library/Application\ Support/Claude/claude_desktop_config.json
	```
	```bash
	code ~/Library/Application\ Support/Claude/claude_desktop_config.json
	```

4. Add this to the configuration

	```
	{
		"mcpServers": {
			"gitingest": {
				"command": "<path to uv>/uv",
				"args": [
					"run",
					"--with",
					"mcp[cli]",
					"--with-editable",
					"<path to gitingest-mcp project>/gitingest-mcp",
					"mcp",
					"run",
					"<path to gitingest-mcp project>/gitingest-mcp/src/gitingest-mcp/server.py"
				]
			}
		}
	}
	```

5. If you have issues, follow this [MCP server documentation](https://modelcontextprotocol.io/quickstart/server)

## Debug

Run mcp inspector
```
uv run mcp dev src/gitingest-mcp/server.py
```