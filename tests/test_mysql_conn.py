import pytest

from chms.utils.mysql_conn import MySQLConn
from chms.utils.commons import DB_DB, DB_HOST, DB_PWD, DB_USER


def get_db():
    return MySQLConn(database=DB_DB, user=DB_USER, password=DB_PWD, host=DB_HOST)


def test_make_connection():
    DB = get_db()

    assert DB is not None
    return


def test_store():
    DB = get_db()

    assert DB is not None

    # TODO: things are still cockeyed. this record is not in the DB
    # I have a connection/commit/config issue
    SQL = "INSERT INTO chms.customer (customer_name, customer_address, contact_number) VALUES (%s, %s, %s);"
    DB.store(SQL, ("Paul Power", "Billings, MT", "4065551212"))
    return


def test_execute():
    DB = get_db()

    assert DB is not None

    rs = DB.query("SELECT * FROM chms.customer ORDER BY customer_id", ())
    assert rs is not None
    return


def test_callproc():
    DB = get_db()

    assert DB is not None

    sql = "chms.daily_report"
    rs = DB.callProc(sql, ("2024-02-14",))
    assert rs is not None
    return
