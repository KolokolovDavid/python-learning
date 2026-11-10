import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)
if response.status_code == 200:
    data = response.json()
    print(data["name"])
    print(data["email"])
    print(type(data))
else:
    print("Ошибка:", response.status_code)