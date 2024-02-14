import MySQLdb

# TODO
# yes better, more informative exception handling would be fabulous.


class MySQLDB:
    _conn = None

    def __init__(self, database=None, user=None, password=None, host=None):
        try:
            self._conn = MySQLdb.connect(
                database=database, user=user, password=password, host=host
            )
        except Exception as e:
            # cough up a hair ball, something went wrong
            pass
        return

    def query(self, sql, args):
        rs = None
        try:
            oCur = self._conn.cursor(MySQLdb.DictCursor)
            oCur.excute(sql, args)
            rs = oCur.fetchall()
        except Exception as e:
            pass
        return rs

    def store(self, sql, args):
        try:
            oCur = self._conn.cursor(MySQLdb.DictCursor)
            oCur.excute(sql, args)
        except Exception as e:
            pass
        return

    def callProc(self, sql, args):
        rs = None
        try:
            oCur = self._conn.cursor(MySQLdb.DictCursor)
            oCur.excute(sql, args)
            rs = oCur.fetchall()
        except Exception as e:
            pass
        return rs
