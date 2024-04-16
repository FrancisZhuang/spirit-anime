"""Test app.py APIs"""

from urllib import parse
from flask import Flask
from flask.testing import FlaskClient
from flask_restful import Api

from apps.app import SpiritAnime, SpiritAnimeDetail
from utils.storage import Storage
from utils.random_num import random_number

app = Flask(__name__)
api = Api(app)
BASE_URL = '/api/v1/spiritanime/'

api.add_resource(SpiritAnime, BASE_URL)
api.add_resource(SpiritAnimeDetail, BASE_URL + "<int:user_id>")


class TestSpiritAnime:
    """Test Spirit Anime Restful APIs"""
    client: FlaskClient = app.test_client()

    def test_put_success(self):
        """Test successful scenario in put method"""
        full_name = 'francis' + str(random_number(6))
        data = {'full_name': full_name, 'dob': '1990-01-01'}
        response = self.client.put(BASE_URL, data=data)
        assert response.status_code == 201, 'unable to create spirit character successfully'

        # clean test case in db
        storage = Storage()
        storage.delete_user_name_dob(full_name, '1990-01-01')

    def test_put_missing_required(self):
        """Test missing required scenario in put method"""
        full_name = 'francis' + str(random_number(6))
        data = {'full_name': full_name}
        response = self.client.put(BASE_URL, data=data)
        assert response.status_code == 400, 'unexpected result, it is supposed to 400 missing required field'

    def test_put_invalid_dob(self):
        """Test invalid dob scenario in put method"""
        full_name = 'francis' + str(random_number(6))
        data = {'full_name': full_name, 'dob': '122321-01-12'}
        response = self.client.put(BASE_URL, data=data)
        assert response.status_code == 400, 'unexpected result, it is supposed to 400 invalid dob format'

    def test_put_already_exist(self):
        """Test full name and dob already exist scenario in put method"""
        storage = Storage()
        random_num = random_number(6)

        # prepare test case in db
        storage.add_anime_data(random_num, 'test', '1990-01-01', 'test', 'test', 'test')

        data = {'full_name': 'test', 'dob': '1990-01-01'}
        response = self.client.put(BASE_URL, data=data)
        assert response.status_code == 409, 'unexpected result, it is supposed to 409 invalid dob format'

        # clean test case in db
        storage.delete_user(random_num)

    def test_get_success(self):
        """Test successful scenario in get method"""
        response = self.client.get(BASE_URL)
        assert response.status_code == 200, 'unable to fetch user list'


class TestSpiritAnimeDetail:
    """Test Spirit Anime Detail Restful APIs"""
    client = app.test_client()

    def test_get_success(self):
        """Test successful scenario in get method"""
        storage = Storage()
        random_num = random_number(6)
        url = parse.urljoin(BASE_URL, str(random_num))

        # prepare test case in db
        storage.add_anime_data(random_num, 'test', '1990-01-01', 'test', 'test', 'test')

        response = self.client.get(url)
        assert response.status_code == 200, 'unable to fetch user data'

        # clean test case in db
        storage.delete_user(random_num)

    def test_get_failed(self):
        """Test Id not found scenario in get method"""
        random_num = random_number(6)
        url = parse.urljoin(BASE_URL, str(random_num))
        response = self.client.get(url)
        assert response.status_code == 404, 'unexpected result, it is supposed to 404 Id not found'

    def test_post_success(self):
        """Test successful scenario in post method"""
        storage = Storage()
        random_num = random_number(6)
        url = parse.urljoin(BASE_URL, str(random_num))

        # prepare test case in db
        storage.add_anime_data(random_num, 'test', '1990-01-01', 'test', 'test', 'test')

        data1 = {'full_name': 'update_name'}
        # update full name
        response1 = self.client.post(url, data=data1)
        assert response1.status_code == 200, 'unable to update user data'
        data2 = {'dob': '1919-12-01'}
        # update dob
        response2 = self.client.post(url, data=data2)
        assert response2.status_code == 200, 'unable to update user data'
        data3 = {'full_name': 'update_again', 'dob': '2019-07-01'}
        # update full name and dob
        response3 = self.client.post(url, data=data3)
        assert response3.status_code == 200, 'unable to update user data'

        # clean test case in db
        storage.delete_user(random_num)

    # Id not found
    def test_post_failed_404(self):
        """Test Id not found scenario in post method"""
        random_num = random_number(6)
        url = parse.urljoin(BASE_URL, str(random_num))
        data = {'full_name': 'update_name'}
        response = self.client.post(url, data=data)
        assert response.status_code == 404, 'unexpected result, it is supposed to 404 Id not found'

    # User has already exist
    def test_post_failed_409(self):
        """Test User already exist scenario in post method"""
        storage = Storage()
        random_num1 = random_number(6)
        random_num2 = random_number(6)
        random_num3 = random_number(6)
        random_num4 = random_number(6)

        # prepare test cases in db
        storage.add_anime_data(random_num1, 'test1', '1990-01-01', 'test1', 'test1', 'test1')
        storage.add_anime_data(random_num2, 'test2', '1990-01-01', 'test2', 'test2', 'test2')
        storage.add_anime_data(random_num3, 'test1', '2000-01-01', 'test3', 'test3', 'test3')
        storage.add_anime_data(random_num4, 'test4', '2021-08-01', 'test4', 'test4', 'test4')

        data1 = {'full_name': 'test2'}
        url = parse.urljoin(BASE_URL, str(random_num1))
        # update full name to exist user's full name
        response1 = self.client.post(url, data=data1)
        assert response1.status_code == 409, 'unexpected result, it is supposed to 409 User has already exist'
        data2 = {'dob': '2000-01-01'}
        # update dob to exist user's dob
        response2 = self.client.post(url, data=data2)
        assert response2.status_code == 409, 'unexpected result, it is supposed to 409 User has already exist'
        data3 = {'full_name': 'test4', 'dob': '2021-08-01'}
        # update full name and dob
        response3 = self.client.post(url, data=data3)
        assert response3.status_code == 409, 'unexpected result, it is supposed to 409 User has already exist'

        # clean test cases in db
        storage.delete_user(random_num1)
        storage.delete_user(random_num2)
        storage.delete_user(random_num3)
        storage.delete_user(random_num4)

    def test_delete_success(self):
        """Test successful scenario in delete method"""
        storage = Storage()
        random_num = random_number(6)
        url = parse.urljoin(BASE_URL, str(random_num))

        # prepare test case in db
        storage.add_anime_data(random_num, 'test', '1990-01-01', 'test', 'test', 'test')

        response = self.client.delete(url)
        assert response.status_code == 200, 'unable to delte user data'

        # clean test case in db
        storage.delete_user(random_num)

    def test_delete_failed(self):
        """Test Id not found scenario in delete method"""
        random_num = random_number(6)
        url = parse.urljoin(BASE_URL, str(random_num))
        response = self.client.delete(url)
        assert response.status_code == 404, 'unexpected result, it is supposed to 404 Id not found'
