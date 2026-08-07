# Module 3: Going Online 🌍📡

It is time to put the "Internet" into our Internet of Things (IoT) project! We are going to connect our Pico W to the WiFi and teach it how to send sensor data to the cloud using Adafruit IO. We will also add our final sensors!

---

## 🛠️ Hardware You Need

* **1x Raspberry Pi Pico W**
* **1x DHT22 Sensor** (Temperature & Humidity)
* **1x PIR Sensor** (Motion Detector for security/pest control!)

---

## 🔌 Wiring Guide

* **DHT22:** Connect the data pin to **GP14**.
* **PIR Motion:** Connect the data pin to **GP13**.

---

## ☁️ Step 1: Create a Cloud Folder (Group)

Before we send data, we need to set up a folder (called a **Group**) in Adafruit IO to keep all our project data organized!

1. Open your web browser and log into [io.adafruit.com](https://io.adafruit.com).
2. On the top menu, click **Feeds**, then select **View Groups** from the drop-down.
3. Click the **+ New Group** button.
4. Name your group exactly: **`iot-adventure`** and click Create.
5. Click on your newly created group.
6. Inside the group, click **+ New Feed** to create your individual sensor feeds. You will need to make four feeds:
   * `temperature`
   * `humidity`
   * `light`
   * `motion`

---

## 💻 Step 2: Connect the Engine

1. Open the `settings.toml` file and enter your WiFi password and Adafruit IO keys. Save it to your Pico.
2. Ensure you have the following libraries inside your Pico's `lib` folder:
   * `adafruit_minimqtt`
   * `adafruit_io`
   * `adafruit_dht`
3. Open `code.py` in Thonny. 
4. **Notice the red Stop Signs 🛑!** Do not touch the code at the top. That is the engine room that connects us to the WiFi. 
5. Click **Run** and watch the bottom of Thonny. It will tell you when it successfully connects to the cloud!

---

## 🎮 Step 3: The Hacker Zone (Code Modding!)

Now that your Pico is online, let's have some fun! Scroll down in your `code.py` file until you see the game controllers `🎮 HACKER ZONE`. 

Try these two Hacker Missions:
1. **Speed it up!** Find `SEND_INTERVAL = 10`. This is a stopwatch that waits 10 seconds. Change it to `5` and run the code again. Watch how much faster the data flies!
2. **Change the text!** Find the print messages like `"🚨 Motion: INTRUDER DETECTED!!"`. Can you change it to say `"🚨 A MONSTER IS HERE!!"` or something silly?

---

## 🚀 Step 4: Check Your Live Data!

A good engineer always verifies that their data made it to space (the cloud). Let's check!

1. Go back to your **`iot-adventure`** Group on the Adafruit IO website.
2. Click on the **temperature** feed. You will see a line graph! 
3. **Test it out:** Try breathing warm air on the DHT22 sensor or covering your light sensor. Watch the graph on your computer screen jump in real-time as your Pico sends the data!
