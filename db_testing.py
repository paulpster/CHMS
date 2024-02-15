import sys

sys.path.append("/usr/lib/python3/dist-packages")

import MySQLdb

DB_DB = "chms"
DB_USER = "ppower"
DB_PWD = "ppower"
DB_HOST = "127.0.0.1"


class MySQLConn:
    _conn = None

    def __init__(
        self, database=None, user=None, password=None, host=None, autocommit=True
    ):
        self._conn = MySQLdb.connect(
            database=database, user=user, password=password, host=host
        )
        return

    def query(self, sql, args):
        rs = None
        oCur = self._conn.cursor(MySQLdb.cursors.DictCursor)
        oCur.execute(sql, args)
        rs = oCur.fetchall()
        return rs

    def store(self, sql, args):
        oCur = self._conn.cursor(MySQLdb.cursors.DictCursor)
        oCur.execute(sql, args)
        return

    def callProc(self, sql, args):
        rs = None
        oCur = self._conn.cursor(MySQLdb.cursors.DictCursor)
        oCur.callproc(sql, args)
        rs = oCur.fetchall()
        return rs


if __name__ == "__main__":
    conn = MySQLConn(database=DB_DB, user=DB_USER, password=DB_PWD, host=DB_HOST)
    SQL = "INSERT INTO chms.customer (customer_name, customer_address, contact_number) VALUES (%s, %s, %s);"
    conn.store(
        SQL,
        (
            "Paul Power",
            "Billings, MT",
            "4065551212",
        ),
    )

    rs = conn.query("SELECT * FROM chms.customer ORDER BY customer_id", ())
    print(rs)

    rs = conn.query("SELECT LAST_INSERT_ID() AS last;", ())
    print(rs, rs[0]["last"])

    sql = "chms.daily_report"
    rs = conn.callProc(sql, ("2024-02-14",))
    print(rs)
