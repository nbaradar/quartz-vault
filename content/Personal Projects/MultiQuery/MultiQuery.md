---
tags:
  - multiquery
  - contextcore
  - lab
  - project
title: MultiQuery
created: 2025-06-18

modified: 2025-11-27

published: 2025-06-18

---

# What is it?
MultiQuery is the async multi-provider query system within [[ContextCore]]. It was written to allow connection to any LLM provider with an API. It was also designed w/ Asynchronous functionality and Dependency Injection in mind, so it is very fast and easy to test. 

I wanted to get started working on ContextCore but it's such a large project I didn't really know where to begin. So I figured I'd start with something small and essential: LLM-Agnostic functionality (also lets you compare different LLMs)

I first [created a simple POC](https://github.com/nbaradar/multiquery_poc) that used the command line as the UI. I focused on making sure the async functionality worked and dependency injection allowed for flexibility where you can easily add "Providers" through config files.
![[Pasted image 20250620153256.png]]

Once I finished the POC, the "backend" was essentially complete for this submodule. I then started [creating an actual WebApp GUI](https://github.com/nbaradar/multiquery_webapp) for this functionality. For now the project is called "MultiQuery WebApp," but I'm planning to seperate the UI portion of ContextCore into its own thing. For now the only functionality the UI has is using the MultiQuery subsystem though. 
![[Pasted image 20250620153500.png|1000]]