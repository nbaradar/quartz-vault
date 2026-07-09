---
title: Quartz Site
description: A guide on how to turn your Obsidian Vault into a Website using Quartz and GitPages
draft: false
tags:
  - obsidian
  - guide
date: 2025-06-10
created: 2025-06-10

modified: 2025-06-29

published: 2025-06-10

---
Showing how to set up and configure quartz with obsidian. And also how to easily host it with GitHub Pages/Netfliy/CloudFlare

# Local Setup
## Quartz 3 Instructions (Hugo Based)
Create a new Vault for Quartz Website. I called it `quartz-vault`
Downloaded Quartz files from github and put the `quartz-site` folder into your `quartz-vault`

Quartz runs on Hugo, so the next step would be to download hugo:
```bash
brew install hugo

hugo version
hugo v0.147.8+extended+withdeploy darwin/arm64 BuildDate=2025-06-07T12:59:52Z VendorInfo=brew
```
Make sure version returns with something. 

Next navigate to where your `quartz-site` folder is with a terminal
```bash
cd /Users/naderbaradar/Library/Mobile Documents/iCloud~md~obsidian/Documents/quartz-vault/quartz-site/
ls
CODE_OF_CONDUCT.md	docs			quartz
Dockerfile		globals.d.ts		quartz.config.ts
LICENSE.txt		index.d.ts		quartz.layout.ts
README.md		package-lock.json	tsconfig.json
content			package.json
```

Then simply run site on an Hugo server:
```bash
hugo server
```

## Quartz 4 Instructions (Next.js + Typescript)
Navigate to where your `quartz-site` folder is with a terminal
```bash
cd /Users/naderbaradar/Library/Mobile Documents/iCloud~md~obsidian/Documents/quartz-vault/quartz-site/
ls
CODE_OF_CONDUCT.md	docs			quartz
Dockerfile		globals.d.ts		quartz.config.ts
LICENSE.txt		index.d.ts		quartz.layout.ts
README.md		package-lock.json	tsconfig.json
content			package.json
```

Now clone the official quartz github repo, navigate to the quartz folder, and install all dependencies with `npm i`. Then initialize the quartz project.
```bash
git clone https://github.com/jackyzha0/quartz.git
cd quartz
npm i
npx quartz create
```

Then we need to set up our Quartz repo in Github. Do **not** initialize the new repository with `README`, license, or `gitignore` files.

![[Pasted image 20250610195752.png]]

Next, list your git remotes in your local quartz git repo:
```bash
git remote -v
origin	https://github.com/jackyzha0/quartz.git (fetch)
origin	https://github.com/jackyzha0/quartz.git (push)
upstream	https://github.com/jackyzha0/quartz.git (fetch)
upstream	https://github.com/jackyzha0/quartz.git (push)
```

If your origin is not the repo you just created on GitHub, change it:
```bash
git remote set-url origin git@github.com:nbaradar/quartz-vault.git

git remote -v
origin	git@github.com:nbaradar/quartz-vault.git (fetch)
origin	git@github.com:nbaradar/quartz-vault.git (push)
upstream	https://github.com/jackyzha0/quartz.git (fetch)
upstream	https://github.com/jackyzha0/quartz.git (push)
```

**MAKE SURE** the upstream remote is set to `https://github.com/jackyzha0/quartz.git` so you can get updates.

Test the updates by issuing the `npx quartz sync --no-pull` command:
```bash
npx quartz sync --no-pull

 Quartz v4.5.1 

Backing up your content
[v4 06e1d47] Quartz sync: Jun 10, 2025, 7:51 PM
 3 files changed, 17 insertions(+)
 delete mode 100644 content/.gitkeep
 create mode 100644 content/index.md
 create mode 100644 content/testpage.md
Pushing your changes
Enumerating objects: 11501, done.
Counting objects: 100% (11501/11501), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4114/4114), done.
Writing objects: 100% (11501/11501), 10.92 MiB | 2.12 MiB/s, done.
Total 11501 (delta 7303), reused 11466 (delta 7274), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (7303/7303), done.
To github.com:nbaradar/quartz-vault.git
 * [new branch]      v4 -> v4
branch 'v4' set up to track 'origin/v4'.
Done!
```
> [!info] In future updates, you can simply run `npx quartz sync` every time you want to push updates to your repository.

---
Added `index` and `testpage` markdown files in the `quartz -> content` folder using obsidian. REMEMBER [[#Things to note|FRONTMATTER]].

Sync with github so it shows up (just do `npx quartz sync`):
![[Pasted image 20250610201646.png]]

Now you can try building it locally. Navigate to the root of your quartz folder and run the app:
``` bash
npx quartz build --serve

 Quartz v4.5.1  

Cleaned output directory `public` in 1ms
Found 2 input files from `content` in 6ms
Parsed 2 Markdown files in 59ms
Filtered out 0 files in 20μs
Emitted 18 files to `public` in 876ms
Done processing 2 files in 944ms
Started a Quartz server listening at http://localhost:8080
```

Navigate to `http://localhost:8080` and you should see your test page in the browser:
![[Pasted image 20250610202136.png]]

---
## Publishing your notes on GitPages
It's actually very easy, just follow [this guide](https://quartz.jzhao.xyz/hosting#github-pages). 

Once you are done, you can go to your repos Settings, then to Pages in the left tab and you'll see your sites URL
![[Pasted image 20250610205935.png]]
## Things to note
```
---
title: Home
draft: false
---
```
You need to add this to the top of any page inside of the content folder if you want it to render. `draft: false` is critical. This plugin is called [Frontmatter](https://quartz.jzhao.xyz/plugins/Frontmatter). 

