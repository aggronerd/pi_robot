__author__ = 'greg'


class Motor(object):

    FORWARDS = 1
    BACKWARDS = 2
    OFF = 3

    def __init__(self):
        self._state = Motor.OFF
        """
        :type int
        """

    @property
    def state(self):
        return self._state

    @state.setter(property=state)
    def set_state(self, value):
        self._state = value