from contextlib import contextmanager
from sqlite3 import connect, Error

database = './users_hw.db'


@contextmanager
def connection():
    conn = None
    try:
        conn = connect(database=database)
        yield conn
        conn.commit()
    except Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
