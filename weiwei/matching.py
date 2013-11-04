from matcha import Matching as m

from .views import PageController


matching = m('/{page_title}', PageController(), name='weiwei_page')
