---
title: prompts
tags:
  - contextstore
  - lab
draft:
created: 2025-07-01

modified: 2025-07-05

published: 2025-07-01

---
Create **one unified `prompts` collection** in your `contextcore` DB, with metadata fields that let you filter/scope across use cases.

This collection **WILL NOT CONTAIN PROMPTS FROM CHATS**. There is a separation of concerns here, as the prompts are meant for different use cases. 

| **Use Case**                        | **Subsystem**           | **Example**                                                    |
| ----------------------------------- | ----------------------- | -------------------------------------------------------------- |
| System-level operational prompts    | EchoForge, ContextWeave | "Prompt for exporting OpenAI memory"                           |
| User-defined reusable prompts       | User UI                 | "My daily reflection prompt", "Midjourney v6 art style prompt" |
| Personality (Akasha) prompt modules | Akasha                  | "Prompt for simulating Carl Jung", "Therapist coaching style"  |

---
# Schema
```JSON
{
  "_id": ObjectId,
  "name": "Export OpenAI Memories",
  "content": "Give me a complete, unfiltered...",
  "description": "Prompt used by EchoForge...",
  "tags": ["echoforge", "system", "openai", "import"],
  "scope": "system",              // or "user", "akasha", "weave", etc.
  "owner_id": null,              // null for system prompts; ObjectId for user
  "persona_id": null,            // link to Akasha personality module
  "version": 1,
  "active": true,
  "created_at": ISODate,
  "updated_at": ISODate
}
```

## Ideas for Later
| Field          | Purpose                                                | Add?                               |
| -------------- | ------------------------------------------------------ | ---------------------------------- |
| `updated_by`   | Track who last modified a prompt (system or user)      | Optional                           |
| `source`       | Enum: `manual`, `system_generated`, `api_imported`     | Optional but useful for provenance |
| `language`     | Default to `"en"` — allows i18n later                  | Optional                           |
| `usage_count`  | Int counter of how often it’s been used                | Optional                           |
| `is_template`  | Bool: whether it has parameterized parts (`{{input}}`) | Optional if you're templating      |
| `format`       | `"plain"` vs `"template"` vs `"function_call"` etc.    | Optional for advanced prompt types |
| `input_schema` | JSON schema (for structured/templated prompts)         | Advanced, maybe overkill for PoC   |

---

| Scenario                             | How This Schema Helps                                                        |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| 🔁 Reusing prompts across subsystems | Just filter by `tags` or `scope` (e.g., `"scope": "system"` for EchoForge)   |
| 👤 Personal prompt management        | Filter by `owner_id = <user_id>` and `scope = "user"`                        |
| 🧠 Prompt injection via Akasha       | Use `persona_id` and `scope = "akasha"` to attach to a personality module    |
| 🔄 Prompt versioning and rollback    | Add a `version` field or create `prompt_versions` collection for audit trail |
