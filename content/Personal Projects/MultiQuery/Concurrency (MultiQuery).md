---
title: Concurrency (MultiQuery)
tags:
  - lab
  - multiquery
  - python
  - asyncio
  - contextcore
draft:
created: 2025-06-29

modified: 2025-06-29

published: 2025-06-29

---

We will use [asyncio](https://docs.python.org/3/library/asyncio.html) for concurrency 

First install aiohttp library
```bash
pip install aiohttp
```

1. update send_query in each provider to use asyn
	1. Should prob modify base.py as well
2. update main.py to run queries for all providers concurrently instead of looping through a DICT

### Make Providers Async 
#### ChatGPT
Check out the [async usage](# Required for HTTP requests aiohttp==3.8.1 requests==2.28.1 # OpenAI LLM API openai==0.27.4 # For loading YAML configuration PyYAML==6.0) section on their GitHub. 

>[!info] PYTHON Async usage
>Simply import `AsyncOpenAI` instead of `OpenAI` and use `await` with each API call. Functionality between the synchronous and asynchronous clients is otherwise identical.

```python
import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-4o",
    )


asyncio.run(main())
```

You need to use `asyncio.run()` to facilitate the asynchronous workflow. It's designed to start the event loop and execute your top-level asynchronous function.

~={red}**You should only have ONE**=~ `asyncio.run()` ~={red}**in your program**=~

**Await Keyword**
The `await` keyword is fundamental to async programming. It is used to **pause the execution of the current coroutine** until the awaited task or coroutine completes. This allows other tasks or coroutines to run concurrently, making your program more efficient and responsive.
#### Gemini
From [this guide](https://medium.com/google-cloud/how-to-prompt-gemini-asynchronously-using-python-on-google-cloud-986ca45d9f1b)
#### Grok is same as ChatGPT (uses openAI)

---
