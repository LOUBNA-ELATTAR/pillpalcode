import RPi.GPIO as GPIO
import time
import serial
# Import Raspberry Pi GPIO library
#from gpiozero import MotionSensor
#pir=MotionSensor(4)
ser = serial.Serial('/dev/ttyACM0',9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
while True:   
   #if GPIO.input(7) == GPIO.HIGH:
        #print("hello")
        #ser.write(b"1")
        #time.sleep(1)
        #while GPIO.input(37) == GPIO.LOW:
            #GPIO.output(15,1)
            #print("buzz")
        #GPIO.output(15,0)
    ser.write(b"1")
    time.sleep(1)