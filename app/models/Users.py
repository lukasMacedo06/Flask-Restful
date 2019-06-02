from sqlalchemy.inspection import inspect
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import DateTime, Integer, SmallInteger, String

from app.models import db


class Users(db.Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(150), nullable=False, unique=False)
    email = Column(String(200), nullable=False, unique=True)
    birthday = Column(DateTime, nullable=False, unique=False)
    salt = Column(String(30), nullable=False, unique=False)
    password = Column(String(200), nullable=False, unique=False)
    status = Column(SmallInteger, nullable=False, unique=False, default=1)

    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
