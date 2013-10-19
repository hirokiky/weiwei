from functools import reduce


def bundle_decorators(*decorators, original_name=None):
    def wrapper(func):
        bundled = reduce(lambda a, b: b(a),
                         [func] + list(reversed(decorators)))

        def wraped(*args, **kwargs):
            return bundled(*args, **kwargs)
        setattr(wraped,
                original_name or '_' + func.__name__,
                func)
        return wraped
    return wrapper
