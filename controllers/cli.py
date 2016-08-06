from controllers import Controller


class Cli(Controller):
    def _run(self):
        print 'Welcome to the robot command (type "exit" to quit)'
        while True:
            user_input = raw_input("> ")
            if user_input != 'exit':
                parts = user_input.split(' ')
                try:
                    returned = self.commands[parts[0]].execute(' '.join(parts[1:]))
                except KeyError:
                    print 'Unrecognised command: %s' % parts[0]
                if returned is not None:
                    print returned
            else:
                break
