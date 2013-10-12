from matcha import make_wsgi_app
from repoze.who.config import make_middleware_with_config


from weiwei.db import initdb
from weiwei.matching import matching


def main(global_conf, root, **settings):
    initdb(settings)

    app = make_wsgi_app(matching)

    config_file = settings['who.config_file']
    return make_middleware_with_config(app, global_conf, config_file)
