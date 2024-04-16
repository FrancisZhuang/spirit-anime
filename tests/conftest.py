import pytest

from flask import Flask
from flask_restful import Api

from apps.app import SpiritAnime, SpiritAnimeDetail


@pytest.fixture()
def app():
    app = Flask(__name__)
    api = Api(app)
    BASE_URL = '/api/v1/spiritanime/'

    api.add_resource(SpiritAnime, BASE_URL)
    api.add_resource(SpiritAnimeDetail, BASE_URL + "<int:user_id>")
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
