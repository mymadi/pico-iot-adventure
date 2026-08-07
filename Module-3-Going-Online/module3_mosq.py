# 🚀 MISSION 3: SENDING & RECEIVING FROM YOUR LOCAL LAB BROKER 🚀
import time, board, digitalio, analogio, os, wifi, socketpool, adafruit_dht
import adafruit_minimqtt.adafruit_minimqtt as MQTT

# 📁 Set the group name for this Pico (e.g., "group01", "group02", etc.)
GROUP_NAME = "group01"

# 🛑 ======================================================== 🛑
# 🛑        ENGINE ROOM: DO NOT TOUCH THE WIRES BELOW!        🛑
# 🛑 ======================================================== 🛑

# 1. Plugging in sensors and LED
dht_device = adafruit_dht.DHT22(board.GP14)

pir_sensor = digitalio.DigitalInOut(board.GP13)
pir_sensor.direction = digitalio.Direction.INPUT

ldr = analogio.AnalogIn(board.GP26)

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

# 2. Connecting to the WiFi Network
print("📡 Connecting to WiFi:", os.getenv("CIRCUITPY_WIFI_SSID"))
try:
    wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
    print("✅ WiFi Connected!")
except Exception as e:
    print("❌ WiFi Error:", e)

# 3. Callback Functions for Local MQTT
def connected(client, userdata, flags, rc):
    print("✅ Connected to Local Lab Broker!")
    # Subscribe to the LED topic for this group
    client.subscribe(f"{GROUP_NAME}/led")

def disconnected(client, userdata, rc):
    print("❌ Disconnected from Broker!")

def message_received(client, topic, message):
    print(f"\n📩 MESSAGE FROM BROKER [{topic}]: {message}")
    if message == "1":
        led.value = True
        print("💡 LED IS ON!")
    else:
        led.value = False
        print("🌑 LED IS OFF!")

# 4. Set up connection to Mosquitto Broker on Teacher's PC
pool = socketpool.SocketPool(wifi.radio)

# Read the PC IP address from settings.toml
broker_address = os.getenv("MQTT_BROKER_IP") 

mqtt_client = MQTT.MQTT(
    broker=broker_address,
    port=1883,
    socket_pool=pool,
    is_ssl=False
)

# Connect callback functions
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message_received

print(f"🔄 Connecting to Local Mosquitto at {broker_address}...")
mqtt_client.connect()


# 🎮 ======================================================== 🎮
# 🎮               HACKER ZONE: SAFE TO EDIT!                 🎮
# 🎮 ======================================================== 🎮

# ⏱️ How many seconds should the Pico wait before sending data?
SEND_INTERVAL = 10  
last_send_time = 0

while True:
    try:
        # Keeps connection alive and listens for LED commands
        mqtt_client.loop() 
        
        # Stopwatch check to send data
        if (time.monotonic() - last_send_time) > SEND_INTERVAL:
            
            # 🌡️ 1. READ THE SENSORS
            try:
                temperature = dht_device.temperature
                humidity = dht_device.humidity
            except:
                temperature = None
                humidity = None
            
            motion_detected = pir_sensor.value
            light_level = 65535 - ldr.value

            # 🖨️ 2. PRINT TO THE SCREEN 
            print(f"\n--- 🕵️‍♂️ SECRET AGENT DASHBOARD [{GROUP_NAME.upper()}] ---")
            
            if temperature is not None:
                print(f"🌡️ Temperature is: {temperature} C")
                print(f"💧 Humidity is: {humidity} %")
            
            print(f"☀️ Light Power: {light_level}")
            
            if motion_detected:
                print("🚨 Motion: INTRUDER DETECTED!!")
            else:
                print("✅ Motion: Coast is clear.")

            # ☁️ 3. SEND TO LOCAL MOSQUITTO BROKER
            if temperature is not None:
                mqtt_client.publish(f"{GROUP_NAME}/temperature", str(temperature))
                mqtt_client.publish(f"{GROUP_NAME}/humidity", str(humidity))
            
            mqtt_client.publish(f"{GROUP_NAME}/light", str(light_level))
            mqtt_client.publish(f"{GROUP_NAME}/motion", "1" if motion_detected else "0")

            print("🚀 WHOOSH! Data published locally!")
            
            last_send_time = time.monotonic()

    except Exception as e:
        print("Uh oh! Network bumped its toe. Retrying...", e)
        time.sleep(2)
