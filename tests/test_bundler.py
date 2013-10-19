import pytest


@pytest.fixture
def target():
    from weiwei.bundler import bundle_decorators
    return bundle_decorators


def outside_dec(func):
    def wraped(*args, **kwargs):
        return 'O' + func(*args, **kwargs) + 'O'
    return wraped


def inside_dec(func):
    def wraped(*args, **kwargs):
        return 'o' + func(*args, **kwargs) + 'o'
    return wraped


def dummy_func():
    return '.'


def test_not_specified_name(target):
    actual = target(
        outside_dec,
        inside_dec,
    )(dummy_func)

    assert actual() == 'Oo.oO'
    assert actual._dummy_func() == '.'


def test_specified_name(target):
    actual = target(
        outside_dec,
        inside_dec,
        original_name='orig'
    )(dummy_func)

    assert actual() == 'Oo.oO'
    assert actual.orig() == '.'
