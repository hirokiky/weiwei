from repoze.who.interfaces import IAuthenticator

from zope.interface import implementer

from weiwei.auth.models import User


@implementer(IAuthenticator)
class UserAuthenticationPlugin(object):
    def authenticate(self, environ, identity):
        try:
            user_name = identity['login']
            password = identity['password']
        except KeyError:
            return None

        user = User.query.filter_by(name=user_name).first()
        if user and user.check_password(password):
            return user
        else:
            return None


def make_user_authentication_plugin():
    return UserAuthenticationPlugin()
