# Show User Detail

Show user's full information

**URL** : `/api/v1/spiritanime/{user_id}`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data**: `{}`

## Success Response


**Code** : `200 OK`

**Content example**

```json
{
    "user_id": 276644,
    "full_name": "test2",
    "dob": "1990-01-01",
    "spirit_anime": {
        "name": "test2",
        "quote": "test2",
        "favor_food": "test2"
    }
}
```
