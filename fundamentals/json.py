# JSON in Python
import json

# Parse JSON
joxos = '{"name": "Joxos", "health": 250, "stamina": 150, "atk":25, "items": ["Unity Stone"], "canFight": true}'
y = json.loads(joxos)
print(y["name"])

# Convert Python to JSON
a = {
    "name": "Joxos",
    "age": 30,
    "city": "Herl"
}

b = json.dumps(a)
print(b)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

c = json.dumps(a, indent=4, sort_keys=True)
print(c)