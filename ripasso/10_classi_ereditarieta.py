"""
Sezione 10 - Classi: ereditarietà e polimorfismo (difficoltà: difficile)

Completa ogni esercizio dove trovi il commento # TODO.
"""

from abc import ABC, abstractmethod


# Esercizio 10.1 - Persona e Studente
# Persona: nome, cognome, eta, __str__.
# Studente(Persona): aggiunge matricola e corso, richiama super().__init__(...)
# e ridefinisce __str__.
class Persona:
    def __init__(self, nome: str, cognome: str, eta: int) -> None:
        # TODO
        pass

    def __str__(self) -> str:
        # TODO
        pass


class Studente(Persona):
    def __init__(self, nome: str, cognome: str, eta: int, matricola: str, corso: str) -> None:
        # TODO: super().__init__(...)
        pass

    def __str__(self) -> str:
        # TODO
        pass


# Esercizio 10.2 - Forme geometriche con classe astratta
# FormaGenerica astratta con area() e perimetro() astratti.
# Implementa Rettangolo, Cerchio, Triangolo. Con un unico for su una lista
# di forme diverse stampa area e perimetro (polimorfismo).
class FormaGenerica(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimetro(self) -> float:
        ...


class Rettangolo(FormaGenerica):
    # TODO
    pass


class Cerchio(FormaGenerica):
    # TODO
    pass


class Triangolo(FormaGenerica):
    # TODO
    pass


# Esercizio 10.3 - Gestionale dipendenti (difficile)
# Dipendente astratto con calcola_stipendio() astratto.
#   - DipendenteFisso (stipendio mensile fisso)
#   - DipendenteOrario (paga oraria * ore lavorate)
#   - Manager(DipendenteFisso) con bonus percentuale
# Azienda: lista di dipendenti, assumi(), costo_totale_mensile().
class Dipendente(ABC):
    @abstractmethod
    def calcola_stipendio(self) -> float:
        ...


# TODO: DipendenteFisso, DipendenteOrario, Manager, Azienda


if __name__ == "__main__":
    # TODO: crea gli oggetti e testa il polimorfismo
    pass
