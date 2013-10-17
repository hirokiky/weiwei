import colander
import transaction
from webob import Response

from weiwei.web import schema as web_schema
from weiwei.web import models as web_models
from weiwei.web.models import Page, Session


def insert_or_update_page(page, page_title, page_text):
    if not page:
        session = Session()
        session.add(Page(page_title,
                         page_text))
    else:
        page.text = page_text
    transaction.commit()
    return page


def apply_page_resource(view_callable):
    def wraped(request, *args, **kwargs):
        page_title = request.matched_dict['page_title']
        schema = web_schema.PageTitle()
        try:
            deserialized = schema.deserialize(dict(title=page_title))
            request.page_title = deserialized['title']
        except colander.Invalid:
            return Response(status_code=400, body='Provided page title was too long')

        request.page = web_models.Page.query.filter_by(title=page_title).first()

        return view_callable(request, *args, **kwargs)
    return wraped
