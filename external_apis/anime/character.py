"""Integrate https://api.aniapi.co - request limit: 90 per minute"""
from urllib import parse

import requests

# request limit: 90 per minute
BASE_URL = 'https://api.aniapi.com'
RANDOM_CHARACTER = '/v1/random/anime'


class AnimeCharacterAPI:
    """Get anime character"""
    def __init__(self, api_token):
        self.__api_token = api_token

    def random_character(self) -> str:
        """Get random anime character name"""

        count = 1
        nsfw = True
        url = parse.urljoin(BASE_URL, f'{RANDOM_CHARACTER}/{count}/{nsfw}')
        source = requests.get(url, headers={'Authorization': self.__api_token})
        assert source.status_code == 200, f'unable to fetch random anime character: {source.text}'
        # todo: validate promise data structure
        anime = source.json().get('data', [])
        anime_title = anime[0].get('titles', '')

        return anime_title.get('en', '')
