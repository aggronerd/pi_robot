__author__ = 'greg'

import setup
import RPi.GPIO as GPIO
from controllers.cli import Cli


print "Running"
controller = Cli()
controller.run()
print "Finished"

GPIO.cleanup()
