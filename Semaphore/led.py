import RPi.GPIO as GPIO
import time

RED = 21 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED,GPIO.OUT)

print ("LED on")

GPIO.output(RED,GPIO.HIGH)
time.sleep(2)

print ("LED off")

GPIO.output(RED,GPIO.LOW)
