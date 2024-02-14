import os

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)

    try:
        fh = open("location.dat")
        print("found location.dat :)")
        loc = fh.readline().strip()
    except:
        print("location.dat not found.")
        loc = ""

    app.config.from_mapping(SECRET_KEY="KLJhKJHkljJH", APP_ROOT=loc)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

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
