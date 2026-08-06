import time
import board
import digitalio
import analogio
import os
import wifi
import socketpool
import adafruit_dht
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT

# --------------------------------------------------
# STEP 1: SET UP SENSORS & HARDWARE
# --------------------------------------------------

# 1. DHT22 Temperature & Humidity Sensor on GP14
dht_device = adafruit_dht.DHT22(board.GP14)

# 2. PIR Motion Sensor on GP13
pir_sensor = digitalio.DigitalInOut(board.GP13)
pir_sensor.direction = digitalio.Direction.INPUT

# 3. LDR Light Sensor on GP26
ldr = analogio.AnalogIn(board.GP26)

# --------------------------------------------------
# STEP 2: CONNECT TO WIFI
# --------------------------------------------------
print("Connecting to WiFi network:", os.getenv("CIRCUITPY_WIFI_SSID"))
try:
    wifi.radio.connect(
        os.getenv("CIRCUITPY_WIFI_SSID"), 
        os.getenv("CIRCUITPY_WIFI_PASSWORD")
    )
    print("Connected to WiFi! IP:", wifi.radio.ipv4_address)
except Exception as e:
    print("Failed to connect to WiFi:", e)

# --------------------------------------------------
# STEP 3: CONNECT TO ADAFRUIT IO (MQTT)
# --------------------------------------------------
pool = socketpool.SocketPool(wifi.radio)

mqtt_client = MQTT.MQTT(
    broker="io.adafruit.com",
    username=os.getenv("ADAFRUIT_AIO_USERNAME"),
    password=os.getenv("ADAFRUIT_AIO_KEY"),
    socket_pool=pool,
)

# Create Adafruit IO MQTT Client
io = IO_MQTT(mqtt_client)

# Callback functions for MQTT connection
def connected(client):
    print("Successfully connected to Adafruit IO!")

def disconnected(client):
    print("Disconnected from Adafruit IO!")

io.on_connect = connected
io.on_disconnect = disconnected

print("Connecting to Adafruit IO Broker...")
io.connect()

# --------------------------------------------------
# STEP 4: MAIN TRANSMISSION LOOP
# --------------------------------------------------
last_send_time = 0
SEND_INTERVAL = 5  # Send data every 5 seconds to prevent overloading Adafruit IO

while True:
    try:
        # Keep MQTT connection alive
        io.loop()
        
        # Check if 5 seconds have passed
        if (time.monotonic() - last_send_time) > SEND_INTERVAL:
            
            # Read DHT22
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            
            # Read PIR & LDR
            motion_detected = pir_sensor.value
            light_level = ldr.value

            # Print to serial console for debugging
            print("\n--- Sensor Readings ---")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Light Level: {light_level}")
            print(f"Motion: {'YES!' if motion_detected else 'No'}")

            # Publish to Adafruit IO feeds
            if temperature is not None:
                io.publish("temperature", temperature)
            if humidity is not None:
                io.publish("humidity", humidity)
            
            io.publish("light", light_level)
            io.publish("motion", 1 if motion_detected else 0)

            print("--> Data successfully sent to the Cloud! 🚀")
            last_send_time = time.monotonic()

    except Exception as e:
        print("Sensor/Network error, retrying...", e)
        time.sleep(2)
