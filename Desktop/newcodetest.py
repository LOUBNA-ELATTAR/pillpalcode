import RPi.GPIO as GPIO
from gpiozero import AngularServo



servo = AngularServo(7, min_pulse_width=0.0006, max_pulse_width=0.0023)
# big servo ;servo =AngularServo(18, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
servo.angle= 170





