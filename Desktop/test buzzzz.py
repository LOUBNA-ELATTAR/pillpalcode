import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(35,GPIO.IN)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,1)
for j in range(60):
    if (GPIO.input(35)==GPIO.HIGH):
        GPIO.output(7,0)
        break
    elif j==40 :
        GPIO.output(7,0)
        email()
        break
    t.sleep(1) 
