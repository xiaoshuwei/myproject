import pytest
from urllib.parse import urlencode
from flaskr import create_app
from flask import Flask
# from flask.app import FlaskClient

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app:Flask):
    return app.test_client()


@pytest.fixture()
def runner(app:Flask):
    return app.test_cli_runner()

def test_request_example(client):
    response = client.get("/?{}".format(urlencode({
        "msg_signature":"012bc692d0a58dd4b10f8dfe5c4ac00ae211ebeb",
        "timestamp":"1476416373",
        "nonce":"47744683",
        "echostr":"fsi1xnbH4yQh0+PJxcOdhhK6TDXkjMyhEPA7xB2TGz6b+g7xyAbEkRxN/3cNXW9qdqjnoVzEtpbhnFyq6SVHyA=="
    })))
    print(12312312312312312)
    print(response.get_data())