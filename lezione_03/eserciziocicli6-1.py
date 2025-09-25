from typing import Any

person: dict[str, Any] = {"frist_name": "Andrea", "last_name": "Luca", "age": 28, "city": "Cassino" }

for value in person.values():
    print(value)