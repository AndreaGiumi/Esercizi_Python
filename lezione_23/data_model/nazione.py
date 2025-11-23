from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from citta import Citta
class Nazione:
    _nome: str
    _citta: set[Citta]

    def __init__(self, nome: str)-> None:
        self.nome = nome
        self._citta = set()

    
    def get_nome(self) -> str:
        return self._nome
    
    # def set_nome(self, nome: str) -> None:
    #     self._nome = nome

    def citta(self) -> frozenset[Citta]:
        return frozenset(self._citta)
    
    def _add_citta(self, citta: Citta) -> None:
        self._citta.add(citta)

    def _remove_citta(self, citta: Citta) -> None:
        self._citta.remove(citta)


    def __str__(self):
        return f"Nazione {self._nome}"
    
    def __repr__(self):
        return f"Nazione(nome={self._nome})"
    
    def info(self) -> dict[str, str]:
        return {self.nome():
            {
                'nome': self.nome(),
            }
        }