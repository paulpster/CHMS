from . import mysql_conn
from . import commons


def before_req(request, session, g):
    if "DB" not in g:
        print("get DB connection")
        g.DB = mysql_conn.mysql(None, commons.DB_DB)
        if g.DB is None:
            print("before_req: Null DB connection")

    return


def teardown_req(request, session, g):
    return
