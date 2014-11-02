__author__ = 'greg'

import setup
from controller import PiRobotJabberBot
import RPi.GPIO as GPIO
import logging

print "Running"

logging.basicConfig(level=logging.DEBUG)
username = 'keximbot@adastra.re'
password = '8_eow3#Ka33f3s'
bot = PiRobotJabberBot(username, password)
bot.serve_forever()

print "Finished"

GPIO.cleanup()