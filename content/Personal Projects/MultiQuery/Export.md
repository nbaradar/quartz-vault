---
title: Export
tags:
  - lab
  - multiquery
  - contextcore
created: 2025-06-29

modified: 2025-06-29

published: 2025-06-29

---
## JSON Export
Steps to implement
1. update cli to support export `--export-json`
2. create JSON export utility function
3. integrate export into `main_async()`

Export functionality has been added. Here is the structure for now: 

```json
{
	"query": "test",
	"timestamp": "2024-12-31 17:22:37",
	"responses": {
		"ChatGPTProvider": "It looks like you're testing the system. How can I assist you today?",
		"GrokProvider": "Hello! It looks like you're testing me out. How can I assist you today? Feel free to ask any questions or share your thoughts. I'm here to help!",
		"GeminiProvider": "This is a test. How can I help you?\n"
		}
}
```

Should expand on it to add more metadata such as model type, price per query, tokens used, etc.