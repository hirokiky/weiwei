import sqlalchemy as sa

from weiwei.web.models import Base, Session


def initdb(config):
    engine = sa.engine_from_config(config, 'sqlalchemy.')
    Session.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all()
