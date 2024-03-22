import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins = [7,11]
for pin in control_pins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin,0)
GPIO.output(control_pins[0],1)
for i in range(812):
    GPIO.output(control_pins[1], 1)
    time.sleep(0.0005)
    GPIO.output(control_pins[1], 0)
    time.sleep(0.0005)
time.sleep(1)
GPIO.output(control_pins[0],0)
for i in range(812):
    GPIO.output(control_pins[1], 1)
    time.sleep(0.0005)
    GPIO.output(control_pins[1], 0)
    time.sleep(0.0005)
GPIO.cleanup()

 