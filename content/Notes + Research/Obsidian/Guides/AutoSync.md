---
title: AutoSync
description: A guide on how to automatically sync your local Obsidian Vaults with your remote Github Repos so your backed up notes will always be up-to-date.
draft: false
tags:
  - obsidian
  - guide
date: 2025-06-10
created: 2025-06-10

modified: 2025-06-29

published: 2025-06-10

---
> [!warning] This section was written very quickly. I will update it with more detail later.
## Step 1: AutoSync Bash Script
We'll need a script that automates the entire sync process and logs the outcome for you. 
I have created a script, all you need to do is save it somewhere on your computer and add your Vault locations to the script. I know the use of emojis in software development is controversial, but I like them for logs. You can remove them, they start/end with `:`

> [!example]- AutoSync Bash Script
> ```bash
>#!/bin/bash
>#######################################
># Configuration
>#######################################
># Add your vault paths here
>VAULT_PATHS=(
>  "/Users/naderbaradar/Documents/context_core_obsidian_vault"
>  "/Users/naderbaradar/Documents/nader_obsidian_vault"
>)
>
># Master log file
>MASTER_LOG="$HOME/obsidian-autosync-master.log"
>
>#######################################
># Utility Functions
>#######################################
># Log to master log file
>log_master() {
>  echo "$1" >> "$MASTER_LOG"
>}
># Log to vault-specific log file
>log_vault() {
>  local vault_log="$1"
>  local message="$2"
>  echo "$message" >> "$vault_log"
>}
># Get vault name from path
>get_vault_name() {
>  basename "$1"
>}
># Get vault log path
>get_vault_log_path() {
>  local vault_name
>  vault_name=$(get_vault_name "$1")
>  echo "$1/${vault_name}_autosync.log"
>}
># Get timestamp for master log (24-hour)
>timestamp_master() {
>  date '+%Y-%m-%d %H:%M:%S'
>}
>
># Get timestamp for vault logs (12-hour with AM/PM)
>timestamp_vault() {
>  date '+%Y-%m-%d %I:%M:%S %p'
>}
>
>#######################################
># Git Sync Function
>#######################################
>sync_vault() {
>  local path="$1"
>  local vault_name
>  vault_name=$(get_vault_name "$path")
>  local vault_log
>  vault_log=$(get_vault_log_path "$path")
>
>  log_master "=== [$vault_name] Sync started at $(timestamp_master) ==="
>  log_vault "$vault_log" "=== [$vault_name] Sync started at $(timestamp_vault) ==="
>
>  if [[ ! -d "$path/.git" ]]; then
>    log_master ":x: [$vault_name] Not a Git repo. Skipping."
>    log_vault "$vault_log" ":x: Not a Git repository. Skipping sync."
>    return
>  fi
>
>  cd "$path" || {
>    log_master ":x: [$vault_name] Path not found: $path"
>    log_vault "$vault_log" ":x: Path not found: $path"
>    return
>  }
>
>  # Pull
>  git pull origin main >> "$vault_log" 2>&1
>  log_master ":arrows_counterclockwise: [$vault_name] Pulled latest changes."
>
>  # Stage
>  git add . >> "$vault_log" 2>&1
>  log_master ":inbox_tray: [$vault_name] Staged files."
>
>  # Commit if there are changes
>  if ! git diff --cached --quiet; then
>    local now
>    now=$(timestamp_master)
>    git commit -m "Auto sync: $now" >> "$vault_log" 2>&1
>    git push origin main >> "$vault_log" 2>&1
>    log_master ":white_check_mark: [$vault_name] Synced successfully at $now"
>    log_vault "$vault_log" ":white_check_mark: Synced at $(timestamp_vault)"
>  else
>    log_master ":warning: [$vault_name] No changes to commit."
>    log_vault "$vault_log" ":warning: No changes to commit."
>  fi
>
>  log_master ""
>}
>
>#######################################
># Main Loop
>#######################################
>
>main() {
>  log_master "========= Obsidian Autosync Run: $(timestamp_master) ========="
>  for vault_path in "${VAULT_PATHS[@]}"; do
>    sync_vault "$vault_path"
>  done
>  log_master "========= End Run: $(timestamp_master) ========="
>  log_master ""
>}
>
>main
> ```

Specifically you need to tell it where your vaults are by giving it the file-path to your vault(s). Add it under the variable `VAULT_PATHS`

## Step 2: CronJob for Script Automation
Then add that script to your crontab (MacOS)
This is very easy. Just open a terminal, issue this command:
```bash
crontab -e
```

Then you'll see a text editor (vi) in your terminal:

![[Pasted image 20250610170510.png]]

Copy this to your clipboard
```crontab
0 0,6,12,18 * * * /bin/bash /Users/naderbaradar/obsidian_autosync.sh
```

Then go back to the terminal and press `i` on your keyboard to enter "Insert" mode and paste the line:
![[Pasted image 20250610170710.png]]

Finally, press `:` (colon) to enter "Command" mode and then type in `wq`

![[Pasted image 20250610170831.png]]

This will `w`rite to the file and `q`uit the text editor (vi). You have now scheduled your script to run automatically everyday at these times:
- 12:00 AM
- 06:00 AM
- 12:00 PM
- 06:00 PM

If you want to change the times/frequency you can play with the Crontab line.

Finally, you can validate that crontab registered your cronjob automation by issuing the `crontab -l` command, and you should see your cron job listed.
```
naderbaradar@Naders-MacBook-Air development_workspace % crontab -l

0 0,6,12,18 * * * /bin/bash /Users/naderbaradar/obsidian_autosync.sh
```

> [!tip] IMPORTANT
> For crontab to work you may need to give it full disk access (depending on where your obsidian vault is stored. Mine is stored in my iCloud directory)
>#### Steps:
>1. Open **System Settings**
>2. Go to **Privacy & Security → Full Disk Access**
>3. Click the **`+`** button
>4. Press `Cmd + Shift + G` and enter:
   `/usr/sbin/cron`


