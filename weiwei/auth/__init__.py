from pkg_resources import EntryPoint
from zope.interface.exceptions import BrokenImplementation

from weiwei.interfaces import IHasher


hasher = None


def get_hasher():
    return hasher


def roll_validator_factory(*roll_names):
    def roll_validator(user):
        if user and user.roll_name in roll_names:
            return True
        else:
            return False
    return roll_validator


def make_hashed(raw_password):
    hasher = get_hasher()
    if hasher:
        raw_password = raw_password.encode('utf-8')
        return hasher.encode(raw_password)
    else:
        raise NotImplementedError


def setup_hasher(hasher_name):
    hasher_class = EntryPoint.parse('hasher=%s' % hasher_name).load(False)
    if not IHasher.implementedBy(hasher_class):
        raise BrokenImplementation
    _hasher = hasher_class()

    global hasher
    hasher = _hasher
