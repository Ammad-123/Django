import requests

URL = 'http://127.0.0.1:8000/stdinfo/'

res = requests.get(url = URL)
print(res)
data = res.json()

print(data)
