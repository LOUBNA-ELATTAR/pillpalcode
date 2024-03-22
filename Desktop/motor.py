import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins = [7,11]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

while True :
    GPIO.output(7,1)
    for i in range (200):
        GPIO.output(11,1)
        time.sleep(0.0005)
        GPIO.output(11,0)
        time.sleep(0.0005)
GPIO.cleanup()