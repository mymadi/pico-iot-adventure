# Module 2: Sensing the World ☀️🤖

Now that our brain is awake, we need to give it "eyes" and "muscles"! In this module, we will use a light sensor (LDR) to detect the sun, and a Servo motor to create physical movement.

* **Smart Bedroom:** You will build Automated Curtains that open when the sun comes up!
* **Mini Smart Farm:** You will build an Automated Sunshade that deploys to protect plants from harsh light!

## 🛠️ Hardware You Need
* 1x Raspberry Pi Pico W & Breadboard
* 1x LDR (Light Dependent Resistor)
* 1x SG90 Micro Servo (The blue motor)
* Jumper Wires

## 🔌 Wiring Guide
* **LDR:** Connect to **GP26** (Analog pin to measure light levels).
* **Servo:** Connect the orange (signal) wire to **GP16**, red to **VBUS** (5V), and brown to **GND**.

## 💻 Your Mission
1. Make sure your Pico has the `adafruit_motor` folder in its `lib` drive.
2. Open the `code.py` file from this folder in Thonny.
3. Test your sensor by covering the LDR with your hand to watch the motor move!

## 🚀 The Hacker Challenge
Look at the `if / else` statement in the code. Can you change the light threshold number so the servo only moves when you shine a bright flashlight directly on it?
