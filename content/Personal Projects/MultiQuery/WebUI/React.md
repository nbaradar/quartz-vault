---
title: React
tags:
  - multiquery
  - contextcore
  - userinterface
  - guide
created: 2025-06-29

modified: 2025-06-29

published: 2025-06-29

---
>[!info] Quick Notes
>- **Functional Components** are the preferred modern approach (use 'function' keyword)
>- For **single-page applications (SPAs)**, you’ll likely use **React Router** for navigation
>- To **share state between components**, you often **"lift state up"** to a common parent.
>- React updates the DOM when **state** or **props** change. Each component can have it's own state
### **Common React Event Handlers**
React supports a variety of event handlers beyond `onChange`. These are the most common:

| **Event Handler** | **Purpose**                                                                        |
| ----------------- | ---------------------------------------------------------------------------------- |
| `onClick`         | Fired when an element (e.g., button, div) is clicked.                              |
| `onChange`        | Fired when the value of an input, textarea, or select changes.                     |
| `onSubmit`        | Fired when a form is submitted.                                                    |
| `onInput`         | Similar to `onChange`, triggered as the user types (useful for immediate updates). |
| `onFocus`         | Fired when an element gains focus.                                                 |
| `onBlur`          | Fired when an element loses focus.                                                 |
| `onKeyPress`      | Fired when a key is pressed (deprecated, use `onKeyDown` or `onKeyUp`).            |
| `onKeyDown`       | Fired when a key is pressed down.                                                  |
| `onKeyUp`         | Fired when a key is released.                                                      |
| `onMouseEnter`    | Fired when the mouse pointer enters an element.                                    |
| `onMouseLeave`    | Fired when the mouse pointer leaves an element.                                    |

### **Key Concepts to Understand**
1. **Props vs State**:
    - `Props`: Data passed from a parent to a child component. Immutable in the child.
    - `State`: Data that a component manages internally. Changes to state trigger re-renders.
2. **Reactivity**:
    - React tracks which components depend on state/props and re-renders them when those values change.
3. **Unidirectional Data Flow**:
    - Data flows from parent to child via props.
    - Child components notify parents of changes (e.g., toggling a provider) via callback functions passed as props.

---
## **What is React?**
- React is a **JavaScript library for building user interfaces**.
- It allows you to build UI components that are reusable and declarative.
	- In the context of React, "declarative" means that ==developers describe what the user interface (UI) should look like based on its current state, without explicitly stating how to achieve that state==; essentially, you tell React what you want the UI to be, and React handles the necessary updates to the DOM to make it happen, making the code more readable and maintainable.
- React is component-based and uses a **virtual DOM** to efficiently update the UI.

---
## **How Does React Work?**
At its core, React is a **declarative UI library**. Instead of manually manipulating the DOM, you declare what the UI should look like based on the **current state** and **props** (data passed to components). React takes care of updating the DOM when the state or props change.

### **Understanding State in React**
1. **State**:
    - State is a special data structure that React uses to track values that change over time (like your `query` variable).
    - Each component can have its own state, and when the state changes, React automatically re-renders the component.
2. **Example: State in React**:
```jsx
import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState(""); // Declare state with initial value ""

  const handleChange = (e) => {
    setQuery(e.target.value); // Update state when user types
  };

  return (
    <div>
      <h1>{query}</h1> {/* React dynamically updates this whenever query changes */}
      <input type="text" value={query} onChange={handleChange} />
    </div>
  );
}

export default App;

```

**What happens when the user types in the input field?**
    - The `onChange` event is triggered.
    - `setQuery(e.target.value)` updates the `query` state.
    - React detects that the state (`query`) has changed and automatically re-renders the component, updating the `<h1>{query}</h1>` element in the DOM.

## **Core Concepts You Should Know**
#### **1. Components**
- **What**: Building blocks of a React application. Each piece of the UI (e.g., a button, form, or dropdown) is a component.
- **Types**:
    - **Functional Components** (modern approach, uses `function` keyword).
    - **Class Components** (older, less common in modern development).
- **Example**:
    
    ```jsx
    function Greeting() {
        return <h1>Hello, World!</h1>;
    }
    ```
#### **2. JSX**
- **What**: A syntax extension that lets you write HTML-like code in JavaScript.
- **Key Rules**:
    - Always return a **single parent element** (use a `<div>` or `<>` for grouping).
    - Use `{}` for embedding JavaScript expressions.
- **Example**:
    ```jsx
    function Greeting() {
        const name = "Nader";
        return <h1>Hello, {name}!</h1>;
    }
    ```
#### **3. Props**
- **What**: Short for "properties," these are inputs to components that allow them to be dynamic.
- **How**: Passed to components as attributes.
- **Example**:
    ```jsx
    function Greeting({ name }) {
        return <h1>Hello, {name}!</h1>;
    }
    
    // Usage
    <Greeting name="Nader" />
    ```
#### **4. State**
- **What**: A way to manage data within a component that can change over time (e.g., user input).
- **How**: In functional components, you use the `useState` hook.
- **Example**:
    ```jsx
    import React, { useState } from 'react';
    
    function Counter() {
        const [count, setCount] = useState(0);
    
        return (
            <div>
                <p>Count: {count}</p>
                <button onClick={() => setCount(count + 1)}>Increment</button>
            </div>
        );
    }
    ```
#### **5. Events**
- **What**: React handles DOM events using camelCase syntax (e.g., `onClick`, `onChange`).
- **Example**:
    ```jsx
    function Button() {
        function handleClick() {
            alert('Button clicked!');
        }
    
        return <button onClick={handleClick}>Click Me</button>;
    }
    ```
#### **6. Hooks**
- **What**: Special functions that let you "hook into" React features like state and lifecycle.
- **Common Hooks**:
    - `useState`: Manage local state.
    - `useEffect`: Handle side effects like fetching data.
- **Example** (`useEffect` for data fetching):
    ```jsx
    import React, { useState, useEffect } from 'react';
    
    function App() {
        const [data, setData] = useState([]);
    
        useEffect(() => {
            fetch('https://api.example.com/data')
                .then((response) => response.json())
                .then((data) => setData(data));
        }, []); // Empty dependency array means it runs once after render
    
        return (
            <ul>
                {data.map((item) => (
                    <li key={item.id}>{item.name}</li>
                ))}
            </ul>
        );
    }
    ```
#### **7. Routing**
- For single-page applications (SPAs), you’ll likely use **React Router** for navigation.
- Example:    
    ```bash
    npm install react-router-dom
    ```

    ```jsx
    import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
    
    function App() {
        return (
            <Router>
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/about" component={About} />
                </Switch>
            </Router>
        );
    }
    ```
#### **8. Lifting State Up**
- To share state between components, you often "lift state up" to a common parent.
- **Example**:
    ```jsx
    function Parent() {
        const [value, setValue] = useState("");
    
        return (
            <div>
                <Input value={value} onChange={setValue} />
                <p>You typed: {value}</p>
            </div>
        );
    }
    
    function Input({ value, onChange }) {
        return (
            <input
                type="text"
                value={value}
                onChange={(e) => onChange(e.target.value)}
            />
        );
    }
    ```

---
## **React Workflow**
1. **Create Components**: Break down your UI into reusable pieces.
2. **Use Props and State**: Pass data between components using `props` and manage dynamic data using `state`.
3. **Fetch Data**: Use `useEffect` for API calls.
4. **Styling**:
    - Use plain CSS, a library like Tailwind, or CSS-in-JS solutions like `styled-components`.
5. **Test and Iterate**: Use tools like React DevTools to debug and improve.
---