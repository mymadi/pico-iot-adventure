# Module 1: Hello Brain! 🧠💡

Welcome to your first IoT mission! Today, we are going to wake up the "brain" of our project—the Raspberry Pi Pico W—and teach it how to control the physical world. 

Whether you are building a **Smart Bedroom** (Smart Nightlight) or a **Mini Smart Farm** (Grow Light), everything starts with turning on a single light.

## 🛠️ Hardware You Need
* 1x Raspberry Pi Pico W
* 1x Breadboard
* 1x LED (Any color!)
* 1x Resistor (To protect our LED from burning out)
* Jumper Wires

## 🔌 Wiring Guide
1. Connect **GP15** on the Pico W to the **long leg** of the LED (use the resistor!).
2. Connect **GND** (Ground) on the Pico W to the **short leg** of the LED.

## 💻 Your Mission
1. Open the `code.py` file in this folder.
2. Copy the code and paste it into **Thonny**.
3. Scroll past the **🛑 Engine Room** (no touching the wires in there!) and find the **🎮 Hacker Zone**.
4. Click **Run** (the green play button) and watch your hardware come to life!

## 🚀 The Hacker Challenge
Right now, your light turns on for 1 second and off for 1 second. Can you change the `TIME_ON` and `TIME_OFF` numbers in the Hacker Zone to make it blink differently?

* **Strobe Light:** Try making both numbers `0.1` to create a super-fast strobe light!
* **Heartbeat:** Try making `TIME_ON = 3` and `TIME_OFF = 0.2` to make it stay on long, but turn off for just a quick blip!
