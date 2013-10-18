import transaction

from weiwei.commands import LoadAppCommand
from weiwei.db import Session, Base
from weiwei.auth.models import User, Roll
from weiwei.web.models import Page


class InitializeDBCommand(LoadAppCommand):
    def take_action(self, parsed_args):
        self.loadapp(parsed_args)

        Base.metadata.create_all(Session.bind)
        session = Session()
        roll = Roll(name='editor')
        user = User(name='test', password='test', roll=roll)
        page = Page(title='', text="""
Front Page
==========

Hello, WeiWei.

WeiWei is a reader-friendly Wiki engine.

login
-----
Now, 'test' user is available.
Click the button in the upper right corner,
and login user 'test' with 'test' password.

edit
----
After login, you will be able to edit this page.
Notice the login button you clicked was changed
to 'edit' button.

Try tof click it and edit this page.

and more
---------

* creating `another page </another>`_
""")
        session.add(roll)
        session.add(user)
        session.add(page)
        transaction.commit()
