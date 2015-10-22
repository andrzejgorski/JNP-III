from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String


Base = declarative_base()


# url = os.environ.get('DATABASE_URL', 'url')


def create_db_session():
    engine = create_engine('postgresql://postgres:postgres@localhost/test_db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)


    def __repr__(self):
        return "<User(name='{}', fullname='{}', password='{}')>".format(
            self.name, self.fullname, self.password
        )