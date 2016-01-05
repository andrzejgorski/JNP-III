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
    ForeignKey,
)


Base = declarative_base()


_engine = None


def configure_engine(config):
    global _engine
    _engine = create_engine(config['db-url'])


def create_db_session():
    global _engine
    Base.metadata.create_all(_engine)
    Session = sessionmaker(bind=_engine)
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


posts_tbl = Table(
    'posts',
    Base.metadata,
    Column('id', Integer, Sequence('post_id_seq'), primary_key=True),
    Column('title', String(40), nullable=True),
    Column('content', String(300), nullable=False),
    Column('user_id', Integer, ForeignKey("users.id"), nullable=False),
)


class Post(Base):
    __tablename__ = 'posts'

    def __repr__(self):
        return "<Post(title='{}', content='{}', user='{}')>".format(
            self.title, self.content, self.user_id
        )


class User(Base):
    __tablename__ = 'users'

    def __repr__(self):
        return "<User(name='{}', fullname='{}', password='{}')>".format(
            self.name, self.fullname, self.password
        )


def recreate_db():
    for tbl in reversed(Base.metadata.sorted_tables):
        _engine.execute(tbl.delete())
    Base.metadata.create_all(_engine)
