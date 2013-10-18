import sqlalchemy as sa
from sqlalchemy.orm import relationship

from weiwei.auth import make_hashed
from weiwei.db import Session, Base


class Roll(Base):
    __tablename__ = 'rolls'
    query = Session.query_property()

    name = sa.Column(sa.String(length=16),
                     unique=True,
                     primary_key=True)

    def __init__(self, name):
        self.name = name


class User(Base):
    __tablename__ = 'users'
    query = Session.query_property()

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(length=255),
                     unique=True)
    password = sa.Column(sa.String(255))
    roll_name = sa.Column(sa.String(length=16),
                          sa.ForeignKey('rolls.name'))
    roll = relationship('Roll')

    def __init__(self, name, password, roll):
        self.name = name
        self.set_password(password)
        self.roll = roll

    def set_password(self, raw_password):
        self.password = make_hashed(raw_password)

    def check_password(self, raw_password):
        hashed = make_hashed(raw_password)
        return self.password == hashed
