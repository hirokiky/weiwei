import deform
from webob import Response
from uiro.controller import BaseController
from uiro.view import view_config

from weiwei import page as weiwei_page
from weiwei import schema as weiwei_schema


def page_predicate(request, context):
    return bool(context.page)


def edit_param_predicate(request, context):
    return request.GET.get('edit') is not None


class PageController(BaseController):
    resource = weiwei_page.PageResource

    @view_config(method='get',
                 template_name='weiwei:page_edit.mako',
                 predicates=(edit_param_predicate,))
    def page_edit_view(self, request, context):
        form = deform.Form(weiwei_schema.PageText(), buttons=('submit',))
        if context.page:
            appstruct = dict(text=context.page.text)
        else:
            appstruct = dict()
        form = form.render(appstruct)
        return dict(request=request,
                    page_title=context.page_title,
                    form=form)

    @view_config(method='get',
                 template_name='weiwei:page.mako',
                 predicates=(page_predicate,))
    def page_view(self, request, context):
        return dict(request=request,
                    page=context.page)

    @view_config(method='get',
                 template_name='weiwei:page_not_found.mako')
    def page_not_found_view(self, request, context):
        return dict(request=request)

    @view_config(method='post')
    def pages_post_view(self, request, context):
        form = deform.Form(weiwei_schema.PageText(), buttons=('submit',))
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
        except deform.ValidationFailure as e:
            return dict(request=request,
                        page_title=context.page_title,
                        form=e.render())

        weiwei_page.insert_or_update_page(
            context.page,
            context.page_title,
            appstruct['text'],
        )

        return Response(
            status_code=302,
            location=request.matching.reverse(
                'weiwei_page', page_title=context.page_title,
            )
        )
