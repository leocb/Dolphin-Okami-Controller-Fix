# Dolphin-Okami-Controller-Fix
This repo has the files for fixing the loss of speed when playing okami (Wii) on dolphin using mouse and keyboard. The following is the tutorial, originally posted in the [Dolphin foruns](https://forums.dolphin-emu.org/Thread-okami-wii-solid-keyboard-mouse-controls-guide-windows)

---

**>>>>>>>>>> [Click here to download the files as a zip](https://github.com/leocb/Dolphin-Okami-Controller-Fix/archive/refs/heads/main.zip)**

---

## The Problem

After creating a ISO from my Okami disk, I started playing around with the various controls configurations dolphin offers, and after a while, I got some pretty solid controls working and could play Okami like a boss, however, if you ever tried playing Okami on the keyboard, you'll know that Amaterasu loses all her speed when changing directions on the nunchuck (from forward to forward+right, for example) and that almost makes the game unplayable, since some cut scenes require the player to run like hell!

So what gives? Why does she loses speed?
Okami has a weird implementation over "not losing speed when changing directions", winch require the player to smoothly transition from position to position on the nunchuck, something dolphin does not offer on the emulated wiimote (devs please? haha)
Dolphin's implementation simply "TAP" the analog in the direction you required, providing a fast feedback to the game, this is generally ok... but for okami, that's a big no no

here's an example (Sry for the FPS, normally it runs at the 30 fps cap):
- Without my fix: https://youtu.be/T61cL5UrLgg
- With the fix: https://youtu.be/RKhBKpNJ3a4

so we need something to smoothly transition the analog movement

## The solution

Fast forward some hours and I have the solution, since this uses vJoy it's only windows compatible, maybe there's something similar for other OSes but I dunno

- FreePie - this is the one responsible to get all our inputs on the keyboard and mice then calculate the appropriate analog sticks and wiimote IR behavior, as well as button presses and send it over to:
- vJoy - Simply an interface, it makes windows think there's a directInput device (a.k.a. joystick) connected to the system, when in reality its all virtual magic -> it gets all the input data and sends it over to:
- Dolphin - Here we map the buttons, analog stick and IR then configure each to provide a solid gaming experience in Okami

**TL;DR FreePie Simulates the required input behavior and send this data to vJoy winch feeds everything to Dolphin**

## How to

that's cool! So how do I do it myself?
Glad you asked!

### Step 1: Downloads

1. download and install FreePie v1.9.629: https://github.com/AndersMalmgren/FreePIE/releases/download/1.9.629/FreePIE.1.9.629.0.msi
2. download and install vJoy v2.1.6 (this is the vJoy version freePie supports in version 1.9.629.0): https://sourceforge.net/projects/vjoystick/files/Beta%202.x/2.1.6-081015/
3. open the vJoy configuration -> on the first virtual controller set the number of buttons to 12 -> hit apply -> restart your PC and comeback here
4. get the FreePie script file from this repo (`Okami FreePie.py`) and save it somewhere easy - Button mappings are down bellow, if you want to change them, you can do so in this script, also, change the `ScreenResX` and `ScreenResY` var on the top of the script to your dolphin **full screen resolution**, this corrects the mouse sensibility when using celestial brush.
5. get the Dolphin configuration file from this repo (`Okami vJoy.ini`) and copy it to `C:\Users\[YourWindowsUserName]\Documents\Dolphin Emulator\Config\Profiles\Wiimote`

### Step 2: Setup

1. Open dolphin, go to Controllers -> Wiimote1 [Emulated Wiimote] -> Configure -> Load the Okami vJoy profile
2. Load your Okami iso
3. Open FreePie and load the file `Okami FreePie.py` -> hit F5 to start executing it (Shift+F5 to stop)

## Play

That's it, now **hit the number `0`** on your keyboard to lock the mouse in position and start sending the inputs from FreePie to Dolphin, hit `0` again to stop and release the mouse

If you have suggestions or questions, open an issue!
Have fun!

### Button mappings

```
WASD - "Smooth" Nunchuck analog stick
Q - "-" Pause menu
E - "Z" most interactions and secondary weapon use
R - "+" Settings menu
F - "C" Bite/Dig
1 - "1" Quick Map
2 - "2" Camera perspective (hold for first person)
SPACE BAR - "A" Jump

LEFT MOUSE - "Wiimote Shake" - Attack/Dash or "A" to Draw while holding Right Mouse Button
RIGHT MOUSE - "B" hold for celestial brush

HOLD SHIFT and WASD to "DPad" control the camera, restricts movement, this behavior can be changed in the dolphin's controller settings
HOLD SHIFT and MOVE THE MOUSE around to "Shake the nunchuck in a direction" - Fleetfoot technique (the implementation of this on the wii is extremely unreliable, I'm amazed it is working so well here)
```

## Contributing

- Feel free to open a PR with new features or bug fixes
- Support this and more projects by donating:

[![Paypal](https://user-images.githubusercontent.com/8310271/225498353-9d0a672d-ed45-4fed-9838-11d71ee49c28.png)](https://www.paypal.com/donate/?hosted_button_id=683D7S6KLX7EA)
