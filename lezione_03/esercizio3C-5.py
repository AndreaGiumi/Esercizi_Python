accessi: dict[str, int] = {}

nome = str(input("Inserisci nome: ".title()))
accessi["nome"] = nome
ruolo = str(input("Inserisci ruolo: ".title()))
accessi["ruolo"] = ruolo
età = int(input("Inserisci età: "))
accessi["età"] = età

match accessi:
    # caso 1
    case {"nome": nome, "ruolo": "Admin", "età": eta}:
        print("Accesso completo a tutte le funzionalità.")
    # caso 2
    case {"nome": nome, "ruolo": "Moderatore", "età": eta}:
        print("Può gestire i contenuti ma non modificare le impostazioni.")
    # caso 3
    case {"nome": nome, "ruolo": "Utente adulto", "età": eta} if eta >= 18:
        print("Accesso standard a tutti i servizi.")
    # caso 4
    case {"nome": nome, "ruolo": "Utente minorenne", "età": eta} if eta < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    # caso 5
    case {"nome": nome, "ruolo": "Ospite", "età": eta}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    # caso default
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")
