from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    json,
    current_app,
    session,
    request,
)
from werkzeug.exceptions import abort
from . import utils

bp = Blueprint("cust", __name__)


@bp.before_request
def pre_req():
    utils.utils.before_req(request, session, g)
    return


@bp.teardown_request
def post_req(req):
    utils.utils.teardown_req(request, session, g)
    return


@bp.route("/<int:cid>", methods=(["GET", "POST", "PUT", "DELETE"]))
def customerCRUD(cid):
    if request.method == "PUT":
        data = json.loads(request.data)
        ret = utils.customer.updateCustomer(g.DB, cid, data)
    elif request.method == "POST":
        data = json.loads(request.data)
        ret = utils.customer.createCustomer(g.DB, data)
    elif request.method == "DELETE":
        ret = utils.customer.deleteCustomer(g.DB, cid)
    else:
        ret = utils.customer.getCustomer(g.DB, cid)

    return json.dumps(ret)
