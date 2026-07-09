---
title: Build a MCP Server
tags:
  - mcp
  - ai/ml
  - lab
  - anthropic
  - agents
draft:
created: 2025-10-24

modified: 2025-10-27
published: 2025-10-24

---
> [!info] Reference: [[MCP Overview]]

In preparation for building an [[Obsidian MCP Server]], I'm going to follow the [official Anthropic guide to build my first MCP server](https://modelcontextprotocol.io/docs/develop/build-server#python).

This will be a very simple server with two tools: `get_alerts` and `get_forecast`. We will connect it to the Claude for Desktop client. MCP supports 3 [[MCP Overview#Primitives|Primitives]], but we will only be implementing **Tools**

I'm choosing to build in Python, [the SDK can be found here](https://github.com/modelcontextprotocol/python-sdk).

> [!warning]- Logging Best Practice 
> **For STDIO-based servers:** Never write to standard output (stdout). This includes:
>- `print()` statements in Python
>- `console.log()` in JavaScript
>- `fmt.Println()` in Go
>- Similar stdout functions in other languages
>
> ```
> # ❌ Bad (STDIO)
> print("Processing request")
> 
> # ✅ Good (STDIO)
> import logging
> logging.info("Processing request")
> ```
>
>Writing to stdout will corrupt the JSON-RPC messages and break your server.
>### Best Practices
>1. Use a logging library that writes to stderr or files.
>2. Tool names should follow the format specified [here](https://modelcontextprotocol.io/specification/draft/server/tools#tool-names)

---
## Setup Env w/ [UV](https://github.com/astral-sh/uv)
First, let's install `uv` (a python package manager) 
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

And then set up our environment
```bash
# Create a new directory for our project
uv init weather
cd weather

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx

# Create our server file
touch weather.py
```

## FastMCP
>[!tip] For more info on [[FastMCP]]

While continuing the guide, I noticed:
```python
# Initialize FastMCP server 
mcp = FastMCP("weather")
```

The [[FastMCP]] class uses Python type hints and docstrings to automatically generate tool definitions, making it easy to create and maintain [[Model Context Protocol]] tools.

## Helper Functions
We added 2 helper functions for querying and formatting data
```python
async def make_nws_request(url: str) -> dict[str], Any] | None:
```
```python
def format_alert(feature: dict) -> str:
```

## Tools
Next we implement the logic for the tool using a **tool execution handler**. We will be implementing 2 tools
```python
@mcp.tool() 
async def get_alerts(state: str) -> str:
```
```python
@mcp.tool() 
async def get_forecast(latitude: float, longitude: float) -> str:
```

## Run server
Finally you just run the server from main method
```python
def main():
    # Initialize and run the server
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

And then start the MCP server with
```bash
uv run weather.py
```

---
## Client Access w/ [Claude Desktop](https://claude.ai/download)
First, you need to configure Claude for Desktop. To do this, open the config file at `~/Library/Application Support/Claude/claude_desktop_config.json`. Create the file if it doesn't already exist

Then add your server in the `mcpServers` key. The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.

```JSON
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
        "run",
        "weather.py"
      ]
    }
  }
}
```
This tells Claude for Desktop:
1. There’s an MCP server named “weather”
2. To launch it by running `uv --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather run weather.py`

FAILED! It did not work, here's what I saw:
![[Pasted image 20251024123441.png]]

You can navigate to your logs (Found here: `/Users/naderbaradar/Library/Logs/Claude`) to debug. Here's what I saw:
```bash
naderbaradar@Naders-MacBook-Air Claude % ls     
claude.ai-web.log mcp-server-weather.log unknown-window.log
main.log mcp.log window.log
naderbaradar@Naders-MacBook-Air Claude % cat mcp-server-weather.log 
2025-10-24T16:29:46.621Z [weather] [info] Initializing server... { metadata: undefined }
2025-10-24T16:29:46.631Z [weather] [info] Using MCP server command: uv with args and path: {
  metadata: {
    args: [
      '--directory',
      '/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather',
      'run',
      'weather.py',
      [length]: 4
    ],

    paths: [
      '/Users/naderbaradar/.nvm/versions/node/v22.13.0/bin',
      '/Users/naderbaradar/.nvm/versions/node/v22.16.0/bin',
      '/usr/local/bin',
      '/opt/homebrew/bin',
      '/usr/bin',
      '/usr/bin',
      '/bin',
      '/usr/sbin',
      '/sbin',
      [length]: 9
    ]
  }
} %o
2025-10-24T16:29:46.632Z [weather] [error] spawn uv ENOENT {
  metadata: {
    context: 'connection',
    stack: 'Error: spawn uv ENOENT\n' +
      '    at ChildProcess._handle.onexit (node:internal/child_process:285:19)\n' +
      '    at onErrorNT (node:internal/child_process:483:16)\n' +
      '    at process.processTicksAndRejections (node:internal/process/task_queues:90:21)'
  }
}
```

Looks like Claude Desktop does not have access to `uv` so it can't run the server. Let's just give it the full path to `uv` instead since maybe Claude Desktop doesn't have access to PATH executables due to being a GUI app.
![[Pasted image 20251024123840.png]]

So we'll just update the JSON entry for the mcp config like so:
```JSON
{
  "mcpServers": {
    "weather": {
      "command": "/Users/naderbaradar/.local/bin/uv",
      "args": [
        "--directory",
        "/Users/naderbaradar/development_workspace/mcp/servers/build_server_intro_guide/weather",
        "run",
        "weather.py"
      ]
    }
  }
}
```

Now let's try again...
![[Pasted image 20251024124128.png]]

It works! 
![[Pasted image 20251024124310.png]]