from pkg_resources import EntryPoint
from webob import Response
from zope.interface.exceptions import BrokenImplementation

from weiwei.interfaces import IHasher


hasher = None


def get_hasher():
    return hasher


def roll_required(*roll_names):
    def _roll_validator(user):
        if user and user.roll_name in roll_names:
            return True
        else:
            return False

    def wrapper(view_callable):
        def _wraped(request, *args, **kwargs):
            if _roll_validator(request.remote_user):
                return view_callable(request, *args, **kwargs)
            else:
                return Response(status_code=401)
        return _wraped
    return wrapper


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
