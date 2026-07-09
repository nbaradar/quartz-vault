---
title: Debugging with uvicorn
tags:
  - multiquery
  - contextcore
  - userinterface
  - lab
created: 2025-06-29

modified: 2025-06-29

published: 2025-06-29

---
Yes, it is possible to run **Uvicorn** in debug mode within **VS Code** to debug your FastAPI application. This involves configuring the VS Code debugger to run Uvicorn with your FastAPI application and enabling breakpoints for debugging.

---

### **Steps to Debug Uvicorn in VS Code**

#### **1. Install Required Extensions**

Ensure you have the following extensions installed in VS Code:

- **Python** (by Microsoft).
- **Debugger for Python**.

---

#### **2. Configure `launch.json`**

Set up a debug configuration in VS Code.

1. Go to the **Run and Debug** view in VS Code (`Ctrl + Shift + D` or click the play icon on the left sidebar).
2. Click on **"create a launch.json file"** if you don’t already have one.
3. Select **"Python"** as the environment.
4. Add a configuration for Uvicorn:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Uvicorn App",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "multiquery.app:app",
        "--reload",
        "--host",
        "127.0.0.1",
        "--port",
        "8000"
      ],
      "jinja": true
    }
  ]
}
```

---

#### **3. Key Points in the Configuration**

- `"module": "uvicorn"`:
    - This runs Uvicorn directly as a module (`python -m uvicorn`).
- `"args"`:
    - `"multiquery.app:app"`: Path to your FastAPI app instance (`app` in `multiquery/app.py`).
    - `"--reload"`: Enables hot-reloading for development.
    - `"--host"` and `"--port"`: Specify the host and port for the app.
- `"jinja": true`:
    - Useful if you're using Jinja templates.

---

#### **4. Set Breakpoints**

1. Open the files you want to debug (e.g., `query.py`, `llm_service.py`).
2. Click in the gutter next to a line of code to set a breakpoint.

---

#### **5. Start Debugging**

1. In the **Run and Debug** view, select the **Debug Uvicorn App** configuration.
2. Click the green **Start Debugging** button (`F5`).
3. VS Code will start the server, and you can use the debugger.

---

#### **6. Test the Debugger**

1. Make a request to the server, such as:
    
    ```bash
    curl -X POST "http://127.0.0.1:8000/query/" \
         -H "Content-Type: application/json" \
         -d '{"prompt": "What is the capital of France?"}'
    ```
    
2. Execution will pause at any breakpoints you've set, allowing you to inspect variables, step through code, and debug effectively.

---

### **Additional Tips**

- **Inspect Variables**: Use the debug console (`Ctrl + ~`) to inspect variables and test expressions.
- **Reload on Changes**: If hot-reloading is causing issues, remove the `--reload` flag from the `args` section.
- **Performance Considerations**: Debug mode is slower because of additional overhead, so use it for development only.

---

Let me know if you encounter any issues setting this up or need further clarification! 😊

---
#debugging #uvicorn #python #research #development