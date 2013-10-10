from matcha import Matching as m, bundle


from weiwei.web import login_dispatch, logout_dispatch, page_dispatch

matching = bundle(
    m('/login', login_dispatch, name='login'),
    m('/logout', logout_dispatch, name='logout'),
    m('/{page_title}', page_dispatch, name='page'),
)
