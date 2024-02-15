import os
import sys

###############################################################################
#   i hate this. but there is a difference between this project and the flask
#   tutorial in the personal directory. there is something about the virtual
#   environment that is different. I have not figured it out. When I do this
#   manual path adjustment will not be needed
sys.path.append("/home/paulp/Data/personal/CMHS")
sys.path.append("/usr/lib/python3/dist-packages")

import pytest
from chms import create_app


@pytest.fixture
def app():
    app = create_app(
        {
            "TESTING": True,
        }
    )


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
