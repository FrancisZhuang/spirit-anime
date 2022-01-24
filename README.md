# Spirit Anime
We would like to provide a spirit anime generator to our user. They can register their own spirit anime with name and
dob. Enjoy it and have fun.

## Install
   pip install -r requirements.txt
## Run the app
   gunicorn --bind 0.0.0.0:5888 --workers 1 --threads 3 app:app
## Run the tests
   pytest


 # Open Endpoints

Open endpoints require no Authentication.

 * [Create Spirit Anime](doc/spirit_anime/put.md): `PUT /api/v1/spiritanime`
 * [Show All User Detail](doc/spirit_anime/get.md): `GET /api/v1/spiritanime`
 * [Show User Detail](doc/spirit_anime_detail/put.md): `GET /api/v1/spiritanime/{user_id}`
 * [Update User Detail](doc/spirit_anime_detail/post.md): `POST /api/v1/spiritanime/{user_id}`
 * [Delete User Detail]((doc/spirit_anime_detail/delete.md)): `DELETE /api/v1/spiritanime/{user_id}`



## System modules

```
 |--------|    |--------------|    |---------------|
 |        |--->|              |--->|               |
 |  USER  |    | Spirit Anime |    | External APIs |
 |        |<---|              |<---|               |
 |--------|    |--------------|    |---------------|

```

## Technical Used
* A web framework: Flask
* DB: SQLite
* Server host: AWS EC2

## System Limitation and improvement
* To achieve the business goal in short term, I use SQLite as a temporary DB. Once it is running smoothly, we can move to
  Postgres.
* Currently, the code is running in EC2 free tier, and it has 30 GB only.
* We can use flask_restful package "fields", it will give us a more readable resource structure.
* To ensure 3rd party APIs to provide the expected objects.
