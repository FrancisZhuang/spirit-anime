"""This app provides two Spirit Anime APIs"""

import os
import json
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

from external_apis.anime.character import AnimeCharacterAPI
from external_apis.anime.quote import AnimeQuoteAPI
from external_apis.food.foodish import FoodDishAPI
from utils.validator import valid_put_payload
from utils.validator import valid_post_payload
from utils.storage import Storage
from utils.random_num import random_number

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to Spirit Anime Maker'


class SpiritAnime(Resource):
    """/api/v1/spiritanime Restful API"""
    def __init__(self):
        self.current_path = os.getcwd()
        self.storage = Storage()

    def get(self):
        """get all user id and full name"""
        user_list = []
        result = {'users': user_list}
        user_infos = self.storage.get_all_id_name()
        for user_id, full_name in user_infos:
            user_data = {'user_id': user_id, 'full_name': full_name}
            user_list.append(user_data)
        return result, 200

    def put(self):
        """create user by full name and dob"""
        anime_put_args = reqparse.RequestParser()
        args = valid_put_payload(anime_put_args)
        config_path = os.path.join(self.current_path, 'utils/env.json')
        with open(config_path, encoding='utf-8') as json_file:
            config = json.load(json_file)
        anime_char = AnimeCharacterAPI(config['anime_token'])
        random_char = anime_char.random_character()
        anime_quote = AnimeQuoteAPI()
        random_quote = anime_quote.random_quote()
        food_dish = FoodDishAPI()
        random_food = food_dish.random_food()
        if args['dob'] == 'Expect dob format: yyyy-mm-dd':
            return args, 400
        check_user_name = self.storage.has_user_name_dob(args['full_name'], args['dob'])
        if check_user_name:
            abort(409, message='User has already exist...')
        user_id = random_number(6)
        self.storage.add_anime_data(user_id,
                                    args['full_name'],
                                    args['dob'],
                                    random_char,
                                    random_quote,
                                    random_food)
        spirit_anime = {'name': random_char, 'quote': random_quote, 'favor_food': random_food}
        args['user_id'] = user_id
        args['spirit_anime'] = spirit_anime

        return args, 201


class SpiritAnimeDetail(Resource):
    """/api/v1/spiritanime/<int:user_id> Restful API"""

    def __init__(self):
        self.storage = Storage()

    def get(self, user_id):
        """get user data by id"""
        check_exist = self.storage.has_user_id(user_id)
        if not check_exist:
            abort(404, message="Id not found...")
        user_info = self.storage.get_info_by_id(user_id)
        result = {'user_id': user_info[0],
                  'full_name': user_info[1],
                  'dob': user_info[2],
                  "spirit_anime": {
                      "name": user_info[3],
                      "quote": user_info[4],
                      "favor_food": user_info[5]
                  },
                  }

        return result, 200

    def post(self, user_id):
        """allow to update user name and dob only"""
        anime_put_args = reqparse.RequestParser()
        args = valid_post_payload(anime_put_args)
        check_exist = self.storage.has_user_id(user_id)
        if not check_exist:
            abort(404, message="Id not found...")
        original_info = self.storage.get_info_by_id(user_id)
        original_dob = original_info[2]
        original_full_name = original_info[1]

        if args['full_name'] and args['dob']:
            check_user_name = self.storage.has_user_name_dob(args['full_name'], args['dob'])
            if check_user_name:
                abort(409, message='User has already exist...')
            self.storage.update_full_name(args['full_name'], args['dob'])
        if args['full_name']:
            check_user_name = self.storage.has_user_name_dob(args['full_name'], original_dob)
            if check_user_name:
                abort(409, message='User has already exist...')
            self.storage.update_full_name(args['full_name'], user_id)
        if args['dob']:
            check_user_name = self.storage.has_user_name_dob(original_full_name, args['dob'])
            if check_user_name:
                abort(409, message='User has already exist...')
            self.storage.update_dob(args['dob'], user_id)
        user_info = self.storage.get_info_by_id(user_id)
        result = {'user_id': user_info[0],
                  'full_name': user_info[1],
                  'dob': user_info[2],
                  "spirit_anime": {
                      "name": user_info[3],
                      "quote": user_info[4],
                      "favor_food": user_info[5]
                  },
                  }

        return result, 200

    def delete(self, user_id):
        """delete user data by id"""
        check_exist = self.storage.has_user_id(user_id)
        if not check_exist:
            abort(404, message="Id not found...")
        self.storage.delete_user(user_id)

        return 'Id delete successfully', 200


api.add_resource(SpiritAnime, "/api/v1/spiritanime")
api.add_resource(SpiritAnimeDetail, "/api/v1/spiritanime/<int:user_id>")

if __name__ == "__main__":
    app.run()
