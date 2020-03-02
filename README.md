# api



## GET /init

#### Expected Payload
  
```
headers: Authorization: YOUR_TOKEN
```

#### Returns

```
{
  "room_id": 0,
  "title": "A Dark Room",
  "description": "You cannot see anything.",
  "coordinates": "(60,60)",
  "exits": ["n", "s", "e", "w"],
  "cooldown": 1.0,
  "errors": [],
  "messages": []
}
```
