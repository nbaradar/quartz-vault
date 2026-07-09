---
title: Omarchy Mac Windows Install
tags:
  - omarchy
  - linux
  - vmware
  - lab
  - arch
  - windows
draft:
created: 2025-10-22

modified: 2025-10-24
published: 2025-10-22

---
>[!hint] See [[Omarchy Mac VM Install]] for MacOS instructions

I'm going to install using the [vanilla Arch ISO](https://archlinux.org/download/), and then following [steps in this guide](https://learn.omacom.io/2/the-omarchy-manual/96/manual-installation)

---
So in VMWare Workstation:
1. File -> New Virtual Machine
2. Select "Typical (recommended)" for configs
3. Installer Disk Image File (ISO) -> Select your arch ISO
4. For version, the site says "Included Kernel 6.16.8" so select "Other Linux 6.x kernel 64 bit". 
5. Set name and location. 
	1. I set name to `Arch-Omarchy-VM`
	2. I set location to `C:\Users\nader\Development\Virtual Machines`
6. I set Disk Size to 40GB and stored it as a SINGLE FILE

Additionally, before I started the VM i went into the VM settings and gave the VM 
- 8 gigs of RAM
- Added new Hard Disk: NVMe, that uses the old hard disk location at
	- `C:\Users\nader\Development\Virtual Machines\Arch-Omarchy-VM.vmdk`
- Enabled Accelerated Graphics under "Display" and set GPU memory to max (8gb for me)
- Go to "Options" tab, then under "Advnaced" look for "Firmware Type" and switch to UEFI. MAKE SURE TO TURN OFF "Enable Secure Boot" as Arch ISO won't boot with Secure Boot enabled. 

---

Now you can finally boot the system. Don't be confused that you're booted into zsh, as this is expected since we are booting into a live environment. Read the [pre-installation configs docs here](https://wiki.archlinux.org/title/Installation_guide#Boot_the_live_environment) 

You can double check that your internet is working with a quick ping command:
```bash
ping ping.archlinux.org
```

Once you are satisfied, go ahead and run the [following command](https://wiki.archlinux.org/title/Archinstall):
```bash
archinstall
```

> [!bug] if you are noticing an issue with input handling
> `archinstall` uses a TUI (Text User Interface) that has a known quirk with VMWare. 
> 
> In shell, VMWare passes raw key events, but in TUI it switches from terminal to raw/alternate screen mode, which then means VMWare uses it's enhanced keyboard, which can sometimes inject ghost scancodes. 
> 
> To fix this, just disable the enhanced keyboard. Power off the VM -> Settings -> Options -> Advanced and set `Enhanced Virtual Keyboard` to OFF

