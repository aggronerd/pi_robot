__author__ = 'greg'

import time, RPi.GPIO as GPIO
import actuators

print "Running"
actuators.left_motor.forwards()
actuators.right_motor.forwards()

time.sleep(1)

actuators.left_motor.stop()
actuators.right_motor.stop()
print "Finished"

GPIO.cleanup()