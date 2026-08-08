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
* **LDR Sensor:** Connect to **GP26**.
* **LED:** Connect to **GP15** (with a resistor).

---

## ⚙️ Step 1: Set Up Your Settings File

Before connecting, your Pico W needs to know where to find the Wi-Fi network and the Teacher PC!

1. Open the `settings.toml` file on your Pico W using Thonny.
2. Enter your Wi-Fi name (`CIRCUITPY_WIFI_SSID`) and password (`CIRCUITPY_WIFI_PASSWORD`).
3. Add the **Teacher PC IP Address** (written on the whiteboard!) under `MQTT_BROKER_IP`:
   ```toml
   CIRCUITPY_WIFI_SSID = "Lab-WiFi"
   CIRCUITPY_WIFI_PASSWORD = "LabPassword123"
   MQTT_BROKER_IP = "192.168.1.100"
   ```
4. Save the file to your Pico W.

---

## 💻 Step 2: Connect the Engine

1. Ensure you have the following libraries inside your Pico's `lib` folder:
   * `adafruit_minimqtt`
   * `adafruit_dht`
2. Open `code.py` in Thonny.
3. Near the top of the file, set your assigned group ID (e.g., `"group01"`, `"group02"`):
   ```python
   GROUP_NAME = "group01"
   ```
4. **Notice the red Stop Signs 🛑!** Do not touch the rest of the engine room code—that handles the Wi-Fi and MQTT connection!
5. Click **Run** (the green play button) and watch the shell at the bottom of Thonny. It will display a success message when connected to the local broker!

---

## 🎮 Step 3: The Hacker Zone (Code Modding!)

Now that your Pico is online, let's have some fun! Scroll down in your `code.py` file until you see the game controllers `🎮 HACKER ZONE`.

Try these two Hacker Missions:
1. **Speed it up!** Find `SEND_INTERVAL = 10`. This is a stopwatch that waits 10 seconds. Change it to `5` and run the code again. Watch how much faster your sensor updates send!
2. **Change the text!** Find the terminal output messages like `"🚨 Motion: INTRUDER DETECTED!!"`. Can you change it to say `"🚨 A MONSTER IS HERE!!"` or something silly?

---

## 🚀 Step 4: Verify Your Sensor Stream!

A good engineer always verifies that their data is broadcasting correctly across the network!

1. Look at the Thonny Shell output at the bottom of your screen.
2. **Test it out:** Try breathing warm air on the DHT22 sensor, waving your hand over the PIR motion detector, or covering the light sensor.
3. Confirm that you see the updated readings and the `🚀 WHOOSH! Data published locally!` message appear each time the stopwatch triggers!
