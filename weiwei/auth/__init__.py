from pkg_resources import EntryPoint
from zope.interface.exceptions import BrokenImplementation

from weiwei.interfaces import IHasher


hash_api = None


def make_hashed(raw_password):
    if hash_api:
        raw_password = raw_password.encode('utf-8')
        return hash_api.encode(raw_password)
    else:
        raise NotImplementedError


def setup_hasher(hasher_name):
    hasher_class = EntryPoint.parse('hasher=%s' % hasher_name).load(False)
    if not IHasher.implementedBy(hasher_class):
        raise BrokenImplementation
    hasher = hasher_class()

    global hash_api
    hash_api = hasher
