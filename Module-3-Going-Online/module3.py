# 🚀 MISSION 3: SENDING & RECEIVING FROM SPACE (THE CLOUD!) 🚀
import time, board, digitalio, analogio, os, wifi, socketpool, adafruit_dht
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT

# 📁 The name of your folder on Adafruit IO (Group Name)
GROUP_NAME = "iot-adventure"

# 🛑 ======================================================== 🛑
# 🛑        ENGINE ROOM: DO NOT TOUCH THE WIRES BELOW!        🛑
# 🛑 ======================================================== 🛑

# 1. Plugging in the robot's eyes, skin, and NEW LED!
dht_device = adafruit_dht.DHT22(board.GP14)

pir_sensor = digitalio.DigitalInOut(board.GP13)
pir_sensor.direction = digitalio.Direction.INPUT

ldr = analogio.AnalogIn(board.GP26)

# ---> THIS IS OUR NEW LED <---
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

# 2. Connecting to the WiFi Network...
print("📡 Connecting to WiFi:", os.getenv("CIRCUITPY_WIFI_SSID"))
try:
    wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
    print("✅ WiFi Connected!")
except Exception as e:
    print("❌ WiFi Error:", e)

# 3. Connecting to the Adafruit IO Cloud...
pool = socketpool.SocketPool(wifi.radio)
mqtt_client = MQTT.MQTT(
    broker="io.adafruit.com", username=os.getenv("ADAFRUIT_AIO_USERNAME"),
    password=os.getenv("ADAFRUIT_AIO_KEY"), socket_pool=pool,
)
io = IO_MQTT(mqtt_client)

io.on_connect = lambda c: print("✅ Cloud Connected!")
io.on_disconnect = lambda c: print("❌ Cloud Disconnected!")

# ---> THIS FUNCTION LISTENS FOR THE WEBSITE BUTTON <---
def message_received(client, feed_id, payload):
    print(f"\n📩 MESSAGE FROM CLOUD: {payload}")
    if payload == "1":
        led.value = True
        print("💡 LED IS ON!")
    else:
        led.value = False
        print("🌑 LED IS OFF!")

io.on_message = message_received

# Connect to the cloud!
io.connect()

# Tell the Pico to LISTEN to the 'led' feed from the website!
io.subscribe(f"{GROUP_NAME}.led")


# 🎮 ======================================================== 🎮
# 🎮               HACKER ZONE: SAFE TO EDIT!                 🎮
# 🎮 ======================================================== 🎮

# ⏱️ How many seconds should the Pico wait before sending data?
SEND_INTERVAL = 10  
last_send_time = 0

while True:
    try:
        # This keeps the internet connection alive AND checks for incoming LED clicks!
        io.loop() 
        
        # Is it time to send a message? (Stopwatch check)
        if (time.monotonic() - last_send_time) > SEND_INTERVAL:
            
            # 🌡️ 1. READ THE SENSORS
            try:
                temperature = dht_device.temperature
                humidity = dht_device.humidity
            except:
                temperature = None
                humidity = None
            
            motion_detected = pir_sensor.value
            
            # 1. Convert raw light value to a percentage (0 - 100%)
            inverted_value = 65535 - ldr.value
            light_level = (inverted_value / 65535) * 100

            # 🖨️ 2. PRINT TO THE SCREEN 
            print("\n--- 🕵️‍♂️ SECRET AGENT DASHBOARD ---")
            
            if temperature is not None:
                print(f"🌡️ Temperature is: {temperature} C")
                print(f"💧 Humidity is: {humidity} %")
            
            # We use :.1f to round it to 1 decimal place (e.g., 45.2%)
            print(f"☀️ Light Power: {light_level:.1f}%")
            
            if motion_detected:
                print("🚨 Motion: INTRUDER DETECTED!!")
            else:
                print("✅ Motion: Coast is clear.")

            # ☁️ 3. SEND TO THE CLOUD
            if temperature is not None:
                io.publish(f"{GROUP_NAME}.temperature", temperature)
                io.publish(f"{GROUP_NAME}.humidity", humidity)
            
            io.publish(f"{GROUP_NAME}.light", light_level)
            io.publish(f"{GROUP_NAME}.motion", 1 if motion_detected else 0)

            print("🚀 WHOOSH! Data sent to the cloud!")
            
            # Reset the stopwatch
            last_send_time = time.monotonic()

    except Exception as e:
        print("Uh oh! Network bumped its toe. Retrying...", e)
        time.sleep(2)
