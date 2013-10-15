import deform
from webob import Response

from weiwei.web import schema as web_schema
from weiwei.web import page as web_page


def page_view(request, page):
    return "{page.title}: {page.text}".format(page=page)


def page_edit_view(request, page, page_title):
    form = deform.Form(web_schema.PageText(), buttons=('submit',))
    if page:
        appstruct = dict(text=page.text)
    else:
        appstruct = dict()
    form = form.render(appstruct)
    return 'Title:{page_title}{form}'.format(
        page_title=page_title,
        form=form
    )


def page_not_found_view(requsest):
    return '<a href="?edit">edit</a>'


def page_post_view(request, page, page_title):
    form = deform.Form(web_schema.PageText(), buttons=('submit',))
    controls = request.POST.items()
    try:
        appstruct = form.validate(controls)
    except deform.ValidationFailure as e:
        return '{}'.format(e.render())

    web_page.insert_or_update_page(
        page,
        page_title,
        appstruct['text'],
    )

    return Response(
        status_code=302,
        location=request.matching.reverse(
            'web_page',
            page_title=page_title,
        )
    )


def login_view(request):
    if request.remote_user:
        return Response(
            status_code=302,
            location=request.matching.reverse('web_page',
                                              page_title='')
        )
    else:
        return Response(status_code=401)
