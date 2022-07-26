import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pinNumLED = 17
pinNumBTN = 18
GPIO.setup(pinNumLED, GPIO.OUT)
GPIO.setup(pinNumBTN, GPIO.IN)

while True:
    if (GPIO.input(pinNumBTN)):
        GPIO.output(pinNumLED, GPIO.HIGH)
    else:
        GPIO.output(pinNumLED, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(pinNumLED, GPIO.LOW)
        sleep(0.2)
