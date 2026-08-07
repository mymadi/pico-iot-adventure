import time
import board
import digitalio
import analogio
import pwmio
from adafruit_motor import servo
import adafruit_dht

# ==========================================
# 🛑 ENGINE ROOM - DO NOT TOUCH! 🛑
# ==========================================
# 1. Setup LED (Actuator)
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

# 2. Setup Servo Motor (Actuator)
pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)
motor = servo.Servo(pwm)

# 3. Setup LDR Light Sensor (Sensor)
light_sensor = analogio.AnalogIn(board.GP26)

# 4. Setup PIR Motion Sensor (Sensor)
pir_sensor = digitalio.DigitalInOut(board.GP13)
pir_sensor.direction = digitalio.Direction.INPUT

# 5. Setup DHT22 Temp/Humidity (Sensor)
dht_sensor = adafruit_dht.DHT22(board.GP14)

def get_light_level():
    # INVERTED MATH: Since the LDR gives a high number in the dark, 
    # we subtract it from the max (65535) so that 100% = Bright and 0% = Dark
    inverted_value = 65535 - light_sensor.value
    return (inverted_value / 65535) * 100

print("🧠 AI Brain Booting Up...")
time.sleep(2)

# ==========================================
# 🎮 HACKER ZONE: THE AI LOGIC! 🎮
# ==========================================
# Change these thresholds to match your room!
DARK_THRESHOLD = 30.0   # If light percentage is below 30%, it is "Dark"
HOT_THRESHOLD = 28.0    # If temperature is above 28°C, it is "Hot"

while True:
    try:
        # Step 1: The AI gathers data about the world
        light_level = get_light_level()
        motion_detected = pir_sensor.value
        temperature = dht_sensor.temperature
        
        print(f"👀 AI Sees -> Light: {light_level:.1f}% | Motion: {motion_detected} | Temp: {temperature}°C")

        # Step 2: The AI makes autonomous decisions!
        
        # 🛏️ SCENARIO A: The Smart Bedroom (Nightlight)
        # RULE: If it is DARK *AND* someone is MOVING, turn on the lights!
        if (light_level < DARK_THRESHOLD) and (motion_detected == True):
            print("🤖 AI Conclusion: Human walking in the dark! Turning LED ON.")
            led.value = True
        else:
            led.value = False

        # 🌾 SCENARIO B: The Smart Farm (Sunshade)
        # RULE: If it is HOT *AND* the sun is BRIGHT, deploy the sunshade!
        if (temperature > HOT_THRESHOLD) and (light_level > DARK_THRESHOLD):
            print("🤖 AI Conclusion: Crops are too hot! Deploying Sunshade.")
            motor.angle = 180  # Move motor to deploy shade
        else:
            motor.angle = 0    # Retract shade
            
    except RuntimeError as e:
        # Sometimes the DHT22 misreads, the AI just ignores it and tries again
        print("Sensor reading error, trying again...")
        
    time.sleep(2) # The AI rests for 2 seconds before checking again
