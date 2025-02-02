import time
import freewili


#typedef enum _LEDManagerLEDMOde {}

# Find all Free Wili devices connected to the system
devices = freewili.find_all()

# Ensure there is at least one device connected
if not devices:
    print("No Free Wili devices found!")
    exit(1)

# Select the first device (index 0)
device = devices[1]

print(device.get_app_info())

# Initialize the LED state as True (on)
led_state = True

# Keep the device open for communication
device.stay_open = True

# Loop to toggle the LED 100 times
for _ in range(100):

    # Set the state of pin 25

    try:
        GPIO  = device.get_all_io()
        time.sleep(1)        
        if GPIO.is_ok(): 

            if (GPIO.unwrap() & (1 << 26)):
                
                state = "high"
                
                    #setBoardLED(7, 255, 0, 255, 5000, ledsimplevalue)
            else:
                state = "low"
            print(f"Pin 25 is {state}.")    
            # Toggle the LED state
            #led_state = not led_state
            # Wait for 0.1 seconds

    except:
        print("uhoh")
        #add holyshit later

print("LED toggle script completed.")
