import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from zope.sqlalchemy import ZopeTransactionExtension

Base = declarative_base()
Session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


def initdb(config):
    engine = sa.engine_from_config(config, 'sqlalchemy.')
    Session.configure(bind=engine)
