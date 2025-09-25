from pagamento_cartadi_credito import PagamentoCartaDiCredito
from pagamento_contanti import PagamentoContanti

pagamento1: PagamentoContanti = PagamentoContanti()
pagamento2: PagamentoContanti = PagamentoContanti()
pagamento3: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Mario Rossi","12/24", "5500-0000-0000-0004")
pagamento4: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Luigi Bianchi", "01/25", "5500-0000-0000-0004")



pagamento1.setImportoPagamento(150.00)
pagamento2.setImportoPagamento(95.25)
pagamento3.setImportoPagamento(200.00)
pagamento4.setImportoPagamento(500.00)



pagamento1.dettagliPagamento()
pagamento1.inPezziDa()

pagamento2.dettagliPagamento()

pagamento2.inPezziDa()

pagamento3.dettagliPagamento()
pagamento4.dettagliPagamento()




