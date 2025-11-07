def calculate_std_dev(nums: list[float]) -> float:
    '''
    che, data una lista di numeri,
    ritorni la deviazione standard (radice quadrata della varianza). Se la lista è vuota, solleva
    un’eccezione ValueError con messaggio "lista vuota". Attenzione: non usare funzioni
    built-in di python o librerie.

    Nota Bene: Il calcolo della varianza misura la dispersione dei dati rispetto alla media. Si
    calcola come la media dei quadrati delle differenze tra ciascun valore all’interno della lista e
    la media dei valori della lista di numeri
    Esempio:
    Se nums = [1.0, 2.0, 3.0, 4.0, 5.0]:
    1. Calcolo della media:
    (1.0 + 2.0 + 3.0 + 4.0 + 5.0) / 5 = 15.0 / 5 = 3.0
    2. Calcolo della varianza:
    ((1.0 - 3.0)^2 + (2.0 - 3.0)^2 + (3.0 - 3.0)^2 + (4.0 - 3.0)^2 + (5.0 - 3.0)^2) / 5
    = ((-2.0)^2 + (-1.0)^2 + (0.0)^2 + (1.0)^2 + (2.0)^2) / 5
    = (4.0 + 1.0 + 0.0 + 1.0 + 4.0) / 5
    = 10.0 / 5 = 2.0
    3. Calcolo della deviazione standard:
    radice quadrata di 2.0 ≈ 1.41421356
    '''
    if not nums:
        raise ValueError("lista vuota")
    somma = 0

    for i in nums:
        somma += i
    media = somma / len(nums)
    somma = 0

    for num in nums:
        var = (num - media)**2
        somma += var
    result = somma / len(nums)

    return result ** 0.5



    
        
if __name__== "__main__":
    lista = [1, 2, 3, 4, 5]
    print(calculate_std_dev(lista))   


