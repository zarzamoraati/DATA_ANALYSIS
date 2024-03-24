import requests
import json

print(dir(requests))

obj_res=requests.get("https://jsonplaceholder.typicode.com/users")

data=obj_res.json()

for user in data:
    print(user["name"])
    print(user["username"])
    print(user["email"])
    