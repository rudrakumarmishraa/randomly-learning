import requests

BASE = "http://127.0.0.1:5000/"
response = requests.put(BASE+"createUser", {"username":"rudra"})
print(response.json())