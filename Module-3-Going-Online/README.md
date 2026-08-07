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

## 💻 Your Mission

1. Open the `settings.toml` file and enter your WiFi password and Adafruit IO keys. Save it to your Pico.
2. Ensure you have the following libraries inside your Pico's `lib` folder:
   * `adafruit_minimqtt`
   * `adafruit_io`
   * `adafruit_dht`
3. Run `code.py` and watch the bottom of Thonny. It will tell you when it successfully connects to the cloud!

---

## 🪄 The Magic of Adafruit IO (Auto-Creation)

You might be wondering: *"Do I need to create my data feeds on Adafruit IO first?"*

**The answer is NO!** 

Adafruit IO is very smart. When your Pico runs its code and shouts, *"Here is the temperature!"*, Adafruit IO automatically creates a new feed called `temperature` to catch it. It will do this for your humidity, light, and motion sensors automatically!

---

## 🚀 The Hacker Challenge: Check Your Live Data!

Even though the feeds are created automatically, a good engineer always verifies their data. Can you see your temperature and light data updating in real-time? 

Here is how to check:

1. Open your web browser and log into [io.adafruit.com](https://io.adafruit.com).
2. Click on **Feeds** in the top menu bar.
3. **Behold!** You should see your new feeds listed there (like `temperature`, `humidity`, and `light`).
4. Click on the **temperature** feed. You will see a line graph! 
5. **Test it out:** Try breathing warm air on the DHT22 sensor or covering your light sensor. Watch the graph on your computer screen jump in real-time!
