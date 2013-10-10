import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from zope.sqlalchemy import ZopeTransactionExtension


Base = declarative_base()
Session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


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
