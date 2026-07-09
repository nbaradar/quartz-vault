---
title: logs
tags:
  - contextstore
  - lab
draft:
created: 2025-07-05

modified: 2025-07-05

published: 2025-07-05

---
This DB is for **APPLICATION LEVEL AUDIT LOGS**. It will not capture any low level errors, but will instead track **events** and provide **traceability** for things like ingestion, enrichment, and tagging. Could support user-facing history / admin dashboards as well. 

|Use Case|Example|
|---|---|
|Debugging|“Why didn’t this import result in new memories?”|
|Auditing|“Which prompt was used in this ingestion?”|
|UI Feedback|“Your import succeeded with 15 entries.”|
|Developer Insight|“Which subsystems are getting hit?”|
**NOTE:** [[Best Practices for App-Level logs in MongoDB]]

---
# Schema
```JSON
{
  "_id": ObjectId,
  "event_type": "import_processed",     // or 'error', 'memory_tagged'
  "user_id": ObjectId,                  // who initiated the action
  "import_id": ObjectId,                // optional, related import
  "memory_id": ObjectId,                // optional, related memory
  "prompt_id": ObjectId,                // optional, related prompt

  "details": {
    "message": "15 memories ingested, 2 duplicates skipped.",
    "tagging_mode": "auto",
    "trigger": "manual"
  },

  "level": "info",                      // info | warning | error
  "created_at": ISODate
}
```

## Ideas for Later
| Field         | Purpose                                                 |
| ------------- | ------------------------------------------------------- |
| `request_id`  | Attach logs to a traceable external request or workflow |
| `subsystem`   | e.g. "echoforge", "contextweave", "akasha"              |
| `error_stack` | If `level === error`, capture traceback                 |
