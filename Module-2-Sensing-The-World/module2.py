import board
import digitalio
import analogio
import pwmio
from adafruit_motor import servo
import time

# --------------------------------------------------
# STEP 1: SET UP THE HARDWARE
# --------------------------------------------------

# 1. Set up the LDR Light Sensor on Analog Pin GP26
ldr = analogio.AnalogIn(board.GP26)

# 2. Set up the SG90 Servo Motor on PWM Pin GP16
pwm = pwmio.PWMOut(board.GP16, duty_cycle=0, frequency=50)
my_servo = servo.Servo(pwm)

# Create a variable to keep track of curtain/shade state
is_open = False

print("Module 2 System Ready! Monitoring Light Levels...")

# --------------------------------------------------
# STEP 2: THE MAIN LOOP
# --------------------------------------------------
while True:
    # Read raw light value (range is 0 to 65535)
    light_level = 65535 - ldr.value
    print("Current Light Level:", light_level)
    
    # --------------------------------------------------
    # STEP 3: IF / ELSE DECISION MAKING
    # --------------------------------------------------
    # HACKER CHALLENGE: Adjust this threshold number (30000)
    # based on how bright your room is!
    
    if light_level > 30000 and not is_open:
        # BRIGHT LIGHT DETECTED!
        # Bedroom: Open curtains / Farm: Deploy sunshade
        print("--> Bright light detected! Moving Servo to OPEN position (90°)...")
        my_servo.angle = 90
        is_open = True
        
    elif light_level <= 30000 and is_open:
        # DARKNESS DETECTED!
        # Bedroom: Close curtains / Farm: Retract sunshade
        print("--> It's dark! Moving Servo to CLOSED position (0°)...")
        my_servo.angle = 0
        is_open = False

    # Pause briefly before reading the light sensor again
    time.sleep(1)
