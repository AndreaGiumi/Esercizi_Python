from typing import Callable

numeri_pari:Callable = lambda x: "Pari" if x % 2 == 0 else "Dispari"


print(numeri_pari(24))
print(numeri_pari(21))