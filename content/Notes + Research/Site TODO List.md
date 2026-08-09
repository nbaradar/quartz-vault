---
title: Site TODO List
tags:
  - meta
created: 2025-06-29
modified: 2025-10-26
published: 2025-06-29
draft: true
---
# Outstanding Tasks

- [x] Fix mobile formatting - site looks messed up from mobile client
- [ ] **update aug 8:** make a quick script that creates proper index pages for the folders and updates the index pages. allow flexibility if you want to include specific things for specific folders. and then have it auto run in the warp workflow script by calling the script every time you build locally or sync to github. 
- [ ] Current Recently updated section isn't updating correctly. I want to show the most recently updated/created notes in order. Check what data source the filtering is using
- [ ] Automate a means to always auto-generate wiki style links any time a page with the "#concept" tag matches a word. So for instance, if I write a summary about a new Microsoft news article, it should auto-generate links so that users can hover over the story summary for concepts they may not be aware of. Don't do this for other tags, only makes sense for concept tag 
- [ ] Add Analytics
	- Use this free tool: https://umami.is/
	- Read config guide here: https://quartz.jzhao.xyz/configuration#general-configuration
	- Seems quite simple. Just add the analytics to `quartz.config.ts`
- [ ] Update Color Theme
	- Change from the default to a selected palette. Should be similar to ContextCore overall design language
- [ ] Remove Quartz/GitHub/Discord Links at bottom of Page
	- Remove the default links at the bottom of the site. Makes it look cheap and lame
- [ ] Create DNS entry for website name
	- Instructions to [add custom Domain](https://quartz.jzhao.xyz/hosting#custom-domain)
- [ ] Fix left pane not refreshing due to caching
	- Check if there's a configuration. 
- [ ]  Flesh out Project Pages
       * For each project in Personal Projects, create a detailed write-up. Don't just have notes. Have a
         proper project page that answers:
           * **Problem**: What problem were you trying to solve?
           * **Solution**: How did you solve it? What was the architecture?
           * **Tech Stack**: What technologies did you use?
           * **Link**: A link to the GitHub repository and, if possible, a live demo.
       * This is the single most important thing you can do. A portfolio with 2-3 well-documented projects is 
         infinitely more valuable than 100 pages of notes.
- [ ] Right now your categories are documented in Start Here, but readers will find it even easier if (for example) you:
    1. Add a collapsible “Categories” section in your Quartz sidebar (via `quartz.layout.ts` or `quartz.config.ts`), linking directly to each tag index.
    2. Generate simple index pages (e.g. `concept/index.md`, `study/index.md`) so category landing pages are one click away.
- [ ] SEO & descriptions — consider adding a brief `description:` field in the front‑matter of key pages (especially your homepage and upcoming “hire-me” page) to improve discoverability.

---
# Quartz Sites for Inspiration:
- https://github.com/plastic-labs/blog: Looks like some sort of AI lab. Really cool styling
- https://tjapit.com/: Wow this guy went all out, his garden has some REALLY cool stuff. 
- https://quartz.eilleeenz.com/: Another really well designed site with tons of customization (and a comment section)
- https://luciradis.arczenpulse.dev/: Look at this for how to implement comment section
Wait I just realized Quartz supports comments officially lol. It's probably not hard: https://quartz.jzhao.xyz/features/comments

- https://ravenpedia.xyz/: This site has an interesting way of organizing info into slides. Might be useful for ContextCore and subsystems
- https://fxnotes.xyz/notes/64-bit/: This guy had a cool idea of adding an "Edit Source" button at the top of pages that open a PR to the markdown file
	- He also has cool styling on tags and changed the bottom links
- https://smit4450.github.io/Legends-of-Ril/: I like how he replaced the background image and some of the styling. Might be useful
- https://www.pelayoarbues.com/: This guy has a "See More" button on his Recent Posts section. 
- https://elaraks.github.io/dampcapital/
- 
