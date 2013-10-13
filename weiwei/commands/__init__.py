import os

from paste.deploy import loadapp
from gearbox.command import Command


class LoadAppCommand(Command):
    def get_parser(self, prog_name):
        parser = super(LoadAppCommand, self).get_parser(prog_name)
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

    def loadapp(self, parsed_args):
        app_spec = 'config:' + parsed_args.config_file
        app_name = parsed_args.app_name
        base = os.getcwd()
        return loadapp(app_spec, name=app_name, relative_to=base)
