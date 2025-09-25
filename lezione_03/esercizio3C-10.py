day: int = int(input("Inserisci giorno del mese: "))
month: int = int(input("Inserisci mese: "))

festa: tuple[str, int] = ()
giorni_per_mese: list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

festa = festa + (day, month)

match festa:
    case (day, month) if day <= 0 or month <= 0:
        print("Inserire un valore positivo per il giorno e per il mese!")
    case (1, 1):
        print("Il 1/01 è Capodanno!")
    case (14, 2):
        print("Il 14/02 è San Valentino!")
    case (2, 6):
        print("Il 2/02 è Festa della Repubblica Italiana!")
    case (15, 8):
        print("Il 15/08 è Ferragosto!")
    case (31, 10):
        print("Il 31/10 è Halloween!")
    case (25, 12):
        print("Il 25/12 è Natale!")
    case(day, month) if month > 12 or day > giorni_per_mese[month-1]:
        print(f"Il {day}/{month} non esiste!")
    case _:
        print("Nessuna festività importante in questa data.")