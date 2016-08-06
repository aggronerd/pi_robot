import abc
import logging
from commands import COMMANDS

logger = logging.getLogger(__name__)


class Controller(object):
    def run(self):
        self._run()

    @abc.abstractmethod
    def _run(self):
        print 'showuld not seet this'
        pass

    def call(self, command, args):
        try:
            func = getattr(self, command)
            return func(command, args)
        except AttributeError:
            print "'%s' not found" % command

    def __init__(self):
        self.commands = dict()
        logger.debug('Loading commands...')
        for command in COMMANDS:
            logger.debug("Loading \"%s\"" % command.name)
            command_inst = command()
            self.commands[command_inst.name()] = command_inst
            for alias in command_inst.aliases():
                self.commands[alias] = command_inst
