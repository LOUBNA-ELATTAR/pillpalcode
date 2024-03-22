import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(16, GPIO.OUT)
control_pins = [7,11,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]]
def move_motor(deg):
    y=int(deg*512/360)
    for i in range(y):
      for halfstep in range(8):
        for pin in range(4):
          GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)
        
while True :
    if GPIO.input(10) == GPIO.HIGH:
        move_motor(400)
        GPIO.output(16,0)
GPIO.cleanup()
