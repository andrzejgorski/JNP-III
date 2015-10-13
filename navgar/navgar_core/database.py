import os
import psycopg2


class Session():
    db = None


def mock_session():
    return Session()


try:
    import urlparse
except ImportError:
    get_db_session = mock_session


# def get_db_session():
#     urlparse.uses_netloc.append("postgres")
#     url = urlparse.urlparse(os.environ["DATABASE_URL"])
#
#     conn = psycopg2.connect(
#         database=url.path[1:],
#         user=url.username,
#         password=url.password,
#         host=url.hostname,
#         port=url.port
#     )
#     return conn
