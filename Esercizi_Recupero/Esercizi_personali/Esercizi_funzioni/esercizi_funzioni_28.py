from typing import Any
def segreteria(scuola: list[dict[str, Any]]) -> None:
    # Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola. Ogni dizionario rappresenta uno studente e contiene nome, cognome, 
    # classe e voti. La funzione deve stampare un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno
    for stud in scuola:
        media_voti = sum(stud["Voti"]) / float(len(stud["Voti"]))
        stud["Media voti"] = media_voti

        print(stud)


    

if __name__=="__main__":

    scuola: list[dict[str, Any]] = [{"Nome":"Andrea","Cognome": "Giumi","Classe": 5, "Voti":[6.5, 4.5, 7, 8]}, {"Nome":"Luca","Cognome": "Bianchi","Classe": 4, "Voti":[6, 3.5, 4, 5.5]}]

    segreteria(scuola)