from matcha import make_wsgi_app

from weiwei.db import initdb
from weiwei.matching import matching


def main(grobal_conf, root, **settings):
    initdb(settings)
    return make_wsgi_app(matching)
