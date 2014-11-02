__author__ = 'greg'

import RPi.GPIO as GPIO
from threading import Thread
import time
import logging

GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

logger = logging.getLogger(__name__)


class MotorPulseThread(Thread):

    def __init__(self, motor, duration_seconds, pause_seconds, motor_state):
        super(MotorPulseThread, self).__init__()
        self._motor = motor
        self._state = False
        self._duration_seconds = duration_seconds
        self._pause_seconds = pause_seconds
        self._execute = True
        self._motor_state = motor_state
        self.daemon = True

    def run(self):
        logger.debug("Thread started")
        while self._execute is True:
            if self._state is True:
                self._motor.state = Motor.OFF
                self._state = False
                time.sleep(self._pause_seconds)
            else:
                self._motor.state = self._motor_state
                self._state = True
                time.sleep(self._duration_seconds)
        logger.debug("Reached end of thread")
        return

    def stop(self):
        logger.debug("Stopping thread")
        self._execute = False


class Motor(object):

    FORWARDS = 1
    BACKWARDS = 2
    OFF = 3

    def __init__(self, forwards_pin, backwards_pin):
        self._state = Motor.OFF
        """
        :type int
        """
        self._current_thread = None
        """
        :type MotorPulseThread
        """
        self._forwards_pin = forwards_pin
        self._backwards_pin = backwards_pin

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.update_state()

    def update_state(self):
        GPIO.output(self._forwards_pin, self._state == Motor.FORWARDS)
        GPIO.output(self._backwards_pin, self._state == Motor.BACKWARDS)

    def forwards(self):
        self.state = Motor.FORWARDS

    def backwards(self):
        self.state = Motor.BACKWARDS

    def backwards_pulse(self, duration_seconds, pause_seconds):
        self._current_thread = MotorPulseThread(self, duration_seconds, pause_seconds, Motor.BACKWARDS)
        self._current_thread.start()

    def forwards_pulse(self, duration_seconds, pause_seconds):
        self._current_thread = MotorPulseThread(self, duration_seconds, pause_seconds, Motor.FORWARDS)
        self._current_thread.start()

    def stop(self):
        if not self._current_thread is None:
            logger.debug("Attempting to stop current thread")
            self._current_thread.stop()
            self._current_thread = None
        self.state = Motor.OFF


left_motor = Motor(19, 21)
right_motor = Motor(24, 26)