from .base import Command


class Status(Command):
    def _execute(self, args):
        """Displays information about the server"""
        version = open('/proc/version').read().strip()
        loadavg = open('/proc/loadavg').read().strip()
        return '%s\n%s' % (version, loadavg,)

    def name(self):
        return 'serverinfo'

    def aliases(self):
        return ['status']
