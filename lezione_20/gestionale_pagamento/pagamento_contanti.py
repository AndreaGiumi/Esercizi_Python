from gestionale_pagamento.pagamento import Pagamento

class PagamentoContanti(Pagamento):

    '''
    Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo.
    Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti.
    Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote
    da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete
     da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie
    per pagare l'importo in contanti.
    
    '''

    def __init__(self):
        super().__init__()


    def dettagliPagamento(self):
        print(f"Pagamento in contanti di €{self.getImportoPagamento()}")
        print(f"{self.getImportoPagamento()} euro da pagare in contanti con: ")

    
    def inPezziDa(self) -> None:
        tagli: list[int] = [
            500.00,
            200.00,
            100.00,
            50.00,
            20.00,
            10.00,
            5.00,
            2.00,
            1.00,
            0.50,
            0.20,
            0.10
        ]
        pagamento: float = self.getImportoPagamento()

        
        for taglio in tagli:
            volte = int(pagamento // taglio)
            pagamento -= taglio * volte         
            if volte > 0:
                print(f"{volte} banconote da {taglio:.2f}")

    
