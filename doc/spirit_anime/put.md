# Create Spirit Anime

Create user with random spirit anime

**URL** : `/api/v1/spiritanim`

**Method** : `PUT`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

```json
{
    "full_name": "francis",
    "dob": "1990-01-01"
}
```

Note that `full_name` and `dob` are required fields.


## Success Response


**Code** : `201 CREATED`

**Content example**

```json
{
    "full_name": "23dfa1",
    "dob": "1994-02-11",
    "user_id": 911830,
    "spirit_anime": {
        "name": "Africa no Salaryman",
        "quote": "Your name sounds like an air conditioner.",
        "favor_food": "https://foodish-api.herokuapp.com/images/biryani/biryani57.jpg"
    }
}
```