from gestionale_pagamento.pagamento import Pagamento
import re
class PagamentoCartaDiCredito(Pagamento):

    '''
    Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
    Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito.
      Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.
    
    '''
    __nome_titolare: str
    __data_scadenza: str
    __numero_carta: str

    def __init__(self, nome_titolare: str, data_scadenza: str, numero_carta: str):
        super().__init__()

        self.setTitolare(nome_titolare)
        self.setDataScadenza(data_scadenza)
        self.setNumeroCarta(numero_carta)

    def setTitolare(self, nome_titolare: str) -> None:
        self.__nome_titolare = nome_titolare

    
    def getTitolare(self) -> str:
        return self.__nome_titolare
    

    def setDataScadenza(self, data_scadenza: str) -> None:
        self.__data_scadenza = data_scadenza

    
    def getDataScadenza(self) -> str:
        return self.__data_scadenza
    
    def setNumeroCarta(self, numero_carta: str) -> None:
        if not re.match(r"^(?=.{13,31}$)\d{1,4}(?:[ -]?\d{1,4}){2,6}$", numero_carta):
            raise ValueError("Inserisci numero di carta valido!")
        self.__numero_carta = numero_carta

    def getNumeroCarta(self) -> str:
        return self.__numero_carta
    

    def dettagliPagamento(self):
        print(f"Pagamento di: €{self.getImportoPagamento() }effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.getTitolare()}\nData di scadenza: {self.getDataScadenza()}\nNumero della carta: {self.getNumeroCarta()}")