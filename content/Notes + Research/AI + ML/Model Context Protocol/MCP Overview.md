---
title: MCP Overview
tags:
  - mcp
  - ai/ml
  - reference
draft:
created: 2025-06-16

modified: 2025-11-23

published: 2025-06-16

---
>[!info]- Relevant and Useful Links/Articles
>[MCP Documentation](https://modelcontextprotocol.io/introduction)
>[Official MCP Github Servers and Libraries](https://github.com/modelcontextprotocol)
>[Anthropic: Writing tools for agents with MCP](https://www.anthropic.com/engineering/writing-tools-for-agents)
>[Great Blogpost on how to build Remote MCP Server](https://simplescraper.io/blog/how-to-mcp)
>[Code execution with MCP: Building more efficient agents](https://www.anthropic.com/engineering/code-execution-with-mcp)
>[MetaMCP: MCP proxy that lets you dynamically aggregate MCP servers into a unified MCP server](https://docs.metamcp.com/en)
>[The second wave of MCP: Building for LLMs, not developers](https://vercel.com/blog/the-second-wave-of-mcp-building-for-llms-not-developers)
# Overview 
The **[[Model Context Protocol]]**, created by [[Anthropic]], is a **protocol** that enables an LLM to communicate with/leverage external data and tools. 

[From their site:](https://www.anthropic.com/news/model-context-protocol):
> It provides a universal, open standard for connecting AI systems with data sources, replacing fragmented integrations with a single protocol. It follows client/server patterns.
> The architecture is straightforward: developers can either expose their data through MCP servers or build AI applications (MCP clients) that connect to these servers.

You can also think of this analogy:
> **MCP like a USB-C port for AI applications.** 
> Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.

---
# Main Components
There are 2 main components 
- **MCP Clients:** These are like the AI app that want to access custom date. So Claude Desktop comes with it's own MCP client that can access servers. If you create your own custom chatbot for a company you'd need to also implement an MCP client for that custom chatbot
- **MCP Servers:** These are the custom resources themselves. But more than that, these servers are basically a way to interact with different data/apps. [[Build a MCP Server|Guide on building a simple MCP Server to retrieve live weather.]]

MCP Servers contain:
- **Resources:** data, filesystem, database, etc
- **Tools:** function, API, image processing, etc
- **Custom Prompts:** templates
## Architecture 
The key participants in the MCP architecture are:
- **MCP Host**: The AI application that coordinates and manages one or multiple MCP clients
- **MCP Client**: A component that maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use
- **MCP Server**: A program that provides context to MCP clients. This can execute locally (STDIO) OR remote (Streamable HTTP)

**For example**: **Visual Studio Code acts as an MCP host.** When Visual Studio Code establishes a connection to an **MCP server, such as the [Sentry MCP server](https://docs.sentry.io/product/sentry-mcp/)**, the Visual Studio Code runtime **instantiates an MCP client object that maintains the connection** to the Sentry MCP server.
## Layers
There are 2 layers in MCP
### Data Layer
Defines the JSON-RPC protocol for client-server communication. This includes... 
- **Lifecycle Management:** Connection initialization, capability negotiation, and connection termination between clients and servers
- **Server Features:** Core server functionality including tools for AI actions, resources for context data, and prompts for interaction templates
- **Client Features:** Enables servers to ask the client to sample from the host LLM, elicit input from the user, and log messages to the client.
- **Utility Features:** Additional features like notifications and progress tracking for long operations
### Transport Layer
Defines communication methods that enable data exchange between MCP clients and MCP servers. This includes transport-specific connection establishment, message framing, and authorization. See [[MCP Overview#Transport/Networking|Below]] for more detail.  
## Data Layer Protocol
### [Lifecycle Management](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
1. **Initialization**: Capability negotiation and protocol version agreement
2. **Operation**: Normal protocol communication
3. **Shutdown**: Graceful termination of the connection
## Primitives 
MCP primitives are the most important concept within MCP. They define what clients and servers can offer each other.
### [**Server Primitives**](https://modelcontextprotocol.io/docs/learn/server-concepts)
- [**Tools**](https://modelcontextprotocol.io/specification/2025-06-18/server/tools): Executable functions that AI applications can invoke to perform actions (e.g., file operations, API calls, database queries)
- **[Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources)**: Data sources that provide contextual information to AI applications (e.g., file contents, database records, API responses)
- **[Prompts](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts)**: Reusable templates that help structure interactions with language models (e.g., system prompts, few-shot examples)
#### Tools
A tool definition includes:
- `name`: Unique identifier for the tool
- `title`: Optional human-readable name of the tool for display purposes.
- `description`: Human-readable description of functionality
- `inputSchema`: JSON Schema defining expected parameters
- `outputSchema`: Optional JSON Schema defining expected output structure
- `annotations`: optional properties describing tool behavior
#### Resources 
A resource definition includes:
- `uri`: Unique identifier for the resource
- `name`: The name of the resource.
- `title`: Optional human-readable name of the resource for display purposes.
- `description`: Optional description
- `mimeType`: Optional MIME type
- `size`: Optional size in bytes
#### Prompts
A prompt definition includes:
- `name`: Unique identifier for the prompt
- `title`: Optional human-readable name of the prompt for display purposes.
- `description`: Optional human-readable description
- `arguments`: Optional list of arguments for customization
### [**Client Primitives**](https://modelcontextprotocol.io/docs/learn/client-concepts)
- **Sampling**: Allows servers to request language model completions from the client’s AI application. This is useful when servers’ authors want access to a language model, but want to stay model independent and not include a language model SDK in their MCP server. They can use the `sampling/complete` method to request a language model completion from the client’s AI application.
- **Elicitation**: Allows servers to request additional information from users. This is useful when servers’ authors want to get more information from the user, or ask for confirmation of an action. They can use the `elicitation/request` method to request additional information from the user.
- **Logging**: Enables servers to send log messages to clients for debugging and monitoring purposes.

>[!warning] For trust & safety and security, clients **MUST** consider tool annotations to be untrusted unless they come from trusted servers.
### Notifications
Data layer protocol also supports notifications which enable dynamic updates between servers and clients. For example, if a servers available tools have changed. 

---
## Example Use Case
So think of having a local workflow where you want to use MCP to accomplish email tasks through Claude Desktop.
You already have an MCP client via Claude Desktop, but you'll need to create your own MCP server. 

What will your MCP server contain?
- Custom prompt 
	- "Virtual Assistant Global Prompt": A system prompt for your email assistant. 
- Resources
	- Email outlines in the form of Markdown files
		- `3-way-into.md`
		- `call-follow-up.md`
		- `schedule-meeting.md`
	- A directory of contacts in the form of CSV files
		- `directory.csv`
- Tools
	- Access to gmail API
		- Will save a draft to gmail using a tool call `write-email-draft`

Then once you go into Claude Desktop and configure it to use your custom MCP server, it will list the tools and resources it sees. You can add those to your prompt.

---
# Reference Guide
## Transport/Networking
MCP uses JSON-RPC to encode messages. JSON-RPC messages **MUST** be UTF-8 encoded.

MCP can use two transport methods:
- [STDIO](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#stdio) (Standard IO): Communication over standard in and standard out
	- **Stdio transport**: Uses standard input/output streams for direct process communication between local processes on the same machine, providing optimal performance with no network overhead.
- [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http): Server operates as an independent process that can handle multiple client connections.
	- **Streamable HTTP transport**: Uses HTTP POST for client-to-server messages with optional Server-Sent Events for streaming capabilities. This transport enables remote server communication and supports standard HTTP authentication methods including bearer tokens, API keys, and custom headers. MCP recommends using OAuth to obtain authentication tokens.
	- SSE ([Server Sent Events](https://en.wikipedia.org/wiki/Server-sent_events)): Optionally, the server can make use of SSE for multiple server messages

---
# Tips and Tricks
## Tool Annotations
[Tool Annotations](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations) are additional properties describing a Tool to clients. This metadata is used by the MCP Client during tool selection
- destructiveHint
- idempotentHint
- openWorldHint
- readOnlyHint
- title
## Token Efficiency
*Firstly, refer to the documentation linked at the top of this page in the "Relevant Links" callout.*

You should combine related tool calls into a single tool with "modes."  In other words, combine related operations into parameters 
Instead of:
```python
append_to_file(path, content)
prepend_to_file(path, content)
overwrite_file(path, content)
insert_at_heading(path, heading, content)
```
Do this:
```python
update_file(path, content, mode="append|prepend|overwrite|insert", heading=None)
```

## Security Hardening
https://hiddenlayer.com/innovation-hub/mcp-model-context-pitfalls-in-an-agentic-world/
MCP is very vulnerable to prompt injection and improper tool calling. 

## Debugging w/ MCP Inspector
>[!info] Documentation
>[MCP Inspector Docs](https://modelcontextprotocol.io/docs/tools/inspector)
>[MCP Debugging Methods](https://modelcontextprotocol.io/legacy/tools/debugging)

![[Pasted image 20251028142433.png]]
[Open Source Library](https://github.com/modelcontextprotocol/inspector) that is a visual testing tool for MCP servers. The Inspector runs directly through `npx` without requiring installation. (NPX is designed to execute Node.js packages directly without requiring them to be permanently installed).

To inspect a locally developed python server:
```shell
npx @modelcontextprotocol/inspector \
  uv \
  --directory path/to/server \
  run \
  package-name \
  args...
```

So for example, if my `claude_desktop_config.json` looks like this:
```json
{
  "mcpServers": {
    "obsidian_vault": {
      "command": "/Users/naderbaradar/.local/bin/uv",
      "args": [
        "--directory",
        "/Users/naderbaradar/development_workspace/mcp/servers/obsidian_vault",
        "run",
        "obsidian_vault.py"
      ]
    }
  }
}     
```

Then my initialization command (without args) would look like this:
```bash
npx @modelcontextprotocol/inspector -- \
  /Users/naderbaradar/.local/bin/uv \
  --directory /Users/naderbaradar/development_workspace/mcp/servers/obsidian_vault \
  run \
  obsidian_vault.py 
```

