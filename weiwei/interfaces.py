from zope.interface import Interface


class IHasher(Interface):
    def encode(raw_password):
        """ Encoding rawpassword to hashed.
        """
