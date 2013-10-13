import hashlib

from zope.interface import implementer

from weiwei.interfaces import IHasher


@implementer(IHasher)
class SHA1Hasher(object):
    def encode(self, raw_password):
        return hashlib.sha1(raw_password).hexdigest()
