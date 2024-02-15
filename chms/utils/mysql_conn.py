import MySQLdb

# TODO
# yes better, more informative exception handling would be fabulous.


class MySQLConn:
    _conn = None

    def __init__(
        self, database=None, user=None, password=None, host=None, autocommit=True
    ):
        try:
            self._conn = MySQLdb.connect(
                database=database, user=user, password=password, host=host
            )
        except Exception as e:
            # cough up a hair ball, something went wrong
            print(f"MySQLConn::__init__ connection error {e}")
        return

    def query(self, sql, args):
        rs = None
        try:
            oCur = self._conn.cursor(MySQLdb.cursors.DictCursor)
            oCur.execute(sql, args)
            rs = oCur.fetchall()
        except Exception as e:
            print(f"MySQLConn::query error: {e}")
        return rs

    def store(self, sql, args):
        try:
            oCur = self._conn.cursor(MySQLdb.cursors.DictCursor)
            oCur.execute(sql, args)
        except Exception as e:
            print(f"MySQLConn::execute error: {e}")
        return

    def callProc(self, sql, args):
        rs = None
        try:
            oCur = self._conn.cursor(MySQLdb.cursors.DictCursor)
            oCur.callproc(sql, args)
            rs = oCur.fetchall()
        except Exception as e:
            print(f"MySQLConn::callProc error {e}")
        return rs
