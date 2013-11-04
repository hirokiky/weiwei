import colander
import transaction
from uiro.controller import NotFound
from uiro.db import Session

from weiwei import schema as web_schema
from weiwei.models import Page


def insert_or_update_page(page, page_title, page_text):
    if not page:
        session = Session()
        session.add(Page(page_title,
                         page_text))
    else:
        page.text = page_text
    transaction.commit()
    return page


class PageResource(object):
    def __init__(self, request):
        self.request = request

    @property
    def page_title(self):
        page_title = self.request.matched_dict.get('page_title')

        schema = web_schema.PageTitle()
        try:
            deserialized = schema.deserialize(dict(title=page_title))
            return deserialized['title']
        except colander.Invalid:
            raise NotFound

    @property
    def page(self):
        return Page.query.filter_by(title=self.page_title).first()
