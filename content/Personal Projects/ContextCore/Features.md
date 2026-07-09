---
title: ContextCore Features
tags:
  - contextcore
  - lab
draft: false
description:
created: 2025-06-16

modified: 2025-07-05

published: 2025-06-16

---
**What are all the features of ContextCore? What are FREE features vs PRO features?**

| Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                           | Pro/Free?    | Open Source? |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------ |
| **Import/Export**           | Allow import/export of the entire context DB (Of just shards) as JSON? BLOB is prob better. Also allow users to import contexts from LLM providers (chatgpt). Need to convert to ContextCore schema.                                                                                                                                                                                                  | Free         | Yes          |
| **Elements**                | Think of context switching. Allows you to turn on/off different contextual data depending on what you want the LLM to understand about you                                                                                                                                                                                                                                                            | Free         | Yes          |
| **Memory Capture**          | Allow users to intentionally save meaningful pieces of conversations into structured long-term memories ("Shards"). Captured memories are automatically categorized using ContextCore Elements/Sub-Elements and stored in the ContextStore DB. Later, these memories can be woven into LLM prompts for smarter, personalized context via ContextWeave. Powered internally by the EchoForge submodule. | Pro          | No           |
| **Integrations**            | Allow you to seamlessly integrate different sources of data to ContextCore for automatic ingestion/categorization                                                                                                                                                                                                                                                                                     | Pro          | No           |
| **Humors**                  | Think of these as emotional states / moods                                                                                                                                                                                                                                                                                                                                                            | Pro (Akasha) | No           |
| **Mimics**                  | Think of these as Versions of people in terms of their history, thinking pattern, and style of speaking                                                                                                                                                                                                                                                                                               | Pro (Akasha) | No           |
| **Prisms (or Focus)**       | Think of these as configuration profiles that contain different combinations of Context Switching, Humors, and Mimc settings. Kinda like “work focus” on iPhone or something.                                                                                                                                                                                                                         | Pro (Akasha) | No           |
| **Prompt Management**       | Allow users to save, organize, and manage their query responses? Maybe allow for tagging of responses for quick look up?                                                                                                                                                                                                                                                                              | Pro          | No           |
| **Scheduling/Automations?** | Automatically send queries to certain prisms based on your automation schedules?                                                                                                                                                                                                                                                                                                                      | Pro          | No           |

- Import/Export: Allow import/export of the entire context DB. Also allow users to import contexts from LLM providers (chatgpt). Need to convert to ContextCore schema.
- Integrations: Allow you to seamlessly integrate different sources of data to ContextCore for automatic ingestion/categorization
- Elements/Shards: Think of context switching. Allows you to turn on/off different contextual data depending on what you want the LLM to understand about you
- Humors: Think of these as emotional states / moods
- Mimics: Think of these as Versions of people in terms of their history, thinking pattern, and style of speaking
- Prisms (or Focus): Think of these as configuration profiles that contain different combinations of Context Switching, Humors, and Mimc settings. Kinda like “work focus” on iPhone or something.
- Prompt Management: Allow users to save, organize, and manage their query responses? Maybe allow for tagging of responses for quick look up?