# Classe Produto simples
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # Método para exibir informações do produto
    def exibir_info(self):
        print(f"Nome: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}")

    # Método para atualizar o preço e quantidade
    def atualizar_info(self, preco=None, quantidade=None):
        if preco:
            self.preco = preco
        if quantidade:
            self.quantidade = quantidade

# Exemplo de uso
produto = Produto("Caneta", 1.50, 100)
produto.exibir_info()
produto.atualizar_info(preco=2.00)
produto.exibir_info()

# Automatização com BotCity não é possível demonstrar diretamente aqui,
# mas seria uma automação para preencher formulário baseado nas informações do produto.
