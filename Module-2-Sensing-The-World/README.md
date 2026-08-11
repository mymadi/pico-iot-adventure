# Module 2: Sensing the World ☀️🤖

<img src="https://github.com/mymadi/pico-iot-adventure/blob/main/Module-2-Sensing-The-World/Light-Triggered_Motion_Electronics_Project.png?raw=true" width="800">
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
* **Servo:** Connect the orange (signal) wire to **GP16**, red to 3.3V or **VBUS** (5V), and brown to **GND**.

## 💻 Your Mission
1. Make sure your Pico has the `adafruit_motor` folder in its `lib` drive.
2. Open the `code.py` file from this folder in Thonny.
3. Scroll past the **🛑 Engine Room** (don't touch the wires in there!) and find the **🎮 Hacker Zone**.
4. Test your sensor by covering the LDR with your hand or shining a flashlight on it to watch the motor move!

## 🚀 The Hacker Challenge
Right now, the robot decides it is "daytime" based on the `MAGIC_NUMBER`. Can you figure out the perfect `MAGIC_NUMBER` for your specific room? 

* **Hint 1:** Look at the bottom of Thonny to see the numbers changing in real-time. Cover the sensor with your hand to see what the "dark" numbers are, then shine a light on it to see the "bright" numbers!
* **Hint 2:** Change the `MAGIC_NUMBER` in your code so the servo *only* moves when you shine a bright flashlight directly on it.
