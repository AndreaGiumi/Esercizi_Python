# Esercizi di Ripasso Python

Esercizi in ordine crescente di difficoltà, basati sugli argomenti visti a lezione.
Per ogni sezione crea un file `.py` separato (es. `01_basi.py`, `02_cicli.py`, ...).

Legenda difficoltà: ⭐ facile · ⭐⭐ media · ⭐⭐⭐ difficile

---

## 1. Basi: variabili, input/output, condizioni ⭐

### Esercizio 1.1 — Saluto personalizzato
Chiedi all'utente nome ed età con `input()`. Stampa con una f-string:
`Ciao Andrea, tra 10 anni avrai 38 anni!`

### Esercizio 1.2 — Pari o dispari
Chiedi un numero intero e stampa se è pari o dispari. Se il numero è `0`, stampa un messaggio dedicato.

### Esercizio 1.3 — Convertitore di voti
Chiedi un voto da 0 a 100 e stampa la fascia corrispondente usando `if/elif/else`:
- 90-100 → "Eccellente"
- 70-89 → "Buono"
- 60-69 → "Sufficiente"
- sotto 60 → "Insufficiente"

Se il voto non è compreso tra 0 e 100, stampa "Voto non valido".

---

## 2. Cicli: while e for ⭐

### Esercizio 2.1 — Somma dei positivi
Con un ciclo `while`, chiedi 5 numeri all'utente e somma **solo quelli positivi**. Alla fine stampa la somma.

### Esercizio 2.2 — Tabellina
Chiedi un numero e stampa la sua tabellina da 1 a 10 usando `for` e `range()`.
Esempio di riga: `7 x 3 = 21`

### Esercizio 2.3 — Indovina il numero ⭐⭐
Il programma "pensa" un numero segreto (usa `random.randint(1, 50)`). L'utente ha 7 tentativi per indovinarlo: a ogni tentativo stampa "Troppo alto" o "Troppo basso". Se finisce i tentativi, stampa il numero segreto.

---

## 3. Liste e stringhe ⭐⭐

### Esercizio 3.1 — Analisi lista
Data la lista `numeri = [12, 5, 8, 21, 3, 16, 9]`, senza usare `min()`, `max()` o `sum()`:
- trova il valore minimo e il massimo
- calcola la media
- crea una nuova lista con i soli numeri maggiori della media

### Esercizio 3.2 — Palindromo
Scrivi un programma che chiede una parola e dice se è palindroma (uguale letta al contrario), ignorando maiuscole/minuscole. Prova sia con lo slicing `[::-1]` sia con un ciclo.

### Esercizio 3.3 — Matrice ⭐⭐⭐
Crea una matrice 3x3 (lista di liste) chiedendo i valori all'utente. Poi:
- stampala riga per riga in modo leggibile
- calcola la somma di ogni riga e di ogni colonna
- calcola la somma della diagonale principale

---

## 4. Dizionari ⭐⭐

### Esercizio 4.1 — Classifica pari/dispari
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario con due chiavi, `"pari"` e `"dispari"`, ognuna con la lista dei numeri corrispondenti.

### Esercizio 4.2 — Conta lettere
Data una frase, costruisci un dizionario che conta quante volte compare ogni lettera (ignora gli spazi). Stampa poi la lettera più frequente.

### Esercizio 4.3 — Rubrica telefonica ⭐⭐⭐
Crea una rubrica come dizionario `{nome: telefono}` con un menu testuale in un ciclo `while`:
1. Aggiungi contatto
2. Cerca contatto
3. Elimina contatto
4. Mostra tutti i contatti
5. Esci

Gestisci i casi di contatto già esistente o inesistente.

---

## 5. Funzioni ⭐⭐

### Esercizio 5.1 — Calcolatrice
Scrivi quattro funzioni (`somma`, `sottrazione`, `moltiplicazione`, `divisione`) con parametri tipizzati (es. `def somma(a: int, b: int) -> int:`). La divisione deve gestire il caso divisore uguale a zero. Poi crea un menu che chiede all'utente operazione e numeri.

### Esercizio 5.2 — Validatore password
Scrivi una funzione `valida_password(password: str) -> bool` che ritorna `True` solo se la password:
- è lunga almeno 8 caratteri
- contiene almeno una maiuscola
- contiene almeno un numero

### Esercizio 5.3 — Funzioni con valori di default ⭐⭐⭐
Scrivi una funzione `calcola_prezzo(prezzo_base: float, sconto: float = 0, iva: float = 22) -> float` che applica prima lo sconto (in percentuale) e poi aggiunge l'IVA. Testala chiamandola con 1, 2 e 3 argomenti, anche usando gli argomenti per nome (keyword arguments).

---

## 6. Ricorsione ⭐⭐

### Esercizio 6.1 — Fattoriale
Scrivi una funzione ricorsiva `fattoriale(n: int) -> int`. Ricorda il caso base!

### Esercizio 6.2 — Potenza ricorsiva
Scrivi `potenza(base: int, esponente: int) -> int` in modo ricorsivo, senza usare `**`.

### Esercizio 6.3 — Fibonacci ⭐⭐⭐
Scrivi una funzione ricorsiva che ritorna l'n-esimo numero di Fibonacci. Poi scrivi la stessa funzione in versione iterativa (con un ciclo) e confronta i tempi con `time.time()` per `n = 30`.

---

## 7. Lambda, map e filter ⭐⭐

### Esercizio 7.1 — Lambda base
Data la lista `numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`:
- usa `map()` con una lambda per ottenere i quadrati
- usa `filter()` con una lambda per tenere solo i multipli di 3

### Esercizio 7.2 — Ordinamento personalizzato
Data la lista di tuple `studenti = [("Anna", 28), ("Luca", 30), ("Marco", 25)]`, usa `sorted()` con `key=lambda ...` per ordinarla:
- per voto crescente
- per nome in ordine alfabetico

### Esercizio 7.3 — RegEx ⭐⭐⭐
Usando il modulo `re`:
- verifica se una stringa è un'email valida (formato semplice: `testo@testo.dominio`)
- estrai tutti i numeri da una frase tipo `"Ho comprato 3 mele e 12 arance a 5 euro"`

---

## 8. Eccezioni ⭐⭐

### Esercizio 8.1 — Radice sicura
Scrivi una funzione `safe_sqrt(numero)` che calcola la radice quadrata con `math.sqrt()` e gestisce con `try/except` il caso di numero negativo (`ValueError`), stampando l'errore.

### Esercizio 8.2 — Input robusto
Scrivi una funzione `chiedi_intero(messaggio: str) -> int` che continua a chiedere un input finché l'utente non inserisce un intero valido, gestendo il `ValueError`.

### Esercizio 8.3 — Eccezione personalizzata ⭐⭐⭐
Crea una classe `SaldoInsufficienteError(Exception)`. Scrivi una funzione `preleva(saldo: float, importo: float) -> float` che solleva l'eccezione con `raise` se l'importo supera il saldo. Gestiscila con `try/except/else/finally` e osserva quando viene eseguito ogni blocco.

---

## 9. Classi: basi ⭐⭐

### Esercizio 9.1 — Classe Libro
Crea una classe `Libro` con attributi `titolo`, `autore`, `pagine`. Implementa:
- il costruttore `__init__`
- il metodo `__str__` che ritorna una descrizione leggibile
- un metodo `is_lungo()` che ritorna `True` se ha più di 300 pagine

Crea 3 oggetti e stampali.

### Esercizio 9.2 — Classe Contatore con incapsulamento
Crea una classe `Contatore` con un attributo protetto `_conteggio`. Implementa `setZero()`, `add1()`, `sub1()` (che non deve mai andare sotto zero) e `getConteggio()`. Testa tutti i metodi.

### Esercizio 9.3 — Classe ContoBancario ⭐⭐⭐
Crea una classe `ContoBancario` con attributi protetti `_titolare` e `_saldo`. Implementa:
- `deposita(importo)` e `preleva(importo)` con controlli di validità (importi negativi, saldo insufficiente)
- getter per saldo e titolare
- una lista interna `_movimenti` che registra ogni operazione con una descrizione
- un metodo `estratto_conto()` che stampa tutti i movimenti

---

## 10. Classi: ereditarietà e polimorfismo ⭐⭐⭐

### Esercizio 10.1 — Persona e Studente
Crea una classe `Persona` con `nome`, `cognome`, `eta` e metodo `__str__`. Poi crea `Studente(Persona)` che aggiunge `matricola` e `corso`, richiama il costruttore padre con `super().__init__(...)` e ridefinisce `__str__`.

### Esercizio 10.2 — Forme geometriche con classe astratta
Usando `abc` (`ABC` e `@abstractmethod`), crea una classe astratta `FormaGenerica` con i metodi astratti `area()` e `perimetro()`. Implementa `Rettangolo`, `Cerchio` e `Triangolo`. Poi crea una lista di forme diverse e, con un unico ciclo `for`, stampa area e perimetro di ognuna (polimorfismo).

### Esercizio 10.3 — Gestionale dipendenti ⭐⭐⭐
Crea una classe astratta `Dipendente` con metodo astratto `calcola_stipendio()`. Implementa:
- `DipendenteFisso` (stipendio mensile fisso)
- `DipendenteOrario` (paga oraria × ore lavorate)
- `Manager(DipendenteFisso)` che aggiunge un bonus percentuale

Crea una classe `Azienda` che contiene una lista di dipendenti, con metodi per assumerli e per calcolare il costo totale mensile.

---

## 11. File e JSON ⭐⭐⭐

### Esercizio 11.1 — Lettura e scrittura file di testo
Scrivi un programma che:
- scrive su `diario.txt` tre righe di testo (usa `with open(...)`)
- rilegge il file e stampa ogni riga numerata
- aggiunge una riga in fondo senza cancellare il contenuto (modalità `a`)

### Esercizio 11.2 — Contatore di parole
Leggi un file di testo e stampa: numero di righe, numero di parole e la parola più frequente. Gestisci con `try/except` il caso di file inesistente (`FileNotFoundError`).

### Esercizio 11.3 — Salvataggio oggetti in JSON ⭐⭐⭐
Riprendi la classe `Libro` dell'esercizio 9.1 e aggiungi:
- un metodo `to_dict()` che ritorna un dizionario con gli attributi
- una funzione `salva_libreria(libri: list, percorso: str)` che salva la lista su file con `json.dump()`
- una funzione `carica_libreria(percorso: str) -> list` che legge il JSON con `json.load()` e ricostruisce gli oggetti `Libro`

---

## 12. Progetto finale: mini gestionale ⭐⭐⭐

### Esercizio 12.1 — Rifugio per animali (OOP + JSON)
Metti insieme tutto: crea un programma per gestire un rifugio per animali.
- Classe astratta `Animale` (nome, età, metodo astratto `verso()`), sottoclassi `Cane` e `Gatto`
- Classe `Rifugio` con metodi `aggiungi_animale()`, `adotta_animale(nome)`, `elenca_animali()`
- Persistenza: il rifugio si salva e si carica da un file `rifugio.json` (come nella lezione sul database mockup)
- Menu testuale con gestione delle eccezioni per gli input dell'utente

### Esercizio 12.2 — API Flask (facoltativo, ⭐⭐⭐)
Trasforma il rifugio in una piccola API Flask:
- `GET /animali` → ritorna la lista degli animali in JSON
- `GET /animali/<nome>` → ritorna un singolo animale (404 se non esiste)
- `POST /animali` → aggiunge un animale dal body JSON della richiesta
- `DELETE /animali/<nome>` → registra un'adozione

I dati devono restare salvati su `rifugio.json` anche dopo il riavvio del server.

---

## Consigli per il ripasso

- Usa sempre i **type hints** come hai fatto negli esercizi delle lezioni (`def somma(a: int, b: int) -> int:`)
- Prima di guardare soluzioni vecchie, prova a scrivere tutto da zero
- Testa ogni esercizio con casi limite: liste vuote, numeri negativi, input sbagliati
- Fai un commit dopo ogni sezione completata
