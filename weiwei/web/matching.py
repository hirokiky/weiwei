from matcha import Matching as m, bundle

from weiwei.web import login_dispatch, page_dispatch


matching = bundle(
    m('/login', login_dispatch, name='web_login'),
    m('/{page_title}', page_dispatch, name='web_page'),
)

