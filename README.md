# api



## GET /init

#### Expected Payload
  
```
headers: Authorization: YOUR_TOKEN
```

#### Returns

```
{
    "cooldown": 1.0,
    "coordinates": "(60,60)",
    "description": "You are standing in the center of a brightly lit room. You notice a shop to the west and exits to the north, south and east.",
    "elevation": 0,
    "errors": [],
    "exits": [
        "n",
        "s",
        "e",
        "w"
    ],
    "items": [],
    "messages": [],
    "players": [
        "User 2079843",
        ....
    ],
    "room_id": 0,
    "terrain": "NORMAL",
    "title": "A brightly lit room"
}
```
