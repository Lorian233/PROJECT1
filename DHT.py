import RPi.GPIO as GPIO
import time
#set up GPIO
GPIO.setmode(GPIO.BCM)
#Define GPIO pins for the ultrasonic sensor
TRIG =23 #pin connected to TRIG
ECHO =24 #pin connected to ECHO

#set up the GPIO pins
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def measure_distance():
    #ensure the trigger pin is set low
    GPIO.output(TRIG,false)
    time.sleep(2)#give sensor time to settle

    #send a 10us pulse to trigger
    GPIO.output(TRIG,True)
    time.sleep(o.00001)
    GPIO.output(TRIG,false)

    #wait for the echo to start
    while GPIO.input(ECHO)==0:
        pulse_start = time()

    #wait for the echo to end
     while GPIO.input(ECHO) ==1:
        pulse_end =time.time()

    #calculate pulse duration
    pulse_duration=pulse_end-pulse_start

    #calculate the distance 
    distanc=pulse_duration * 33000 /2 
    return distance    

try:
    while true:
        distance =measure_distance()
        print f"Distance :{distance:>2f} cm
        time.sleep(1)    