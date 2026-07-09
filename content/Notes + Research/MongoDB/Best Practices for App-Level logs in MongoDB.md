---
title: Best Practices for App-Level logs in MongoDB
tags:
  - mongodb
  - reference
draft:
created: 2025-07-05

modified: 2025-07-05

published: 2025-07-05

---
### **Keep logs structured** — every log is a _typed event_
- Use an `event_type` field with enums like:
    - `import_created`
    - `import_processed`
    - `memory_ingested`
    - `auto_tagged`
    - `error`
### **Keep logs tied to entities**
- Add references:
    - `user_id`
    - `import_id`
    - `memory_id`
    - `prompt_id`
### **Avoid logging excessively granular steps**
- No need to log “normalized field X” unless debugging
- Focus on **discrete lifecycle transitions**
### **Keep them immutable**
- Logs should be _write-once_ and never edited