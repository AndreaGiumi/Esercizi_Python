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

---

## Ripasso errori commessi

Diario degli errori fatti durante gli esercizi, da rileggere prima di rifare una sezione.
Ci sono due tipi di voce:
- **Errori comuni / attenzione** (Sezioni 1-4): trappole tipiche e punti su cui stare attento, scritti in generale perché questi esercizi non li abbiamo rivisti insieme.
- **Errori osservati** (dalla Sezione 5 in poi): sbagli reali fatti nel codice, con schema *cosa ho sbagliato → perché è un errore → regola da ricordare*.

### Sezione 1 — Basi (errori comuni / attenzione)

- **`input()` restituisce sempre una stringa.** Per fare calcoli o confronti numerici devi convertire con `int()` / `float()`. Dimenticarlo porta a errori (`"10" + 10`) o a confronti sbagliati.
- **f-string senza la `f`.** Se scrivi `"Ciao {nome}"` senza la `f` davanti, le graffe restano testo letterale e non vengono sostituite.
- **Pari/dispari (1.2):** usa il resto `% 2`. Ricorda che `0` è pari, ma l'esercizio chiede un messaggio dedicato → controlla il caso `0` **prima** del pari/dispari.
- **Fasce di voto (1.3):** usa `elif` (non tanti `if` separati, che si sovrappongono) e cura l'ordine delle soglie. Attento ai bordi (90-100 include il 100?) e valida il range 0-100 prima di assegnare la fascia.
- **`/` vs `//`:** la divisione normale dà sempre un `float`; usa `//` solo se vuoi il quoziente intero.

### Sezione 2 — Cicli (errori comuni / attenzione)

- **Ciclo infinito nel `while`.** Devi aggiornare dentro il ciclo la variabile che controlla la condizione, altrimenti non finisce mai.
- **`range()` esclude l'estremo superiore.** `range(1, 10)` arriva a 9. Per la tabellina 1-10 serve `range(1, 11)`. Fonte tipica di errori "off-by-one".
- **Accumulatori inizializzati fuori dal ciclo.** La somma/il contatore vanno messi a `0` **prima** del `for`/`while`, non dentro (altrimenti si azzerano ad ogni giro).
- **Somma dei positivi (2.1):** non confondere "quante volte chiedo un numero" (5 iterazioni) con "quali sommo" (solo se `> 0`; lo `0` non è positivo).
- **Indovina il numero (2.3):** converti l'input in `int`; esci dal ciclo con `break` appena indovina; mostra il numero segreto **solo** a tentativi esauriti. Conta bene i tentativi (attento all'off-by-one).

### Sezione 3 — Liste e stringhe (errori comuni / attenzione)

- **Gli indici partono da 0.** L'ultimo elemento è `lista[len(lista) - 1]` oppure `lista[-1]`; `lista[len(lista)]` dà `IndexError`.
- **Min/max manuale (3.1):** inizializza il minimo e il massimo con il **primo elemento della lista**, non con `0`. Se parti da `0` sbagli con liste di soli negativi (o soli positivi). Per la media attento a `/` vs `//`.
- **Palindromo (3.2):** normalizza con `.lower()` (ed eventualmente togli spazi) prima di confrontare. Ricorda che `s[::-1]` inverte la stringa.
- **Le stringhe sono immutabili.** Non puoi fare `s[0] = "x"`; devi costruire una nuova stringa.
- **Matrice (3.3):** NON creare la griglia con `[[0] * 3] * 3` → crea 3 riferimenti alla **stessa** riga, modificarne una le cambia tutte. Usa una list comprehension. Accedi con `m[riga][colonna]`.
- **Non modificare una lista mentre la si scorre** (aggiunte/rimozioni durante il `for` danno comportamenti imprevisti).

### Sezione 4 — Dizionari (errori comuni / attenzione)

- **Chiave inesistente con `dict[chiave]` → `KeyError`.** Prima controlla con `in`, oppure usa `dict.get(chiave, default)`.
- **Conta lettere (4.2):** il pattern comodo è `conteggio[c] = conteggio.get(c, 0) + 1`. Ricorda di ignorare gli spazi e decidi se contare maiuscole e minuscole come uguali (`.lower()`).
- **Lettera più frequente:** si trova con `max(conteggio, key=conteggio.get)`; non confondere la chiave (lettera) con il valore (conteggio).
- **Iterazione:** `.items()` dà coppie `(chiave, valore)`, `.keys()` le chiavi, `.values()` i valori. Scegliere quello sbagliato è un errore frequente.
- **Rubrica (4.3):** prima di aggiungere/cercare/eliminare gestisci il caso "già esistente" o "inesistente". `del dict[k]` su una chiave assente dà errore → controlla prima.

### Sezione 5 — Funzioni (rivisto il 2026-07-18)

**5.1 — `divisione`: tipo di ritorno incoerente**
- *Cosa*: annotazione `-> float | None`, ma in caso di divisore 0 restituivo la stringa `"Errore divisione per 0"`.
- *Perché*: il valore restituito (`str`) non rispetta il tipo dichiarato; chi legge la firma si aspetta un numero o `None`, non testo.
- *Regola*: l'annotazione di ritorno deve combaciare con **tutti** i possibili valori restituiti. O includi `str` nel tipo, o restituisci `None`/sollevi un errore e gestisci il messaggio fuori dalla funzione.

**5.2 — `valida_password`: `return` dentro il ciclo (errore principale)**
- *Cosa*: sia `return True` sia `return False` erano dentro il `for`, quindi la funzione decideva tutto sul **primo carattere** ed usciva subito.
- *Perché*: per verificare "esiste almeno un carattere che…" devi guardare **tutta** la stringa prima di decidere.
- *Regola*: nei controlli "esiste almeno uno…" usa dei **flag** booleani, accendili dentro il ciclo, e metti il `return` finale **fuori** dal ciclo.

**5.2 — `valida_password`: confronti sbagliati sui caratteri**
- *Cosa*: `i == i.isalnum()` (confronto tra una stringa e un booleano → sempre `False`) e `i == i.capitalize()` per "cercare la maiuscola".
- *Perché*: `.isalnum()`/`.isupper()`/`.isdigit()` restituiscono **già** `True`/`False`, vanno usati direttamente in un `if`, non confrontati con il carattere. E `.capitalize()` non serve a sapere se un carattere è maiuscolo.
- *Regola*: usa i metodi giusti — `.isupper()` per la maiuscola, `.isdigit()` per la cifra — dentro l'`if`, senza `i == ...`.

**5.2 — `valida_password`: tre condizioni in un solo `and` su un carattere**
- *Cosa*: `if maiuscola and numero and lunghezza` valutato su ogni singolo carattere.
- *Perché*: un carattere non può essere **contemporaneamente** maiuscola *e* cifra, quindi quell'`and` non è mai vero. Le tre condizioni riguardano l'intera password, non il singolo carattere.
- *Regola*: condizioni indipendenti → flag separati, combinati con `and` **alla fine**. La lunghezza si controlla una volta sola, fuori dal ciclo.

**5.3 — `calcola_prezzo`: virgola al posto del punto nei decimali**
- *Cosa*: `tot_con_sconto * 1,22`.
- *Perché*: in Python la virgola crea una **tupla**: `x * 1,22` viene letto come `(x * 1, 22)`. Il separatore decimale è il **punto**.
- *Regola*: i decimali si scrivono con il punto (`1.22`). Se una funzione "restituisce una coppia" senza motivo, sospetta una virgola di troppo.

**5.3 — `calcola_prezzo`: valore "murato" invece del parametro**
- *Cosa*: IVA fissa a `1.22` invece di usare il parametro `iva`.
- *Perché*: così i valori di default e i keyword argument (`iva=4`) venivano ignorati — proprio lo scopo dell'esercizio.
- *Regola*: costruisci il moltiplicatore **dal parametro** (`1 + iva / 100`), come già facevi con lo sconto (`sconto / 100`).

**Nota trasversale (stile)**
- `if condizione: return True` / `return False` si può scrivere direttamente `return condizione`, perché l'espressione è già un booleano.
- Attento ai `float`: risultati tipo `109.80000000000001` sono normali; per i soldi "veri" esiste il modulo `decimal`.

### Sezione 6 — Ricorsione (rivisto il 2026-07-19)

**6.3 — `fibonacci_ricorsivo`: secondo addendo con `n - 1` invece di `n - 2`**
- *Cosa*: `return fibonacci_ricorsivo(n - 1) + fibonacci_ricorsivo(n - 1)` (stesso termine due volte).
- *Perché*: sommare due volte `fib(n-1)` equivale a `2 * fib(n-1)`, quindi la funzione raddoppia ad ogni passo e produce le potenze di 2 (`1, 2, 4, 8, ...`), non la sequenza di Fibonacci (`1, 1, 2, 3, 5, ...`). Il "trucco" di Fibonacci è che i due addendi sono **diversi**.
- *Regola*: attieniti alla definizione `fib(n) = fib(n-1) + fib(n-2)`. I due termini ricorsivi devono essere sfalsati (uno indietro di 1, l'altro di 2).

**6.3 — `fibonacci_iterativo`: off-by-one nel ciclo + variabile di ritorno sbagliata**
- *Cosa*: `for i in range(n + 1)` con `return b` → la funzione restituiva `fib(n + 2)` invece di `fib(n)` (es. `fibonacci_iterativo(5)` dava `13` invece di `5`).
- *Perché*: partendo da `a = 0`, `b = 1`, dopo `k` giri si ha `a = fib(k)` e `b = fib(k+1)`. Con `n + 1` giri e restituendo `b` si finisce due posizioni troppo avanti.
- *Regola*: servono esattamente `n` giri (`range(n)`) e il risultato è in `a` → `return a`. Verifica **sempre** con un caso piccolo a mano (`n = 0`, `n = 1`, `n = 5`) per scovare gli off-by-one prima di fidarti del codice.

**Nota trasversale (concetto)**
- Ricorsione ingenua vs iterazione: la versione ricorsiva di Fibonacci è O(2ⁿ) perché ricalcola più volte gli stessi valori (~2,7 milioni di chiamate per `n = 30`), mentre quella iterativa è O(n) (30 giri). Stessa formula, costo enormemente diverso: la ricorsione è elegante ma non sempre efficiente.
- Se la variabile del `for` non la usi (conti solo le iterazioni), la convenzione è chiamarla `_` invece di `i`.
- Per unire eleganza ricorsiva ed efficienza esiste la *memoizzazione* (ricorsione + cache dei risultati già calcolati) → argomento per il futuro.
