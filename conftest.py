from flask.helpers import url_for
import pytest
from website import create_app
from flask import Response

class MyResponse(Response):

    @property
    def json(self):
        return 42

@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.response_class = MyResponse
    return app

def test_my_json_response(client):
    res = client.get(url_for('api.ping'))
    assert res.json == 42
