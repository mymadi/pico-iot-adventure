# 🧠 Module 5: The Smart AI Brain (Autonomous Mode)

<img src="https://github.com/mymadi/pico-iot-adventure/blob/main/Module-5-The-Smart-AI-Brain/Building_Autonomous_Edge_AI_Systems.png?raw=true" width="800">

Welcome to your final mission! Until now, your Raspberry Pi Pico W has been a "puppet"—it just sends data to the cloud and waits for a human to click a button to move a motor or turn on a light. 

**Today, we cut the strings.** You are going to code an **"Expert System"** (a form of Edge AI). Your Pico W will now look at its sensor data, combine the information using Boolean Logic, and make its own decisions instantly—all while keeping your web dashboard updated in real-time!

---

## 🛠️ Hardware You Need

For the ultimate AI system, we need all hands on deck. Plug in everything!
* **1x Raspberry Pi Pico W**
* **1x DHT22 Sensor** (Temperature & Humidity)
* **1x PIR Sensor** (Motion Detector)
* **1x LDR Sensor** (Light Level)
* **1x LED + 220Ω Resistor**
* **1x SG90 Micro Servo Motor**

---

## 🔌 Master Wiring Guide

| Component | Pin on Pico W | Notes |
| :--- | :--- | :--- |
| **LED** | **GP15** | Use a resistor! Connect the short leg to GND. |
| **Servo Motor** | **GP16** | Orange/Yellow to GP16. Red to VBUS(5V). Brown to GND. |
| **DHT22** | **GP14** | Connect VCC to 3V3 and GND to GND. |
| **PIR Motion**| **GP13** | Connect VCC to VBUS(5V) and GND to GND. |
| **LDR Sensor**| **GP26** | Connect to the Analog pin. |

---

## ☁️ Step 1: Upgrade Your Cloud Storage

Your AI is going to need a place to broadcast its inner thoughts. Let's add a new feed to your Adafruit IO dashboard!

1. Log into [io.adafruit.com](https://io.adafruit.com) and go to your **`iot-adventure`** group.
2. Click **+ New Feed**.
3. Name this new feed exactly: **`ai-decision`**
4. *(Optional)* If you are building the Smart Farm, create one more feed named: **`sunshade`**

---

## 💻 Step 2: Code the AI Brain

1. Open `code.py` in **Thonny IDE**.
2. Copy and paste the provided Module 5 Python code.
3. Update the engine room with your Adafruit IO Username, Key, and Wi-Fi credentials.
4. **Click Run!** 
5. Watch the Thonny Shell at the bottom. You will see your AI booting up, reading the sensors, and printing its "thoughts" to the screen based on real-world conditions!
> **💡 Pro Tip:** We set the AI to send data to the cloud every **15 seconds** (`SEND_INTERVAL = 15`). This prevents Adafruit IO from temporarily blocking (throttling) your free account for sending too much data!

---

## 🖥️ Step 3: Launch the AI Control Center

Now let's visualize the AI's brain on a futuristic web dashboard with Two-Way Sync!

1. Open the `indexAI.html` file in your web browser (Chrome, Edge, or Safari).
2. Enter your Adafruit IO **Username** and **AIO Key** in the top boxes.
3. Leave the **Refresh Rate** at `5` seconds (or bump it to `10` if you experience lag).
4. Click **Connect**.
5. **Watch the magic happen!** As you cover the light sensor or trigger the motion detector, watch the 🧠 **Latest AI Decision** box update automatically. Notice how the Manual Override LED button automatically switches to Red when the AI turns the light on!

---

## 🎮 Step 4: The Hacker Zone (Calibrate Your AI)

AI models need to be "trained" or "calibrated" to work perfectly in their real-world environment. Scroll down to the `🎮 HACKER ZONE` in your `code.py` file to adjust the rules.

### 🎯 Mission 1: Tweak the Thresholds
Look for these two lines of code:
```python
DARK_THRESHOLD = 30.0   # If light percentage is below 30%, it is "Dark"
HOT_THRESHOLD = 28.0    # If temperature is above 28°C, it is "Hot"
```
* **Too sensitive?** If your AI thinks the room is dark when the sun is shining, try lowering the `DARK_THRESHOLD` to `15.0`.
* **Test it:** Cover the LDR with your hand to trigger the nightlight AI rule and watch the dashboard update!

### 🕵️‍♂️ Mission 2: Write a New Rule
Can you add an `elif` statement to make the AI do something silly or highly specific? 
* **Example:** If it is perfectly bright (`light_level > 80`) and no one is moving (`motion_detected == False`), make the AI broadcast: `"I am bored! Waiting for humans..."`
