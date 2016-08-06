from .base import Command
import RPi.GPIO as GPIO


class Read(Command):
    def _execute(self, args):
        pin = int(args[0])
        GPIO.setup(pin, GPIO.IN)
        val = GPIO.input(pin)
        if val:
            return 'High'
        else:
            return 'Low'

    def name(self):
        return 'read'


class Write(Command):
    def _execute(self, args):
        pin = int(args[0])
        val = int(args[1]) == 1
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, val)

    def name(self):
        return 'write'
