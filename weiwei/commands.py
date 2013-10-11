import os
import sys
from code import interact

from paste.deploy import loadapp
from gearbox.command import Command


class ShellCommand(Command):
    def get_parser(self, prog_name):
        parser = super(ShellCommand, self).get_parser(prog_name)
        parser.add_argument(
            "-c", "--config",
            help='application config file to read (default: development.ini)',
            dest='config_file', default="development.ini"
        )
        parser.add_argument(
            '-n', '--app-name',
            dest='app_name',
            metavar='NAME',
            help="Load the named application (default main)")
        return parser

    def take_action(self, parsed_args):
        app_spec = 'config:' + parsed_args.config_file
        app_name = parsed_args.app_name
        base = os.getcwd()
        app = loadapp(app_spec, name=app_name, relative_to=base)
        shell = self.make_default_shell()
        shell({'app': app}, 'app: WSGI application.')

    def make_default_shell(self, interact=interact):
        def shell(env, help):
            cprt = 'Type "help" for more information.'
            banner = "Python %s on %s\n%s" % (sys.version, sys.platform, cprt)
            banner += '\n\n' + help + '\n'
            interact(banner, local=env)
        return shell
