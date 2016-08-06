__author__ = 'greg'

from actuators import left_motor, right_motor
import time


def sleep(duration):
    """
    :type duration: float
    """
    time.sleep(duration)


def forward(duration):
    """
    :type duration: float
    :param duration: The duration is seconds to maintain the movement
    """
    right_motor.forwards()
    left_motor.forwards()
    sleep(duration)
    right_motor.stop()
    left_motor.stop()


def backwards(duration):
    """
    :type duration: float
    :param duration: The duration is seconds to maintain the movement
    """
    right_motor.backwards()
    left_motor.backwards()
    sleep(duration)
    right_motor.stop()
    left_motor.stop()


def left(duration):
    """
    :type duration: float
    :param duration: The duration is seconds to maintain the movement
    """
    right_motor.forwards()
    left_motor.backwards_pulse(0.5, 0.5)
    sleep(duration)
    right_motor.stop()
    left_motor.stop()


def right(duration):
    """
    :type duration: float
    :param duration: The duration is seconds to maintain the movement
    """
    left_motor.forwards()
    right_motor.backwards_pulse(0.5, 0.5)
    sleep(duration)
    right_motor.stop()
    left_motor.stop()