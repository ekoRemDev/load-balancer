import requests

MAX_REQUESTS = 100
data = {}

for i in range(MAX_REQUESTS):
    res = requests.get('http://localhost:8000')
    id = res.json()["id"]
    print(id)
    if data.get(id):
        data[id] += 1
    else:
        data[id] = 1

print(data)
