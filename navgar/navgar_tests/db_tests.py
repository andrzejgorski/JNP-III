from testconfig import config
import navgar_core.database
from navgar_core.database import (
    create_db_session,
    User,
    recreate_db,
)


def test_connection():
    session = create_db_session(config)
    recreate_db()
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    session.commit()

    our_user = session.query(User).filter_by(name='ed').one()
    assert our_user.name == 'ed'
    assert our_user.fullname == 'Ed Jones'
    assert our_user.password == 'edspassword'
