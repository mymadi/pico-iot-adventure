import board, analogio, pwmio, time
from adafruit_motor import servo

# 🛑 ======================================================== 🛑
# 🛑        ENGINE ROOM: DO NOT TOUCH THE WIRES BELOW!        🛑
# 🛑 ======================================================== 🛑

# 1. Plugging in the robot's eye (Light Sensor)
ldr = analogio.AnalogIn(board.GP26)

# 2. Plugging in the robot's arm (Servo Motor)
pwm = pwmio.PWMOut(board.GP16, duty_cycle=0, frequency=50)
my_servo = servo.Servo(pwm)

# Robot memory: Is the curtain open or closed right now?
is_open = False

print("🤖 Robot Awake! Waiting for light...")


# 🎮 ======================================================== 🎮
# 🎮               HACKER ZONE: SAFE TO EDIT!                 🎮
# 🎮 ======================================================== 🎮

# 🕵️‍♂️ HACKER MISSION: Find your perfect "Magic Number"!
# Use your flashlight and your hand to test the light sensor. 
# Change 50 to the best percentage for your room (0 to 100).
MAGIC_NUMBER = 50 

while True:
    
    # 1. Read the light sensor (Flipping the numbers and converting to percentage 0-100%)
    inverted_value = 65535 - ldr.value
    light_level = (inverted_value / 65535) * 100
    
    # We use :.1f to round it to 1 decimal place (e.g., 45.2%)
    print(f"☀️ Current Light Level is: {light_level:.1f}%")
     
    # 2. The Robot's Brain (If / Else Decision)
    if light_level > MAGIC_NUMBER and is_open == False:
        # BRIGHT LIGHT DETECTED!
        print("😎 It is bright! Opening the curtains...")
        my_servo.angle = 90  # 90 degrees is OPEN
        is_open = True       # The robot remembers it opened the curtain
        
    elif light_level <= MAGIC_NUMBER and is_open == True:
        # DARKNESS DETECTED!
        print("😴 It is dark! Closing the curtains...")
        my_servo.angle = 0   # 0 degrees is CLOSED
        is_open = False      # The robot remembers it closed the curtain

    # Wait 1 second before checking again so the robot doesn't get dizzy
    time.sleep(1)
