# Create Spirit Anime

Update user full name or dob

**URL** : `/api/v1/spiritanim/{user_id}`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

```json
{
    "full_name": "francis",
    "dob": "1990-01-01"
}
```

Note that `full_name` and `dob` are optional fields.


## Success Response


**Code** : `200 OK`

**Content example**

```json
{
    "user_id": 911830,
    "full_name": "11sfdafd11111",
    "dob": "1294-02-11",
    "spirit_anime": {
        "name": "Africa no Salaryman",
        "quote": "Your name sounds like an air conditioner.",
        "favor_food": "https://foodish-api.herokuapp.com/images/biryani/biryani57.jpg"
    }
}
```