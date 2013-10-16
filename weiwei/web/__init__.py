import colander
from webob import Response
from webob.dec import wsgify

from weiwei.request import Request
from weiwei.web import schema as web_schema
from weiwei.web import models as web_models
from weiwei.web import views as web_views


@wsgify(RequestClass=Request)
def login_dispatch(request):
    return web_views.login_view(request)


@wsgify(RequestClass=Request)
def page_dispatch(request):
    page_title = request.matched_dict['page_title']
    schema = web_schema.PageTitle()
    try:
        deserialized = schema.deserialize(dict(title=page_title))
        page_title = deserialized['title']
    except colander.Invalid:
        return Response(status_code=400, body='Provided page title was too long')

    page = web_models.Page.query.filter_by(title=page_title).first()

    if request.method == 'GET':
        if request.GET.get('edit') is not None:
            return web_views.page_edit_view(request, page, page_title)
        elif page:
            return web_views.page_view(request, page)
        else:
            return web_views.page_not_found_view(request)
    elif request.method == 'POST':
        return web_views.page_post_view(request, page, page_title)
    else:
        return Response(
            status_code=405,
            allow=['GET', 'POST']
        )
