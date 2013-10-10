import deform
from webob import Response

from weiwei.web import schema as web_schema
from weiwei.web import page as web_page


def page_view(request, page):
    return "{page.title}: {page.text}".format(page=page)


def page_edit_view(request, page, page_title):
    form = deform.Form(web_schema.Page(), buttons=('submit',))
    if page:
        appstruct = dict(title=page.title,
                         text=page.text)
    else:
        appstruct = dict(title=page_title)
    form = form.render(appstruct)
    return '{}'.format(form)


def page_not_found_view(requsest):
    return '<a href="?edit">edit</a>'


def page_post_view(request, page):
    form = deform.Form(web_schema.Page(), buttons=('submit',))
    controls = request.POST.items()
    try:
        appstruct = form.validate(controls)
    except deform.ValidationFailure as e:
        return '{}'.format(e.render())

    web_page.insert_or_update_page(
        page,
        appstruct['title'],
        appstruct['text'],
    )

    return Response(
        status_code=302,
        location=request.matching.reverse(
            'page',
            page_title=appstruct['title']
        )
    )


def login_view(request):
    raise NotImplemented


def login_post_view(request):
    raise NotImplemented


def logout_view(request):
    raise NotImplemented
