from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy import (
    Column,
    Integer,
    String,
    MetaData,
    Table,
)


Base = declarative_base()
metadata = MetaData()


_engine = None


def _get_engine(url=None):
    global _engine
    if _engine is not None:
        return _engine
    _engine = create_engine(url)
    return _engine


def create_db_session(config=None):
    engine = _get_engine(config['db-url'])
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


users_tbl = Table(
    'users',
    Base.metadata,
    Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
    Column('name', String(20), nullable=False),
    Column('fullname', String(40)),
    Column('password', String(40), nullable=False),
)


class User(Base):
    __tablename__ = 'users'

    def __repr__(self):
        return "<User(name='{}', fullname='{}', password='{}')>".format(
            self.name, self.fullname, self.password
        )

# mapper(User, users_tbl,

def recreate_db():
    engine = _get_engine()
    for tbl in reversed(Base.metadata.sorted_tables):
        engine.execute(tbl.delete())
    Base.metadata.create_all(engine)
