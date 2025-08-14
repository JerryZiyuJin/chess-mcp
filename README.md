Install by insert the following in your local MCP host configuration file:
'''json
{  "mcpServers": {
    "Chess": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/JerryZiyuJin/chess-mcp.git",
		"chess"
      ]
    }
  }
}
'''	  	