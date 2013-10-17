from webob import Response
from webob.dec import wsgify

from weiwei.request import Request
from weiwei.web import schema as web_schema
from weiwei.web import models as web_models
from weiwei.web import views as web_views
from weiwei.web.page import apply_page_resource


@wsgify(RequestClass=Request)
def login_dispatch(request):
    return web_views.login_view(request)


@wsgify(RequestClass=Request)
@apply_page_resource
def page_dispatch(request):
    if request.method == 'GET':
        if request.GET.get('edit') is not None:
            return web_views.page_edit_view(request)
        elif request.page:
            return web_views.page_view(request)
        else:
            return web_views.page_not_found_view(request)
    elif request.method == 'POST':
        return web_views.page_post_view(request)
    else:
        return Response(
            status_code=405,
            allow=['GET', 'POST']
        )
