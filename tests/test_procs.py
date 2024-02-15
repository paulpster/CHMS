import pytest

from chms.utils.mysql_conn import MySQLConn
from chms.utils.commons import DB_DB, DB_HOST, DB_PWD, DB_USER

# basic functionality testing. no real data to back things up.


def get_db():
    return MySQLConn(database=DB_DB, user=DB_USER, password=DB_PWD, host=DB_HOST)


def test_daily_report():
    DB = get_db()

    assert DB is not None

    sql = "chms.daily_report"
    rs = DB.callProc(sql, ("2024-02-14",))
    assert rs is not None
    return


def test_availability_report():
    DB = get_db()

    assert DB is not None

    sql = "chms.availability_report"
    rs = DB.callProc(sql, ("2024-02-14",))
    assert rs is not None
    return


def test_old_customer_book():
    DB = get_db()

    assert DB is not None

    sql = "chms.old_customer_booking"
    rs = DB.callProc(sql, (1000, 1000, "2024-02-15", "2024-02-17", 123.56))
    return


def test_new_customer_book():
    DB = get_db()

    assert DB is not None

    sql = "chms.new_customer_booking"
    rs = DB.callProc(
        sql,
        ("george", "Alabama", "6548676542", 1000, "2024-02-15", "2024-02-17", 123.56),
    )
    return
