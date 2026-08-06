# Module 3: Going Online 🌍📡

It is time to put the "Internet" into our Internet of Things (IoT) project! We are going to connect our Pico W to the WiFi and teach it how to send sensor data to the cloud using Adafruit IO. We will also add our final sensors!

## 🛠️ Hardware You Need
* 1x Raspberry Pi Pico W
* 1x DHT22 Sensor (Temperature & Humidity)
* 1x PIR Sensor (Motion Detector for security/pest control!)

## 🔌 Wiring Guide
* **DHT22:** Connect data pin to **GP14**.
* **PIR Motion:** Connect data pin to **GP13**.

## 💻 Your Mission
1. Open the `settings.toml` file and enter your WiFi password and Adafruit IO keys. Save it to your Pico.
2. Ensure you have the `adafruit_minimqtt`, `adafruit_io`, and `adafruit_dht` libraries in your `lib` folder.
3. Run `code.py` and watch the bottom of Thonny. It will tell you when it successfully connects to the cloud!

## 🚀 The Hacker Challenge
Log into the Adafruit IO dashboard. Can you see your temperature and light data updating in real-time? Try breathing warm air on the DHT22 to see the numbers jump!
