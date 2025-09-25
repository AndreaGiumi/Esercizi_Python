def frequenzimetro(word: str) -> dict[str, int]:

    
    '''
    Scrivi una funzione che, data una stringa come parametro,
      restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.

    Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}
    '''
    freq: dict[str, int] = {}

    for char in word:
      freq[char.lower()] = 0
    for char in word:
        if char.lower() in freq:
            freq[char.lower()] += 1
                


    print(freq)


frequenzimetro("cciiiao")