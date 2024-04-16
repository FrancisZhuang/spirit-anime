"""Integrate https://animechan.vercel.app - request limit: 100 per hour"""

from urllib import parse

import requests

BASE_URL = 'https://animechan.vercel.app'
RANDOM_QUOTE = '/api/random'


class AnimeQuoteAPI:
    """Get anime quote"""
    @staticmethod
    def random_quote() -> str:
        """Get random anime quote"""
        url = parse.urljoin(BASE_URL, RANDOM_QUOTE)
        source = requests.get(url)
        assert source.status_code == 200, f'unable to fetch random anime quote: {source.text}'
        # todo: validate promise data structure

        return source.json().get('quote', '')
