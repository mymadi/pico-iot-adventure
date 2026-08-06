import board
import digitalio
import time

# --------------------------------------------------
# STEP 1: SET UP THE HARDWARE
# --------------------------------------------------
# We are telling the Brain that an LED is plugged into Pin GP15
smart_light = digitalio.DigitalInOut(board.GP15)
smart_light.direction = digitalio.Direction.OUTPUT

print("Brain is awake! Starting the Smart Light...")

# --------------------------------------------------
# STEP 2: THE MAIN LOOP (The Brain keeps doing this forever)
# --------------------------------------------------
while True:
    
    # Turn the light ON
    smart_light.value = True
    print("Light is ON!")
    
    # Wait for a few seconds 
    # HACKER CHALLENGE: Change the number 1 to 0.5 or 3!
    time.sleep(1) 
    
    # Turn the light OFF
    smart_light.value = False
    print("Light is OFF!")
    
    # Wait again before repeating
    # HACKER CHALLENGE: Change this number too!
    time.sleep(1)
