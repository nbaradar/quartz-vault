---
title: Claude Code Install
tags:
  - ai/ml
  - anthropic
  - claude
  - guide
draft:
created: 2025-07-19

modified: 2025-07-20
published: 2025-07-19

---
>[!important]- **You** must **have a** **pro account**
>[Pricing](https://www.anthropic.com/pricing) 
>- `$17/month` if billed annually
>- `$20/month` if billed monthly.
>
>Also comes with more usage and more models. 

>[!info] Relevant Links
>[Using Claude w/ Pro or Max Plan](https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
>[Claude Code Developer Docs](https://docs.anthropic.com/en/docs/claude-code/overview)

Very easy, first ensure you have [Node.js version 18](https://nodejs.org/en/download) or higher installed.

Then simply install it using npm: 
```bash
npm install -g @anthropic-ai/claude-code
```

![[Pasted image 20250720153545.png]]

And that's quite literally it. You now have access to ClaudeCode on your machine. Now to USE ClaudeCode, first navigate to the directory where you want to work... (in this example I will navigate to my Obsidian Vault that contains this site so Claude has access to all my notes)
```bash
cd "/Users/naderbaradar/Library/Mobile Documents/iCloud~md~obsidian/Documents/quartz-vault/quartz"
```

And then run ClaudeCode by issuing this command:
```bash
claude
```

And that's it! First it will ask you what color themes you like...
![[Pasted image 20250720153914.png]]

And then it will ask you to authenticate with your pro/max account. You could also use and API key if you want.
![[Pasted image 20250720154034.png]]

If you choose to log in with your subscription, you will be directed to Anthropics login page, and then asked to authorize ClaudeCode to your account:
![[Pasted image 20250720154229.png|500]]

And that's it! [[Claude Code#Additional Tips/Tricks|Click here for additional tips and tricks.]]