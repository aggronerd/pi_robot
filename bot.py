from jabberbot import JabberBot, botcmd
import commands
import logging

logger = logging.getLogger(__name__)

class PiRobotJabberBot(JabberBot):
    @botcmd
    def serverinfo( self, mess, args):
        """Displays information about the server"""
        version = open('/proc/version').read().strip()
        loadavg = open('/proc/loadavg').read().strip()

        return '%s\n\n%s' % ( version, loadavg, )

    @botcmd
    def mv(self, mess, args):
        self.move(mess, args)

    @botcmd
    def move(self, mess, args):
        """
        :type mess: str
        :type args: str
        """
        args = args.split(" ")
        if len(args) == 2:
            step = float(args[1])
            logger.debug("Got step of " + str(step))
            if step > 0:
                logger.debug("Got direction of " + str(step))
                if args[0] == "forward" or args[0] == "f":
                    commands.forward(step)
                elif args[0] == "back" or args[0] == "b":
                    commands.backwards(step)
                elif args[0] == "left" or args[0] == "l":
                    commands.left(step)
                elif args[0] == "right" or args[0] == "r":
                    commands.right(step)
                else:
                    return "Invalid direction " + args[0]
                return "Done"
        return "Invalid step " + args[1]

    @botcmd
    def terminate(self, mess, args):
        self.shutdown()

    @botcmd
    def whoami(self, mess, args):
        """Tells you your username"""
        return mess.getFrom().getStripped()