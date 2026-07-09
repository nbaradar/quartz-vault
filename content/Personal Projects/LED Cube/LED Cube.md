---
title: LED Cube
tags:
  - project
  - diy
  - arduino
draft: true
created: 2026-02-23

modified: 2026-06-14

published: 2026-02-23

---
[1000pcs F5 5mm Round White Clear Led Super Bright Ligte Emitting Diodes 6000-6500k Lamp Bulb](https://www.aliexpress.us/item/3256806931796890.html?spm=a2g0o.order_list.order_list_main.53.4b7b1802aY1G3X&gatewayAdapt=glo2usa#nav-specification)
![[S5f45ffb3030c483e9a1244d7c4a1ab0c7.pdf]]

White 
voltage = ~3.2-3.4
luminance (mcd) = 12000-14000
wave band (nm, k) = 6000~6500k

What is the actual current we can run through these LEDs? 80mW is lower power dissipation, let's check. 

According to Ohms law, P = V x I 
P = Power (watts)
V = Voltage (volts)
I = Current (amps)

## Resistor?
Because power max is **80mW**, that actually limits you:

At 3.4V:
I = P/V 
I = 0.08W / 3.4V = 23.5mA

So even though it says 30mA max, **23mA is the real thermal limit** if you don’t want to shorten lifespan.

So this means we should run 23mA max if we want to play it safe. LEDs cube usually run 10-15ma anyway

For the resistors
Voltage across resistor:
5−3.4=1.6V5 - 3.4 = 1.6V5−3.4=1.6V
### 🎯 10mA (safe, cube-friendly)
R=1.6/0.01=160ΩR = 1.6 / 0.01 = 160ΩR=1.6/0.01=160Ω
Use **180Ω** (standard value)
### 🎯 15mA (bright, still safe)
R=1.6/0.015=106ΩR = 1.6 / 0.015 = 106ΩR=1.6/0.015=106Ω
Use **120Ω** (safer than 110Ω)
### 🎯 20mA (near practical max)
R=1.6/0.02=80ΩR = 1.6 / 0.02 = 80ΩR=1.6/0.02=80Ω
Use **82Ω**

with 180ohm:
![[Pasted image 20260219200156.png]]

Running at:
- 10mA → bright
- 15mA → very bright
- 20mA → very bright, shorter lifespan
- 30mA → pushing it

# Why are we choosing 8–12mA instead of 20–30mA?

### The 74HC595 is the bottleneck.
Each output pin of a 74HC595:
- Is happiest at around **6–8mA**
- Can technically go higher
- But total chip current is limited

If you try to run 20mA per LED:
- Voltage droops
- Chip heats up
- Brightness becomes uneven
- Things behave weirdly

> We are intentionally choosing lower current because of the shift register.

---
## 🔧 Tools
- **Fanttik T1 Max Soldering Iron Kit**
- **Fanttik L1 Pro Cordless Screwdriver**
- **RA Flux Solder (.025")**
## 🧠 Logic Components
- **30× SN74HC595 Shift Registers**
- **200× 2N3904 NPN Transistors**
## ⚡ Passive Components
- **605-piece 1% metal film resistor kit**
- **Electrolytic capacitor assortment**

---
# The Build
First of all, you shuold really create a jig to hold the LEDs in place. For my first prototype cube I'm going to use foam, but I'm telling you from personal experience foam is NOT the optimal choice. I will create a 3d printed rig once I get to the final build. 
![[Pasted image 20260223111236.png]]

You want to bend the cathodes in the same direction and have each row connect all cathodes together. 

Then you'll want to connect each row of cathodes to a single rail, like so
![[Pasted image 20260223111429.png]]

After you finish with your first layer you should have something like this. 1 cathode end with 25 anode ends. Each layer will have 1 cathode lead. 
![[Pasted image 20260223111106.png]

---
# Misc
I bought some cool looking LED bulbs called "Edison bulbs" and I want to try making something cool with them. Don't know what yet. 
![[IMG_9034.mov]]