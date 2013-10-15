import sqlalchemy as sa
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from zope.sqlalchemy import ZopeTransactionExtension

Session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

from weiwei.auth import models as auth_models
from weiwei.web import models as web_models


def initdb(config):
    def _init(engine, base):
        base.metadata.bind = engine
        base.metadata.create_all()

    engine = sa.engine_from_config(config, 'sqlalchemy.')
    Session.configure(bind=engine)

    _init(engine, auth_models.Base)
    _init(engine, web_models.Base)
