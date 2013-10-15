from matcha import Matching as m, bundle, include, make_wsgi_app
from webob.static import DirectoryApp

from weiwei.web.matching import matching as web_matching


def get_matching_app(settings):
    static_app = DirectoryApp(settings['weiwei.static'])
    static_matching = m('/static/*path', static_app, name='static')
    matching = bundle(
        static_matching,
        include('', web_matching),
    )
    return make_wsgi_app(matching)
