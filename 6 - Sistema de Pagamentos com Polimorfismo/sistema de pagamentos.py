# Classe base Pagamento
class Pagamento:
    def processar_pagamento(self):
        pass

# Subclasse PagamentoCartaoCredito
class PagamentoCartaoCredito(Pagamento):
    def __init__(self, numero_cartao):
        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        print(f"Pagamento processado com cartão de crédito: {self.numero_cartao}")

# Subclasse PagamentoBoleto
class PagamentoBoleto(Pagamento):
    def __init__(self, codigo_boleto):
        self.codigo_boleto = codigo_boleto

    def processar_pagamento(self):
        print(f"Pagamento processado com boleto: {self.codigo_boleto}")

# Subclasse PagamentoPix
class PagamentoPix(Pagamento):
    def __init__(self, chave_pix):
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        print(f"Pagamento processado via Pix: {self.chave_pix}")

# Função processar que aceita qualquer tipo de pagamento
def processar(pagamento):
    pagamento.processar_pagamento()

# Testando o polimorfismo
cartao = PagamentoCartaoCredito("1234-5678-9101")
boleto = PagamentoBoleto("987654321")
pix = PagamentoPix("chave-pix")

processar(cartao)
processar(boleto)
processar(pix)
