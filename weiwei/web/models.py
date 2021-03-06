import sqlalchemy as sa

from weiwei.db import Session, Base
from weiwei.web.markup import rst_renderer


class Page(Base):
    __tablename__ = 'pages'
    query = Session.query_property()

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(length=255),
                      unique=True)
    text = sa.Column(sa.Text)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return "<Page {0}>".format(self.title)

    @property
    def markuped_text(self):
        return rst_renderer(self.text)
