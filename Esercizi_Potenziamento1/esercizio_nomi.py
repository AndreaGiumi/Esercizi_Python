
list_nomi: list[str] = []
while len(list_nomi) <= 30:
    nome: str = input("Inserisci un nome: ")
    if nome in list_nomi:
        raise KeyError("Il nome è già stato inserito!")
    if not nome or len(nome) > 20:
        raise KeyError("Errore! Il nome non può essere una stringa vuota o non deve superare i 20 caratteri.")
    list_nomi.append(nome)

print(list_nomi)
         
max_nome = max(list_nomi, key=len)

print(f"Il nome più lungo inserito nella lista è {max_nome}")
print(f"La lunghezza del nome è: {len(max_nome)}")


