import pytest

import json


# these are bare bone functionality checking. nothing clever.
def test_customer_post(client):
    ret = client.post(
        "/0",
        data=json.dumps({"name": "george", "addr": "Baltimore", "num": "2075551212"}),
    )

    assert ret.status_code == 200


def test_customer_put(client):
    ret = client.put(
        "/1000",
        data=json.dumps({"name": "frank", "addr": "Atlanta", "num": "3035551212"}),
    )

    assert ret.status_code == 200
    return


def test_customer_get(client):
    ret = client.get("/1000")

    assert ret.status_code == 200
    return


def test_customer_delete(client):
    ret = client.delete("/1000")

    assert ret.status_code == 200
    return
