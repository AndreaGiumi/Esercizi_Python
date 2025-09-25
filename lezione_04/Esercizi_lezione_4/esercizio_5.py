from typing import Any
inventory: list[Any]
def  InventoryManagementSystem(code:str, name:str, quantity:int, price:float):
    return {
        "Codice": code,
        "Nome": name,
        "Quantità": quantity,
        "Prezzo": price
          }
def add_inventory(item:dict[str, Any], inventory:list[dict[str, Any]]):
    return inventory.append(item)

def remuve_inventory(item: str, inventory:list[dict[str, Any]]):
    updated_inventory: list[dict[str, Any]] = []
    for p in inventory:
        if p["name"] != item:
            updated_inventory.append(p)
        return updated_inventory


item1: dict[str, Any] = InventoryManagementSystem("2652d21", "cosa", 12, 12.5)
item2: dict[str, Any] = InventoryManagementSystem("142d54", "cosa1", 1, 21)

print(item1, item2)

inventory: list[dict[str, Any]] = []

add_inventory(item1, inventory)
add_inventory(item2, inventory)

print(inventory)

remuve_inventory(inventory, item1)

print(inventory)


