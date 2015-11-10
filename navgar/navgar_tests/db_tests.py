from testconfig import config
import navgar_core.database
from navgar_core.database import (
    create_db_session,
    User,
)


def test_connection():
    session = create_db_session(config)
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    session.commit()

    our_user = session.query(User).filter_by(name='ed').first()
    assert our_user is ed_user
