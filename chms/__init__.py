import os

from flask import Flask


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(SECRET_KEY="KLJhKJHkljJH")

    # from utils.utils import teardown_req, before_req

    # app.teardown_appcontext(teardown_req)
    # before_req()

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello there. I am CHMS."

    from . import customer

    app.register_blueprint(customer.bp)
    app.add_url_rule("/", endpoint="index")

    @app.route("/<path:subpath>")
    def catchall(subpath):
        print(f"catch-all: {subpath}")
        return "catch-all"

    return app
