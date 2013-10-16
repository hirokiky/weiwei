import transaction
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
