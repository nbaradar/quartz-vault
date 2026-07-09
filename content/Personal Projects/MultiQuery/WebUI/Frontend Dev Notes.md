---
title: Frontend Dev Notes
tags:
  - multiquery
  - contextcore
  - userinterface
  - lab
created: 2025-06-29

modified: 2025-06-29

published: 2025-06-29

---
## Overview
We will most likely be using...
- [[React]] for the front end UI
	- React-Select for dropdown menus
- [[Axios]] for making HTTP requests to the backend
- [[Tailwind CSS]] or Material UI for styling
	- Might want to look into other styling options
	- Will use [shadcn/ui](https://ui.shadcn.com/)

## Initialize React Project
#### Install NPM
npx is an npm command. we need to install NPM first. NPM comes with Node.js, so let's install it from their websites recommended method:
1. Install Node Version Manager (nvm)
2. Use nvm to install Node.js
```bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# Download and install Node.js:
nvm install 22

# Verify the Node.js version:
node -v # Should print "v22.13.0".
nvm current # Should print "v22.13.0".

# Verify npm version:
npm -v # Should print "10.9.2".

```
#### Initialize React App
```bash
npx create-react-app frontend
cd frontend
npm install axios react-select
```

>[!info]- npx VS npm
> NPM = Install and run package
> NPX = Run the package but don't install it
> 
> One installs a package/dependency for your project, saves it under node_modules and also in the package.json, example: npm i express
> The other one "executes" the package, only for that run, and doesn't save anything anywhere, for example: npx create-react-app
##### IMPORTANT: VULNERABILITIES
~={red}**TODO**=~ You still need to address these 6 vulnerabilities at a later date: 
```
* **nth-check < 2.0.1 (high severity):** This vulnerability is related to inefficient regular expression complexity in `nth-check`. 
* **css-select <= 3.1.0 (depends on vulnerable nth-check):** This vulnerability is inherited from the dependency `nth-check`. 
* **svgo 1.0.0 - 1.3.2 (depends on vulnerable css-select):** This vulnerability is inherited from the dependency `css-select`. 
* **@svgr/plugin-svgo <= 5.5.0 (depends on vulnerable svgo):** This vulnerability is inherited from the dependency `svgo`. 
* **@svgr/webpack 4.0.0 - 5.5.0 (depends on vulnerable @svgr/plugin-svgo):** This vulnerability is inherited from the dependency `@svgr/plugin-svgo`. 
* **react-scripts >= 2.1.4 (depends on vulnerable @svgr/webpack and resolve-url-loader):** This vulnerability is inherited from the dependencies `@svgr/webpack` and `resolve-url-loader`. 
* **resolve-url-loader < 0.0.1-experiment-postcss || 3.0.0-alpha.1 - 4.0.0 (moderate severity):** This vulnerability is related to PostCSS line return parsing errors. 
* **postcss < 8.4.31 (moderate severity):** This vulnerability is also related to PostCSS line return parsing errors.
```

## Create REACT Components
Going to go with these techs
- **Tailwind CSS**: The base styling framework. It provides utility classes you use to style all components.
- **shadcn/ui**: A source of customizable, unstyled components that you can style with Tailwind. These will form the core of your application’s custom design system.
- **DaisyUI**: A helper library for prototyping with pre-styled components, speeding up the development process for less critical UI elements.

For now I'm just going to use DaisyUI to create a text output area and a text input area with a dropdown to select LLMs 
I will potentially switch to shadcn later when I understand react better.

```bash 
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
npm install daisyui
```

>[!attention] VSCode Compatibility
>Get Tailwind VSCode Extension: [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)
>Add tailwind to CSS file associations in the VSCode `settings.json` file (`command+shift+p: open user settings(JSON)`)
>```JSON
>"files.associations": {
>	"*.css": "tailwindcss"
>	}
>```

Comments in JSX:
```jsx
{/* This is a single-line comment in JSX */}
{/* This is a 
   multi-line comment in JSX */}
```

Created 3 Component. Comments can be found in files themselves
- App.jsx
- ChatHistory.jsx
- ChatInput.jsx

You'll need to create message objects in store them in the mongodb history. Right now, queries are being saved in a db called "result"
Think about how you want to approach saving chats. It should probably be per user
This means youll have
- `user` object
	- info about the user
	- contains `user_preference` object
	- contains chat 
- `user_preference` object
	- configs and preferences tied to `user` (api keys for instance)
- `chat_message` object
	- contains a `result` object tied to a `user` object
	- contains a `chat_id`
- `chat_window` object
	- contains `chat_window_id`
	- contains list of chat_message objects tied by `chat_id`
- `chat_configs` object
	- maps to `chat_id`
	- contains configs for each chat (llm provider configs for instance)
- `result` object

##### **[[MongoDB connection#MongoDB Schema Design|Refined Schema Design for This Data]]** that was made using ChatGPT

#### FrontEnd DaisyUI Tasks
- [ ] Theme controller is used to change page theme https://v5.daisyui.com/components/theme-controller/
- [ ] You'll want to use https://daisyui.com/components/badge/ for the LLM labels on QueryDisplay
- [ ] You can use https://daisyui.com/components/avatar/ for a UI profile button
- [ ] Maybe you can make ResultWindow a carousel https://daisyui.com/components/carousel/
- [ ] Loading can be used when fetching results: https://daisyui.com/components/loading/
	- [ ] Or you can use load progress https://daisyui.com/components/progress/
- [ ] You can update the checkbox https://daisyui.com/components/checkbox/
	- [ ] https://daisyui.com/components/toggle/ using toggles might look cooler
- [ ] You can use range to set the model temps https://daisyui.com/components/range/
- [x] Should use textarea for inputsection https://daisyui.com/components/textarea/ ✅ 2025-01-23
- [ ] Use dividers between your ResultCards https://daisyui.com/components/divider/

# Connect FrontEnd to BackEnd
Now that you have these components created:
- **QueryDisplay**: Displays user query and llm_provider tags at top
- **ResultWindow**: Displays all llm results as individual components
	- **ResultCard**: Displays result for a single llm provider
- **InputSection**: Area where user inputs query. Includes section to choose LLM providers
- **ChatList**: Panel on left that shows the users chats

You'll need to connect them to the backend. 
Currently, when InputSection fires, /query will be called. 
The result will be returned from `const handleSendQuery = (newQuery) => {` which gets called when the submit button is pressed. 
So then, you'll want to initialize the resultWindow with resultcards created from the /query results

>[!error] CORS Needed
> Realized that you will need CORS to run backend/frontend together. 
> Refer here: [[CORS To run Frontend+Backend]]

This is the current flow of your Props and their states (Jan 17)
![[Pasted image 20250117192111.png]]
This diagram illustrates:
- Where state (`query`, `results`, `activeProviders`) is defined (`App.jsx`).
- How props (`onSend`, `activeProviders`, `results`) are passed to child components.
- How `InputSection` communicates with the backend via the `/query` endpoint and how results flow back into the app.

1. **Keep Backend Calls in `App.jsx`**:
    - Make the API call in `handleSendQuery` and update `results`.
2. **Refactor API Calls**:
    - Use a utility or API service file (`api.js`) to centralize the logic for making requests to `/query`.
3. **Optimize Performance**:
    - Use React’s `useCallback` to memoize `handleSendQuery` if it’s passed as a prop to multiple children.
4. **Test Data Flow**:
    - Use React DevTools to verify how `results` propagates from `App.jsx` to `ResultsWindow` and `ResultCard`.

You will need to restructure the /query response. Your current schema is not best practice for JSON
>[!note]- JSON Best Practice
>

# Markdown on ResultCards
First you need to install correct libraries
```bash
npm install react-markdown
npm install remark-gfm
npm install rehype-raw
```

Then update resultCard to use react-markdown

To make it look even better, add typography library from TailWind
```bash
npm install @tailwindcss/typography
```

And add to tailwind configs
```js
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography")],
};
```


---







---

#react #python #frontend #ui #research #development #restapi #rest #axios #css #style #tailwindcss #tailwind #daisyui #jsx
