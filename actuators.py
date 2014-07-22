__author__ = 'greg'

import RPi.GPIO as GPIO

GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


class Motor(object):

    FORWARDS = 1
    BACKWARDS = 2
    OFF = 3

    def __init__(self, forwards_pin, backwards_pin):
        self._state = Motor.OFF
        """
        :type int
        """
        self._forwards_pin = forwards_pin
        self._backwards_pin = backwards_pin

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self.update_state()
        self._state = value

    def update_state(self):
        GPIO.out(self._forwards_pin, self._state == Motor.FORWARDS)
        GPIO.out(self._backwards_pin, self._state == Motor.BACKWARDS)

    def forwards(self):
        self.state = Motor.FORWARDS

    def backwards(self):
        self.state = Motor.BACKWARDS

    def stop(self):
        self.state = Motor.OFF


left_motor = Motor(19, 21)
right_motor = Motor(24, 26)