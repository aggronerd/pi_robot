import abc
import logging
import shlex


class Command(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @abc.abstractmethod
    def name(self):
        """

        :return: The name of the command
        """
        pass

    def aliases(self):
        return []

    def execute(self, args_string):
        return self._execute(shlex.split(args_string))

    @abc.abstractmethod
    def _execute(self, args):
        """
        Perform the actual method.

        :return: Output of call
        """
        pass