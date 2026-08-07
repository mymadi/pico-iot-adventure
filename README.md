# 🚀 Pico IoT Adventure: Primary & Secondary School Course

[![Target Level](https://img.shields.io/badge/Level-Primary%20%26%20Secondary%20School-orange.svg)](#)
[![Platform](https://img.shields.io/badge/Board-Raspberry%20Pi%20Pico%20W-red.svg)](https://www.raspberrypi.com/products/raspberry-pi-pico/)
[![Language](https://img.shields.io/badge/Language-CircuitPython-blue.svg)](https://circuitpython.org/)
[![Broker](https://img.shields.io/badge/MQTT-Adafruit%20IO-black.svg)](https://io.adafruit.com/)

Welcome to the **Pico IoT Adventure** repository! Designed for both **primary and secondary school students**, this hands-on course guides learners through building a complete Internet of Things (IoT) system using the **Raspberry Pi Pico W**, **CircuitPython**, and the **Adafruit IO Cloud Service**.

![IoT Hardware to Cloud Journey](./IoT_Hardware_to_Cloud_Journey.png)

Students will learn to bridge physical electronic hardware with modern browser-based web dashboards using **Adafruit IO** and real-time **MQTT** messaging.

---

## 📺 Getting Started Video Tutorial

Need help setting up your workspace? Watch the step-by-step video guide below:

[![Watch the Getting Started Tutorial](https://img.youtube.com/vi/56N_8FI_WLU/maxresdefault.jpg)](https://www.youtube.com/watch?v=56N_8FI_WLU)

> 🎬 **[Click here to watch the setup guide on YouTube](https://www.youtube.com/watch?v=56N_8FI_WLU)**

---

## 🌟 Learning Themes

Students can choose between two fun real-world applications to build throughout the course:

* 🛏️ **Theme 1: The Smart Bedroom**
  * Automated ambient nightlight
  * Motorized morning sun curtains
  * Intruder security alarm
* 🌾 **Theme 2: The Mini Smart Farm**
  * Automated greenhouse grow light
  * Smart sunshade deployer
  * Crop security & environment monitor

---

## 🛠️ Required Hardware List

| Category | Component | Quantity |
| :--- | :--- | :--- |
| **Brain** | Raspberry Pi Pico W | 1 |
| **Sensors** | LDR Light Sensor<br>DHT22 Temp & Humidity Sensor<br>PIR Motion Sensor | 1 of each |
| **Actuators** | LED + 220Ω Resistor<br>SG90 Micro Servo Motor | 1 of each |
| **Accessories** | Breadboard, Jumper Wires, Micro-USB Cable, Craft Materials | 1 set |

---

## 📂 Course Modules

This course is structured into 4 sequential modules. Click any module link below to access its step-by-step guide and starter code:

| Module | Title | Hardware Covered | Key Concept |
| :--- | :--- | :--- | :--- |
| 🧠 **[Module 1](./Module-1-Hello-Brain)** | **Hello Brain!** | LED | Basic GPIO Outputs & Timing Loops |
| ☀️ **[Module 2](./Module-2-Sensing-The-World)** | **Sensing the World** | LDR, Servo Motor | Analog Inputs & Threshold Logic |
| 🛰️ **[Module 3](./Module-3-Going-Online)** | **Going Online** | DHT22, PIR Sensor, Wi-Fi | MQTT Publishing & Adafruit IO Cloud |
| 💻 **[Module 4](./Module-4-The-Website)** | **The Control Center** | HTML, Web Browser | Data Visualization & Web Remote Control |

---

## 🧰 Software Requirements

1. **[Thonny IDE](https://thonny.org/):** Beginner-friendly Python editor used to run code on the Pico W.
2. **[CircuitPython UF2](https://circuitpython.org/board/raspberry_pi_pico_w/):** Firmware installed on the Raspberry Pi Pico W.
3. **[Adafruit IO Account](https://io.adafruit.com/):** Free MQTT cloud service for storing and visualizing sensor data.

---

## 🚀 Quick Setup Instructions

> [!TIP]
> **Before Starting:** Make sure you have created a free account on [Adafruit IO](https://io.adafruit.com/) and noted down your **Username** and **AIO Key**!

1. Clone or download this repository to your computer.
2. Open **Thonny IDE** and select the interpreter: **CircuitPython (Generic)**.
3. Plug in your Raspberry Pi Pico W via Micro-USB.
4. Watch the [Getting Started Video](https://www.youtube.com/watch?v=56N_8FI_WLU) and dive into **[Module 1](./Module-1-Hello-Brain)**!
