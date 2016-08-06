from .base import Command
import actions


class Move(Command):
    def _execute(self, args):
        if len(args) == 2:
            step = float(args[1])
            self.logger.debug("Got step of " + str(step))
            if step > 0:
                self.logger.debug("Got direction of %s" % args[0])
                if args[0] == "forward" or args[0] == "f":
                    actions.forward(step)
                elif args[0] == "back" or args[0] == "b":
                    actions.backwards(step)
                elif args[0] == "left" or args[0] == "l":
                    actions.left(step)
                elif args[0] == "right" or args[0] == "r":
                    actions.right(step)
                else:
                    return "Invalid direction " + args[0]
                return "Done"
        return "Invalid step " + args[1]

    def name(self):
        return 'move'

    def aliases(self):
        return ['mv']
