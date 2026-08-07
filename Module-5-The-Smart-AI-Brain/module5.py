import time, board, digitalio, analogio, pwmio, os, wifi, socketpool, adafruit_dht
from adafruit_motor import servo
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT

# 📁 The name of your folder on Adafruit IO (Group Name)
GROUP_NAME = "iot-adventure"

# ==========================================
# 🛑 ENGINE ROOM - DO NOT TOUCH! 🛑
# ==========================================
# 1. Setup LED & Servo Motor (Actuators)
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)
motor = servo.Servo(pwm)

# 2. Setup Sensors
light_sensor = analogio.AnalogIn(board.GP26)
pir_sensor = digitalio.DigitalInOut(board.GP13)
pir_sensor.direction = digitalio.Direction.INPUT
dht_sensor = adafruit_dht.DHT22(board.GP14)

def get_light_level():
    inverted_value = 65535 - light_sensor.value
    return (inverted_value / 65535) * 100

# 3. Connecting to the WiFi Network...
print("📡 Connecting to WiFi:", os.getenv("CIRCUITPY_WIFI_SSID"))
try:
    wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
    print("✅ WiFi Connected!")
except Exception as e:
    print("❌ WiFi Error:", e)

# 4. Connecting to the Adafruit IO Cloud...
pool = socketpool.SocketPool(wifi.radio)
mqtt_client = MQTT.MQTT(
    broker="io.adafruit.com", username=os.getenv("ADAFRUIT_AIO_USERNAME"),
    password=os.getenv("ADAFRUIT_AIO_KEY"), socket_pool=pool,
)
io = IO_MQTT(mqtt_client)
io.connect()
print("✅ Cloud Connected! 🧠 AI Brain Booting Up...")
time.sleep(2)

# ==========================================
# 🎮 HACKER ZONE: THE AI LOGIC! 🎮
# ==========================================
# Change these thresholds to match your room!
DARK_THRESHOLD = 30.0   # If light percentage is below 30%, it is "Dark"
HOT_THRESHOLD = 28.0    # If temperature is above 28°C, it is "Hot"

SEND_INTERVAL = 10       # Send data to dashboard every 10 seconds
last_send_time = 0

while True:
    try:
        io.loop() # Keeps the internet connection alive
        
        if (time.monotonic() - last_send_time) > SEND_INTERVAL:
            # Step 1: The AI gathers data about the world
            light_level = get_light_level()
            motion_detected = pir_sensor.value
            try:
                temperature = dht_sensor.temperature
                humidity = dht_sensor.humidity
            except:
                temperature = None
                humidity = None
            
            print(f"\n👀 AI Sees -> Light: {light_level:.1f}% | Motion: {motion_detected} | Temp: {temperature}°C")

            # Step 2: The AI makes autonomous decisions!
            ai_thought = "Analyzing environment..." # Default thought
            
            # 🛏️ SCENARIO A: The Smart Bedroom (Nightlight)
            if (light_level < DARK_THRESHOLD) and (motion_detected == True):
                print("🤖 AI Conclusion: Human walking in the dark! Turning LED ON.")
                led.value = True
                ai_thought = "Intruder in the dark! Lights ON."
            else:
                led.value = False

            # 🌾 SCENARIO B: The Smart Farm (Sunshade)
            if temperature is not None and (temperature > HOT_THRESHOLD) and (light_level > DARK_THRESHOLD):
                print("🤖 AI Conclusion: Crops are too hot! Deploying Sunshade.")
                motor.angle = 180  # Deploy shade
                if ai_thought == "Analyzing environment...":
                    ai_thought = "Too hot! Deploying Sunshade."
            else:
                motor.angle = 0    # Retract shade
                
            if led.value == False and motor.angle == 0:
                 ai_thought = "Environment is stable and safe."

            # Step 3: Broadcast the AI's thoughts to the Web Dashboard!
            print(f"📡 Sending to Dashboard: {ai_thought}")
            
            if temperature is not None:
                io.publish(f"{GROUP_NAME}.temperature", temperature)
                io.publish(f"{GROUP_NAME}.humidity", humidity)
                
            io.publish(f"{GROUP_NAME}.light", light_level)
            io.publish(f"{GROUP_NAME}.motion", 1 if motion_detected else 0)
            
            # ✨ Sending the special AI Decision text to the dashboard! ✨
            io.publish(f"{GROUP_NAME}.ai-decision", ai_thought)
            
            last_send_time = time.monotonic()
            
    except Exception as e:
        print("Uh oh! Network or Sensor bumped its toe. Retrying...", e)
        time.sleep(2)
