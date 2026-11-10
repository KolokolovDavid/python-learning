import json
about_me = {"name": "David", "age": 17, "profession":"Programmer"}
with open("about_me.json", "w", encoding="utf-8") as f:
    json.dump(about_me, f, ensure_ascii=False, indent=4)
try:
    with open("about_me2.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for key, value in data.items():
        print(f"{key}: {value}")
except FileNotFoundError:
    print("Файл не найден")
