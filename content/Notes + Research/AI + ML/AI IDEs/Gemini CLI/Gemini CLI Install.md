---
title: Gemini CLI Install
tags:
  - guide
  - ai/ml
  - gemini
  - google
created: 2025-06-28

modified: 2025-07-19

published: 2025-06-28

---
Very easy, first ensure you have [Node.js version 18](https://nodejs.org/en/download) or higher installed.

From here you have 2 options. Either you can run the terminal by running the remote package with `npx` OR you can install the package locally with `npm install`

1. Run the CLI: Execute this command in your terminal
	```bash
	npx https://github.com/google-gemini/gemini-cli
	```
2. Install the CLI: Execute these commands in your terminal
	```bash
	npm install -g @google/gemini-cli
	gemini
	```

I choose to install it locally. Verify that the install worked by listing all your packages globally:
```bash
npm list -g

/Users/naderbaradar/.nvm/versions/node/v22.16.0/lib
├── @google/gemini-cli@0.1.7
├── corepack@0.32.0
└── npm@10.9.2
```

Once done, just type `gemini` into the terminal and you'll see the app start up:
![[Pasted image 20250628151907.png|700]]

Pick your theme (I went with `Dracula Dark`) and then either log into your Google account or Use an API key. Personally, I choose to use an API key as I feel it will give me more granular control. 

To do this, go to [Google AI Studio](https://aistudio.google.com/) and click the "Get API key" button at the top
![[Pasted image 20250628153254.png|450]]

Then click the "Create API Key" button and you will be provided with a newly generated key.
![[Pasted image 20250628153432.png|450]]

**DO NOT SHARE THIS KEY**. You will have to generate a new key if you lose or leak this one. (Which isn't a big deal, just delete it and create another)

Next, open a terminal and create an environment variable for your newly generated API key. First, export the variable, then run an echo to make sure it was set correctly. 
```bash
naderbaradar@Naders-MacBook-Air ~ % export GEMINI_API_KEY="YOUR_API_KEY"

naderbaradar@Naders-MacBook-Air ~ % echo $GEMINI_API_KEY
YOUR_API_KEY
```
NOTE: YOU MUST NAME THE ENV VARIABLE AS `GEMINI_API_KEY`

Then go back to the Gemini CLI and select `Gemini API Key (AI Studio)`

![[Pasted image 20250628153555.png|600]]

And that's it! You should see this screen if you are successful:
![[Pasted image 20250628154820.png|600]]
