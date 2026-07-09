---
title: FastMCP
tags:
  - reference
  - mcp
  - python
  - agents
  - ai/ml
  - anthropic
draft:
created: 2025-10-27

modified: 2025-10-27
published: 2025-10-27

---
>[!tip] Tutorial: [[Build a MCP Server]] with FastMCP

>[!note] My [[Obsidian MCP Server]] project

![[Pasted image 20251027195637.png|400]]
# Overview
[FastMCP](https://gofastmcp.com/getting-started/welcome) ([Github Repo](https://github.com/jlowin/fastmcp)) is the standard framework for building [[Model Context Protocol]] applications with Python. With FastMCP, you don't need to deal with protocol details. You can just decorate [[MCP Overview#Primitives|MCP Primitives]] with annotations for most use cases.

The central piece of a FastMCP application is the `FastMCP` server class. This class acts as the main container for your application’s tools, resources, and prompts, and manages communication with MCP clients.
```python
from fastmcp import FastMCP

# Create a basic server instance
mcp = FastMCP(name="MyAssistantServer")

# You can also add instructions for how to interact with the server
mcp_with_instructions = FastMCP(
    name="HelpfulAssistant",
    instructions="""
        This server provides data analysis tools.
        Call get_average() to analyze numerical data.
    """,
)
```

List of [all Constructor Parameters can be found here](https://gofastmcp.com/servers/server#param-name)

---
# Tips
## FastMCP Docs via MCP
The FastMCP docs are accessible via MCP! The server URL is `https://gofastmcp.com/mcp`
```python
import asyncio
from fastmcp import Client

async def main():
    async with Client("https://gofastmcp.com/mcp") as client:
        result = await client.call_tool(
            name="SearchFastMcp", 
            arguments={"query": "deploy a FastMCP server"}
        )
    print(result)

asyncio.run(main())
```

The docs are also available in [llms.txt format](https://llmstxt.org/):
- [llms.txt](https://gofastmcp.com/llms.txt) - A sitemap listing all documentation pages
- [llms-full.txt](https://gofastmcp.com/llms-full.txt) - The entire documentation in one file (may exceed context windows)

Any page can be accessed as markdown by appending `.md` to the URL. 
For example:  `https://gofastmcp.com/getting-started/welcome.md`.