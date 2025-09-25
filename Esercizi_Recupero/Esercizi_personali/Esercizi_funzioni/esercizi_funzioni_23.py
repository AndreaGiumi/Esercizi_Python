def tempo(giorni: int, ore: int, minuti: float) -> float:
    "Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi."
    conv_secondi = {}

    conv_secondi["giorni"] = (giorni * 24) * 3600
    conv_secondi["ore"] = ore * 3600
    conv_secondi["minuti"] = minuti * 60

    print(f"{giorni} giorno/i, {ore} ore, {minuti} minuto/i diventano: ")

    for key, value in conv_secondi.items():
        print(f"{key} : {value}")


tempo(2,15,50)