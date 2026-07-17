"""
Sezione 12 - Progetto finale: rifugio per animali (difficoltà: difficile)

Metti insieme OOP + JSON (+ Flask facoltativo).
Completa ogni parte dove trovi il commento # TODO.
"""

import json
from abc import ABC, abstractmethod


# Esercizio 12.1 - Rifugio per animali
# Animale astratto (nome, eta, verso() astratto), sottoclassi Cane e Gatto.
# Rifugio: aggiungi_animale(), adotta_animale(nome), elenca_animali().
# Persistenza su rifugio.json. Menu testuale con gestione eccezioni.
class Animale(ABC):
    def __init__(self, nome: str, eta: int) -> None:
        self.nome = nome
        self.eta = eta

    @abstractmethod
    def verso(self) -> str:
        ...

    def to_dict(self) -> dict:
        # TODO: includi il tipo per poter ricostruire l'oggetto giusto
        pass


class Cane(Animale):
    def verso(self) -> str:
        # TODO
        pass


class Gatto(Animale):
    def verso(self) -> str:
        # TODO
        pass


class Rifugio:
    def __init__(self) -> None:
        self._animali: list[Animale] = []

    def aggiungi_animale(self, animale: Animale) -> None:
        # TODO
        pass

    def adotta_animale(self, nome: str) -> None:
        # TODO
        pass

    def elenca_animali(self) -> None:
        # TODO
        pass

    def salva(self, percorso: str = "rifugio.json") -> None:
        # TODO: json.dump della lista di to_dict()
        pass

    def carica(self, percorso: str = "rifugio.json") -> None:
        # TODO: json.load e ricostruzione di Cane/Gatto in base al tipo
        pass


def menu() -> None:
    # TODO: ciclo del menu con try/except sugli input
    pass


# Esercizio 12.2 - API Flask (facoltativo)
# GET  /animali          -> lista animali in JSON
# GET  /animali/<nome>   -> singolo animale (404 se non esiste)
# POST /animali          -> aggiunge un animale dal body JSON
# DELETE /animali/<nome> -> registra un'adozione
# I dati restano su rifugio.json anche dopo il riavvio del server.
#
# Suggerimento: from flask import Flask, jsonify, request


if __name__ == "__main__":
    menu()
