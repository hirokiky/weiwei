from repoze.who.config import make_middleware_with_config

from weiwei.auth import setup_hasher
from weiwei.db import initdb
from weiwei.matching import get_matching_app


def main(global_conf, root, **settings):
    initdb(settings)

    app = get_matching_app(settings)

    # weiwei.auth
    setup_hasher(settings['weiwei.auth.hasher'])

    # repoze.who
    config_file = settings['who.config_file']
    return make_middleware_with_config(app, global_conf, config_file)
