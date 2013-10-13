from matcha import make_wsgi_app
from repoze.who.config import make_middleware_with_config


from weiwei.auth import setup_hasher
from weiwei.db import initdb
from weiwei.matching import matching


def main(global_conf, root, **settings):
    initdb(settings)

    app = make_wsgi_app(matching)

    # weiwei.auth
    setup_hasher(settings['weiwei.auth.hasher'])

    # repoze.who
    config_file = settings['who.config_file']
    return make_middleware_with_config(app, global_conf, config_file)
