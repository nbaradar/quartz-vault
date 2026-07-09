---
title: Web UI
tags:
  - lab
  - multiquery
  - contextcore
  - userinterface
created: 2025-06-29

modified: 2025-06-29

published: 2025-06-29

---
# Overall App Tasks
- [ ] DB Integrations ➕ 2025-01-07
	- [x] MongoDB Client ✅ 2025-01-07
	- [ ] MongoDB CRUD Operations
		- [x] save_query_result ✅ 2025-01-07
		- [ ] read_result
			- [ ] based on dates
			- [x] based on id
			- [ ] based on user
			- [ ] based on chatID
		- [x] delete_result
		- [x] update_result
	- [x] MongoDB Config Injections ✅ 2025-01-07
- [ ] Create DB Schema
- [x] Create Frontend ✅ 2025-01-14
	- [x] Initial MVP ✅ 2025-01-14
		- [x] Create Chat area with text ✅ 2025-01-14
		- [x] Create Text area ✅ 2025-01-12
		- [x] Create button to submit ✅ 2025-01-12
		- [x] Create LLM selection ✅ 2025-01-14
- [x] Connect FrontEnd to Backend ✅ 2025-01-23


---
# Plan
We're going to start building a simple Web UI using the POC engine. It's very easy to convert the CLI into a webapp. Just make each function an endpoint that you call. 

Stack:
- frontend = react
- backend = flask
- communication = rest
- db = mongo (nosql)

- Create API endpoints for:
    - Submitting queries.
    - Fetching results.
    - Managing provider configurations.
- Build a web frontend to:
    - Display a query input form.
    - Show query results dynamically.
    - Include export options (Markdown/JSON).

---
### **Frontend Options**

#### **1. Lightweight Option: HTML, CSS, JavaScript**
- Best if you want a quick, simple interface.
- Ideal for proof-of-concept with minimal complexity.
- Can be extended later with frameworks.
#### **2. Modern Framework: React**
- Highly recommended for scalable and interactive applications.
- Allows you to create reusable components (e.g., query forms, results display).
- Seamless integration with APIs for dynamic content.
#### **3. Backend-Centric: Flask or FastAPI with Jinja2 Templates**
- If you prefer a backend-heavy approach, serve HTML templates directly from your Python backend.
- Good for keeping everything Python-based.

---
### **Suggested Approach: React Frontend + FastAPI Backend**

#### Why React?
- Component-based, making it easy to build and maintain.
- Ecosystem support for state management (e.g., Redux, Context API).
- Rich developer tools and community support.
#### Why FastAPI?
- Great for serving REST APIs and handling requests from the frontend.
- Native support for async operations, perfect for querying providers and the database.
- Easy to extend with authentication, middleware, and more.

---
### **Plan to Build the Frontend**

#### **Step 1: Set Up FastAPI Backend**
- Define REST API endpoints for the frontend to interact with.
- Key endpoints:
    1. `/query`: Accepts user input and returns responses from providers.
    2. `/history`: Retrieves stored queries and responses from the database.
    3. `/export`: Exports query results in Markdown or JSON format.
#### **Step 2: Set Up the React Frontend**
- Key pages/components:
    1. **Home Page**: Input form for user queries, displaying provider results dynamically.
    2. **History Page**: View past queries and results.
    3. **Settings Page**: Manage provider configurations (e.g., enable/disable providers).
#### **Step 3: Connect Frontend and Backend**
- Use `fetch` or `axios` in React to send requests to the FastAPI backend.
- Use JSON responses to dynamically update the UI.
#### **Step 4: Style the Application**
- Add basic styling with CSS or use a library like TailwindCSS or Material-UI for a polished look.

---
### **Next Steps**
1. **Start with Backend (FastAPI)**:
    - Define and test the REST endpoints.
    - Prepare the API documentation using FastAPI's built-in Swagger UI.
2. **Set Up React Project**:
    - Use `create-react-app` to quickly scaffold the project.
    - Focus on the Home Page first to handle user queries.
3. **Iterative Development**:
    - Build the core querying functionality first.
    - Gradually add features like history and exports.
## QUERY
```
I would like to start with the FastAPI backend for the frontend to interact with. I also currently have a mongodb server running locally. The database is called MultiQuery and there is one collection called result that stores the results of each query. I'm open to improving everything as well. Let's try to integrate my existing POC code with the backend as well so that code doesn't go to waste. We can refactor code as needed. 

This is what my current codebase looks like: 

multiquery/
|--> multiquery/
      |--> config/
            |--> config.yaml
      |--> llm_providers/
            |--> __init__.py
            |--> base.py
            |--> chatgpt.py
            |--> gemini.py
            |--> grok.py
      |--> utils/
            |--> __init__.py
            |--> config_loader.py
            |--> json_exporter.py
            |--> mongodb_client.py
      |---> __init__.py
      |---> main.py
|--> output/
```
---

#multiquery #multiquery #research #development 

%% Begin Waypoint %%
- [[Axios]]
- [[Backend FastAPI + Pydantic]]
- [[Chat History Feature]]
- [[Debugging with uvicorn]]
- [[Frontend Dev Notes]]
- [[Initial Front End Plan]]
- [[MongoDB connection]]
- [[NPM Hints]]
- [[React]]
- [[Realtime Features]]
- [[Tailwind CSS]]

%% End Waypoint %%
