"""Integrate https://foodish-api.herokuapp.com"""


from urllib import parse

import requests

BASE_URL = 'https://foodish-api.herokuapp.com'
RANDOM_FOOD = '/api/'


class FoodDishAPI:
    """Get food dish"""
    @staticmethod
    def random_food() -> str:
        """Get random food dish picture"""
        url = parse.urljoin(BASE_URL, RANDOM_FOOD)
        source = requests.get(url)
        assert source.status_code == 200, f'unable to fetch random food dish: {source.text}'
        # todo: validate promise data structure

        return source.json().get('image', '')
