import deform
from webob import Response

from weiwei.auth import roll_required
from weiwei.web import schema as web_schema
from weiwei.web import page as web_page
from weiwei.template.renderer import using_template


@using_template('weiwei.web.templates.page')
def page_view(request):
    return dict(page=request.page)


@roll_required('editor')
@using_template('weiwei.web.templates.page_edit')
def page_edit_view(request):
    form = deform.Form(web_schema.PageText(), buttons=('submit',))
    if request.page:
        appstruct = dict(text=request.page.text)
    else:
        appstruct = dict()
    form = form.render(appstruct)
    return dict(page_title=request.page_title,
                form=form)


@using_template('weiwei.web.templates.page_not_found')
def page_not_found_view(requsest):
    return {}


@roll_required('editor')
@using_template('weiwei.web.templates.page_edit')
def page_post_view(request):
    form = deform.Form(web_schema.PageText(), buttons=('submit',))
    controls = request.POST.items()
    try:
        appstruct = form.validate(controls)
    except deform.ValidationFailure as e:
        return dict(page_title=request.page_title,
                    form=e.render())

    web_page.insert_or_update_page(
        request.page,
        request.page_title,
        appstruct['text'],
    )

    return Response(
        status_code=302,
        location=request.matching.reverse(
            'web_page',
            page_title=request.page_title,
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
