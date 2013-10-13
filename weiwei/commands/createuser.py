import transaction

from weiwei.commands import LoadAppCommand
from weiwei.db import Session
from weiwei.auth.models import User, Roll


class CreateUserCommand(LoadAppCommand):
    def take_action(self, parsed_args):
        self.loadapp(parsed_args)

        session = Session()
        roll = Roll(name='test')
        user = User(name='test', password='test', roll=roll)
        session.add(roll)
        session.add(user)
        transaction.commit()
