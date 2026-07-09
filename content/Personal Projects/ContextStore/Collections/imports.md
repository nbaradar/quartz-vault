---
title: imports
tags:
  - contextstore
  - lab
created: 2025-07-05

modified: 2025-07-05

published: 2025-07-05

---
The imports collection will represent raw, unprocessed user input/data/memories that will later be ingested into the ContextCore memory system

Categories of Data:
- Core Data: This like the `raw_content` of the user input or data and the `source_provider` of the data
```JSON
{
  "raw_content": { ... },   // original user input (JSON object or array)
  "source_provider": "openai",  // e.g., openai, anthropic, obsidian_plugin
}
```
- Import Classification: `import_type`, `import_trigger`, `import_session`
```JSON
{
  "import_type": "provider",      // "provider", "integration", "manual_upload", "file_upload"
  "import_trigger": "manual",     // "manual", "scheduled", "auto_response"
  "import_session": "sess_abc123" // all imports part of one UX event share this
}
```
- User + Traceability
```JSON
{
  "user_id": ObjectId,
  "source_prompt_id": ObjectId,    // (if applicable — which prompt was used to request export)
  "num_memories": 15
}
```
- Status + Workflow: Needed for ingestion and data pipelines
```JSON
{
  "status": "pending",             // "pending", "processed", "errored", "duplicate"
  "processing_notes": null,        // or a string with error/debug message
  "is_duplicate": false            // based on hash match
}
```
- Timestamps

# Schema
```JSON
{
  "_id": ObjectId,
  "user_id": ObjectId,
  "raw_content": [...],                  // the unprocessed JSON array of memories
  "source_provider": "openai",           // origin of export
  "import_type": "provider",             // provider | integration | manual_upload
  "import_trigger": "manual",            // manual | auto_response | scheduled
  "import_session": "sess_abc123",       // all imports from same UX flow share this
  "source_prompt_id": ObjectId,          // optional
  "num_memories": 15,                    // count of raw memory objects

  "status": "pending",                   // pending | processed | errored
  "processing_notes": null,             // useful for debugging errors
  "is_duplicate": false,                 // hash match of content (optional)

  "created_at": ISODate(),
  "processed_at": null
}
```

## Ideas for later:
|Field|Purpose|
|---|---|
|`client_metadata`|JSON blob (user-agent, app version, etc.) for telemetry/debugging|
|`import_hash`|Hash of full payload — helps with deduplication at batch level|
|`memory_fingerprints`|Optional array of memory hashes extracted from payload (if pre-processed)|
