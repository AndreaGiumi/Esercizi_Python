'''
Esercizio 10

Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

    acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
    calcolare e visualizzare la somma di tutti i numeri pari inseriti;
    calcolare e visualizzare la media di tutti i numeri dispari inseriti;
    determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
    se più numeri hanno la stessa frequenza massima, visualizzarli tutti.

Esempio di input e output
Input:

Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0

Output:

Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: [4, 7] (2 volte)

'''

lista_num: list[int] = []

# inserimento numeri nella lista e controllo del numero sentinella (lo zero)
while True:
    numero: int = int(input("Inserire un numero(0 per terminare): "))

    if numero == 0:
        break
    else:
        lista_num.append(numero)

# somma dei numeri pari e media numeri dispari
somma_pari = 0
somma_disp = 0
count_disp = 0
for num in lista_num:
    if num % 2 == 0:
        somma_pari+= num
    else:
        somma_disp += num
        count_disp += 1
        media = somma_disp / count_disp

print(f"Somma dei numeri pari: {somma_pari}\nMedia dei numeri dispari: {media:.2f}")

# numero più frequente
frequenze: dict[int, int] = {}

for i in lista_num:
    frequenze[i] = 0
for j in lista_num:
    if j in frequenze:
        frequenze[j] += 1

max_val = max(frequenze.values())
max_freq: list[int] = []
for key, value in frequenze.items():
    if  value == max_val:
        max_freq.append(key)
print(f"Numero più frequente: {max_freq} ({max_val} volte)")