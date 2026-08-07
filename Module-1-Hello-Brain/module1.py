import board
import digitalio
import time

# 🛑 ======================================================== 🛑
# 🛑        ENGINE ROOM: DO NOT TOUCH THE WIRES BELOW!        🛑
# 🛑 ======================================================== 🛑

# 1. Plugging the smart light into the robot's brain
smart_light = digitalio.DigitalInOut(board.GP15)
smart_light.direction = digitalio.Direction.OUTPUT

print("🤖 Brain is awake! Starting the Smart Light...")


# 🎮 ======================================================== 🎮
# 🎮               HACKER ZONE: SAFE TO EDIT!                 🎮
# 🎮 ======================================================== 🎮

# ⏱️ HACKER MISSION: Change how fast the light blinks!
# Try changing these numbers to 0.5 (super fast!), 0.1 (strobe light!), or 3 (slow).
TIME_ON = 1
TIME_OFF = 1

while True:
    
    # 1. Turn the light ON
    smart_light.value = True
    print("💡 Light is ON!")
    
    # Wait while the light is on
    time.sleep(TIME_ON) 
    
    # 2. Turn the light OFF
    smart_light.value = False
    print("🌑 Light is OFF!")
    
    # Wait while the light is off
    time.sleep(TIME_OFF)
