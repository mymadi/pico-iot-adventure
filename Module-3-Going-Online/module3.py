# 🚀 MISSION 3: SENDING DATA TO SPACE (THE CLOUD!) 🚀
import time, board, digitalio, analogio, os, wifi, socketpool, adafruit_dht
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT

# 🛑 ======================================================== 🛑
# 🛑        ENGINE ROOM: DO NOT TOUCH THE WIRES BELOW!        🛑
# 🛑 ======================================================== 🛑

# 1. Plugging in the robot's eyes and skin...
dht_device = adafruit_dht.DHT22(board.GP14)
pir_sensor = digitalio.DigitalInOut(board.GP13)
pir_sensor.direction = digitalio.Direction.INPUT
ldr = analogio.AnalogIn(board.GP26)

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
io.connect()


# 🎮 ======================================================== 🎮
# 🎮               HACKER ZONE: SAFE TO EDIT!                 🎮
# 🎮 ======================================================== 🎮

# ⏱️ How many seconds should the Pico wait before sending data?
# Try changing this to 15 or 5!
SEND_INTERVAL = 10  

# 📁 The name of your folder on Adafruit IO (Group Name)
GROUP_NAME = "iot-adventure"

last_send_time = 0

while True:
    try:
        io.loop() # This keeps the internet connection alive!
        
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
            light_level = ldr.value

            # 🖨️ 2. PRINT TO THE SCREEN 
            # (Hacker Mission: Change the fun words inside the quotes "")
            print("\n--- 🕵️‍♂️ SECRET AGENT DASHBOARD ---")
            
            if temperature is not None:
                print(f"🌡️ Temperature is: {temperature} C")
                print(f"💧 Humidity is: {humidity} %")
            
            print(f"☀️ Light Power: {light_level}")
            
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
