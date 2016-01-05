from testconfig import config
import navgar_core.database
from navgar_core.database import (
    create_db_session,
    User,
    Post,
    recreate_db,
    configure_engine,
)


def test_add_user():
    configure_engine(config)
    session = create_db_session()
    recreate_db()
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    session.commit()

    our_user = session.query(User).filter_by(name='ed').one()
    assert our_user.name == 'ed'
    assert our_user.fullname == 'Ed Jones'
    assert our_user.password == 'edspassword'


def test_add_post():
    configure_engine(config)
    session = create_db_session()
    recreate_db()

    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    session.commit()

    ed_post = Post(
        title='My title', content='Post content hehehe', user_id=ed_user.id)
    session.add(ed_post)
    session.commit()

    selected_user = session.query(User).filter_by(name='ed').one()
    assert selected_user.name == 'ed'
    assert selected_user.fullname == 'Ed Jones'
    assert selected_user.password == 'edspassword'

    selected_post = (
        session.query(Post).filter_by(user_id=selected_user.id).one())

    assert selected_post.title == 'My title'
    assert selected_post.content == 'Post content hehehe'
    assert selected_post.user_id == selected_user.id
