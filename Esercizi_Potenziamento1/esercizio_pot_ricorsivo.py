from typing import Any
def printListBackward(lista: list[Any]) -> Any:
    if not lista:
        return 0

    print(lista.pop())
    printListBackward(lista)

lista = ["Ciao", 34, "pippo"]

printListBackward(lista)