import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
    blink_count = 0
    while True:
        GPIO.output(18, GPIO.HIGH)
        blink_count += 1
        print(f"Blink count: {blink_count}")
        time.sleep(1)  
        GPIO.output(18, GPIO.LOW)
        time.sleep(1) 

except KeyboardInterrupt:
    GPIO.cleanup()