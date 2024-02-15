from . import mysql_conn
from . import commons


def before_req(request, session, g):
    if "DB" not in g:
        print("get DB connection")
        g.DB = mysql_conn.mysql(
            database=commons.DB_DB,
            user=commons.DB_USER,
            password=commons.DB_PWD,
            host=commons.DB_HOST,
        )
        if g.DB is None:
            print("before_req: Null DB connection")

    return g.DB


def teardown_req(request, session, g):
    DB = g.pop("DB", None)

    if DB is not None:
        DB.close()
    return
