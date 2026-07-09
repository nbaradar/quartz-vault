---
title: Chat History Feature
tags:
  - multiquery
  - contextcore
  - userinterface
  - lab
created: 2025-06-29

modified: 2025-06-29

published: 2025-06-29

---
Need to restructure how the DB schema is designed

Rename the `results` collection to `messages`

Also will need to create a collection called `chats` that store associations of messages. 

The chats data schema will look something like this: 
```json
{
  "_id": { "$oid": "67890abcde1234567890abcd" },
  "chat_name": "Chat 1",
  "created_at": { "$date": "2025-01-08T03:46:35.036Z" },
  "messages": [
    { "$oid": "677df51b8b0f9b20375a247a" }, 
    { "$oid": "677df51b8b0f9b20375a247b" }
  ]
}
```
#### **Fields**
- **`_id`** → Unique chat ID.
- **`chat_name`** → A user-friendly chat name.
- **`created_at`** → Timestamp when the chat was started.
- **`messages`** → Array of **message IDs** (links to `messages` collection).

You will also need to add a new field to your `messages` schema
- **`chat_id`** → Reference to the `chats` collection.
```json
{
  "_id": { "$oid": "677df51b8b0f9b20375a247a" },
  "chat_id": { "$oid": "67890abcde1234567890abcd" },
  "query": "Who are you?",
  "responses": {
    "ChatGPTProvider": "I am an AI language model...",
    "GrokProvider": "I am Grok, a humorous AI...",
    "GeminiProvider": "I am a large language model..."
  },
  "timestamp": { "$date": "2025-01-08T03:46:35.036Z" }
}
```