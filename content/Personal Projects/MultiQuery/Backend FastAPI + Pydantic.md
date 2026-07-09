---
title: Backend Config Notes
tags:
  - multiquery
  - contextcore
  - pydantic
  - fastapi
created: 2025-06-29

modified: 2025-07-05

published: 2025-06-29

---
# Plan for FastAPI Backend
#### **1. Set Up the FastAPI Application**
- Create a FastAPI app to handle API requests.
- Organize the backend into modules for scalability.
#### **2. Define API Endpoints**
- `/query`: Accept user input, run queries with your existing LLM providers, and return the results.
- `/history`: Retrieve stored queries and results from the MongoDB `result` collection.
- `/export`: Export results in Markdown or JSON format.
#### **3. Integrate Existing POC Code**
- Refactor the querying logic (`main.py`) into a service module.
- Use your MongoDB client for saving and retrieving data.
#### **4. Add Dependency Injection**
- Use FastAPI’s dependency injection to manage MongoDB connections and configurations.
---
# Pre-Dev: Install Required Dependencies
Install FastAPI, Uvicorn (server), and Motor (MongoDB driver):

```
multiquery/
|--> multiquery/
      |--> api/
            |--> __init__.py
            |--> endpoints/
                  |--> __init__.py
                  |--> query.py
                  |--> history.py
                  |--> export.py
      |--> core/
            |--> __init__.py
            |--> config.py
            |--> services/
                  |--> __init__.py
                  |--> llm_service.py
      |--> utils/
            |--> __init__.py
            |--> json_exporter.py
            |--> mongodb_client.py
      |--> app.py
|--> output/
```
## [[Pydantic]]
### How are we using Pydantic?
   1. API Data Validation: The project uses FastAPI, which leverages Pydantic to validate
      incoming API requests. For example, in backend/multiquery/api/endpoints/query.py, the
      QueryRequest model ensures that any request to the query endpoint contains a prompt
      string. This prevents errors from malformed requests.
   
   2. Configuration Management: Pydantic models in backend/multiquery/config/config.py define
      the structure for the application's configuration, including settings for different LLM
      providers and the database. This ensures that the configuration loaded from config.yaml
      is valid and adheres to a strict, typed schema, which makes the application more robust
      and easier to maintain.

---
# Settings Configs using Pydantic

First set the configs using the .yaml file in `app.py`
```python
# Load configuration at startup 
	config = load_config("multiquery/config/config.yaml") 
	
def get_config(): 
	""" Dependency to provide the configuration object. """ 
	return config
```

Then import to relevant endpoint 
```python
from multiquery.app import get_config # Import get_config

@router.post("/")
async def query_api(
	prompt: str,
	config=Depends(get_config), # Inject config dependency
	collection=Depends(get_mongo_collection)
):
```

## [Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/) w/ FastAPI
**`get_config` Function**:
- This function acts as a **dependency provider** for the configuration object.
- It simply returns the pre-loaded `config` object from `app.py`.
**Dependency Injection in `query_api`**:
    - FastAPI’s `Depends(get_config)` automatically injects the `config` object into the `query_api` function.
**Modular Reuse**:
    - `get_config` can now be reused across all endpoints in your application without requiring repetitive imports or global variables.

So the configurations are now global and mapped to Pydantic BaseModel Configs found in `multiquery -> core -> config.py`

---
### How exactly is this project leveraging dependency injection?

   1. `Depends(get_provider_factory)`: Before query_api is executed, FastAPI calls the
      get_provider_factory function (from backend/multiquery/api/dependencies.py). This
      function is responsible for creating an instance of ProviderFactory, which knows how to
      create the various LLM providers based on your configuration. The returned
      ProviderFactory instance is then passed as the factory argument to your endpoint.

   2. `Depends(get_mongo_client)`: Similarly, FastAPI calls get_mongo_client (from
      backend/multiquery/utils/mongodb_client.py) to establish a connection to your MongoDB
      database and passes the resulting client object as the mongo_client argument.

  This design pattern decouples the endpoint logic from the instantiation of its
  dependencies, making the code cleaner and easier to test.

---
## Refactoring Config file
Previous config file had llms providers seperated from their configs:
```yaml
llm_providers:
  - name: chatgpt
    class_path: multiquery.llm_providers.chatgpt.ChatGPTProvider
    api_key: "YOUR_CHATGPT_API_KEY"
  - name: grok
    class_path: multiquery.llm_providers.grok.GrokProvider
    api_key: "YOUR_GROK_API_KEY"
  - name: gemini
    class_path: multiquery.llm_providers.gemini.GeminiProvider
    api_key: "YOUR_GEMINI_API_KEY"

llm_configs:
  - name: chatgpt
    model: gpt-4o-mini
    max_tokens: 100
    temperature: 0.5
```

Makes more sense to combine these:
```yaml
llms_providers:
  - name: chatgpt
	class_path: multiquery.llm_providers.chatgpt.ChatGPTProvider
	api_key: "YOUR_CHATGPT_API_KEY"
	config:
		model: gpt-4o-mini
		max_tokens: 100
		temperature: 0.5
```

And you'll need to update your Pydantic models to match the new config structure. 
Specifically, the `config.py` file which defines all mapping config objects

---
## Dependency Injection and Factory Pattern

>[!info]- **How DI and Factory Pattern Work Together**
>#### **1. DI for Configs**
>- FastAPI uses `get_config` to inject the `AppConfig` object into endpoints or services.
>- This removes the need for manual configuration management in the endpoints.
>
>#### **2. Factory for Providers**
>- The `ProviderFactory` uses the injected `AppConfig` to dynamically instantiate providers.
>- The factory abstracts away the complexity of creating and configuring provider instances.
>
>#### **3. Injecting Providers via DI**
>
>- The factory itself can be injected into endpoints using FastAPI’s DI system.
>- Example:
>    `@router.post("/") async def query_api(factory: ProviderFactory = Depends(get_provider_factory)):     providers = factory.create_providers()     ...`
>    
>#### **Combined Flow**
>1. FastAPI resolves `get_config` to provide the `AppConfig`.
>2. The `ProviderFactory` is instantiated with `AppConfig` to create providers.
>3. Providers are injected into endpoints or services as needed.

Couple of improvements need to be made to the current implementation:
1. **~={cyan}Dependency Injection=~**: Inject pre-configured `ProviderFactory` objects instead of instantiating them in endpoints.
2. **~={cyan}Factory Pattern=~:** Use a fully centralized `ProviderFactory` class instead of partially implemented dynamic instantiation.
### ~={red}**TODO**:=~ Going to refactor the rest of this later. For now, moving on. 

# Ability to select LLM Provider
Accept a `providers` query parameter (e.g., `?providers=chatgpt,grok`) to filter which LLM providers are used.

---
# Logging
### **What is Middleware?**
Middleware in FastAPI is a layer of code that runs **before and/or after** every request that your application processes. Middleware allows you to intercept requests **before they hit your endpoints** (e.g., `/query`) and modify the request or perform some action (like logging). Similarly, it can also intercept the response **before it is sent back to the client**.

Think of middleware as a "wrapper" around your app’s endpoints. It gives you control over what happens at the request and response level.

---

# 

---

#backend #fastapi #webapp #multiquery #research #development #pydantic #configs #dependencyinjection #fastapi #python #importlib