from repoze.who.interfaces import IAuthenticator

from zope.interface import implementer


@implementer(IAuthenticator)
class SillyPlugin(object):
    def authenticate(self, environ, identity):
        try:
            return identity['login']
        except KeyError:
            return None


def make_silly_plugin():
    return SillyPlugin()
