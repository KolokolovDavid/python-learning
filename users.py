users = {
    1: {"name": "David", "age": 17},
    2: {"name": "Аня", "age": 20},
}

print(users[1]["age"])
users[2]["age"] = 21
print(users[2])
users[3] = {"name": "Борис", "age": 25}
print(len(users))