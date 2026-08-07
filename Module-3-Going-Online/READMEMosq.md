# Module 3: Connecting to the Lab Network 🛰️📡

It is time to put the "Network" into our Internet of Things (IoT) project! We are going to connect our Pico W to the lab Wi-Fi and teach it how to send sensor data directly to our local **Mosquitto MQTT Broker** on the Teacher PC. We will also add our final sensors!

---

## 🛠️ Hardware You Need

* **1x Raspberry Pi Pico W**
* **1x DHT22 Sensor** (Temperature & Humidity)
* **1x PIR Sensor** (Motion Detector for security/pest control!)
* *(Don't forget to keep your LED and Light Sensor plugged in from Modules 1 & 2!)*

---

## 🔌 Wiring Guide

* **DHT22:** Connect the data pin to **GP14**.
* **PIR Motion:** Connect the data pin to **GP13**.

---

## ⚙️ Step 1: Set Up Your Settings File

Before connecting, your Pico W needs to know where to find the Wi-Fi network and the Teacher PC!

1. Open the `settings.toml` file on your Pico W using Thonny.
2. Enter your Wi-Fi name (`CIRCUITPY_WIFI_SSID`) and password (`CIRCUITPY_WIFI_PASSWORD`).
3. Add the **Teacher PC IP Address** (written on the whiteboard!) under `MQTT_BROKER_IP`:
   ```toml
   MQTT_BROKER_IP = "192.168.1.100"  # Example IP address
