def createCustomer(DB, data):
    # this is too basic, I do not have a grip in the new CID tso that I can return the new record
    sql = "INSERT INTO chms.customer (customer_name, customer_address, contact_number) VALUES (%s, %s, %s);"

    # yes this bit following is duplicated, need to decide what to do about it (create a validator or sorts?)
    if "name" not in data:
        # this is really not any good
        return
    addr = None
    num = None

    if "addr" in data:
        addr = data["addr"]
    if "num" in data:
        num = data["num"]

    DB.store(
        sql,
        (
            data["name"],
            addr,
            num,
        ),
    )
    rs = DB.query("SELECT LAST_INSERT_ID() AS last;", ())

    return getCustomer(sql, rs[0]["last"])


def deleteCustomer(DB, cid):
    # Thre are FK issues here, either need to remove the associated bookings, payments, invoices, letters
    #       OR the FK enforcment needs to occur in a proc that puts in the booking
    sql = "DELETE FROM chms.customer WHERE customer_id = %s;"
    DB.store(
        sql(
            cid,
        )
    )
    return None


def updateCustomer(DB, cid, data):
    sql = "UPDATE chms.customer SET customer_name = %s, customer_addr = %s, concact_number = %s WHERE customer.id = %s;"

    # yes this bit following is duplicated, need to decide what to do about it (create a validator or sorts?)
    if "name" not in data:
        # this is really not any good
        return
    addr = None
    num = None

    if "addr" in data:
        addr = data["addr"]
    if "num" in data:
        num = data["num"]

    DB.store(
        sql(
            data["name"],
            addr,
            num,
            cid,
        )
    )
    return getCustomer(DB, cid)


def getCustomer(DB, cid):
    sql = "SELECT * FROM chms.customer WHERE customer_id = %s;"
    rs = DB.excute(sql, (cid,))

    if rs:
        return {
            "customer_id": rs[0]["customer_id"],
            "customer_name": rs[0]["customer_name"],
            "customer_address": rs[0]["customer_address"],
            "contact_number": rs[0]["contact_number"],
        }
    return {
        "customer_id": "",
        "customer_name": "",
        "customer_address": "",
        "contact_number": "",
    }
