import sys
from code import interact

from weiwei.commands import LoadAppCommand


class ShellCommand(LoadAppCommand):
    def take_action(self, parsed_args):
        app = self.loadapp(parsed_args)
        shell = self.make_default_shell()
        shell({'app': app}, 'app: WSGI application.')

    def make_default_shell(self, interact=interact):
        def shell(env, help):
            cprt = 'Type "help" for more information.'
            banner = "Python %s on %s\n%s" % (sys.version, sys.platform, cprt)
            banner += '\n\n' + help + '\n'
            interact(banner, local=env)
        return shell
