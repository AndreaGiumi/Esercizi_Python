from typing import Any
pepole: list[dict[str, Any]] = [{"frist_name": "Andrea", "last_name": "Giumi", "age": 28, "city": "Cassino" }, {"frist_name": "Mirko", "last_name": "Capraro", "age": 25, "city": "Roma" }, {"frist_name": "Giovanni", "last_name": "Capraro", "age": 30, "city": "Firenze" }]

for dict in pepole:
    for values in dict.values():
        print({values})