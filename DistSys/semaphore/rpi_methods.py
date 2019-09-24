import RPi.GPIO as GPIO
import time


RED_LED = False
GREEN_LED = True
YELLOW_LED = False

RED_PIN = 16
YELLOW_PIN = 20
GREEN_PIN = 21

LAMPS = [16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)


# def turn_on_red():
#     turn_on_led(RED_PIN)
#
#
# def turn_on_green():
#     turn_on_led(GREEN_PIN)
#
#
# def switch_lights():
#     turn_on_led(YELLOW_PIN)
#
#
# def turn_on_led(pin):
#     GPIO.output(pin, GPIO.HIGH)
#     time.sleep(1)
#     GPIO.output(pin, GPIO.LOW)
#
#
# def set_lights(green, yellow, red):
#     pass
def toggle_led(lamp):
    print("Toggling lamp #{}".format(lamp))
    lamp = LAMPS [lamp - 1]
    if GPIO.input(lamp) == 1:
        GPIO.output(lamp, GPIO.LOW)
    else:
        GPIO.output(lamp, GPIO.HIGH)


def get_lamp_status(lamp):
    pin = LAMPS[lamp - 1]
    return bool(GPIO.input(pin))

