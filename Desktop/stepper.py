import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
ControlPin =[7,11,13,15]
for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
def move_motor(d):
  y=int(d*512/360)
  seq= [ [1,0,0,0],
         [1,1,0,0],
         [0,1,0,0],
         [0,1,1,0],
         [0,0,1,0],
         [0,0,1,1],
         [0,0,0,1],
         [1,0,0,1] ]
  for i in range (y):
    for h in range(8):
     for p in range(4):
      GPIO.output(ControlPin[p],seq[h][p])
     time.sleep(0.001)
  GPIO.cleanup()
while True :
    move_motor(12)
    time.sleep(5)
    