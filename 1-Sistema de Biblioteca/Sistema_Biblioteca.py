# Classe que modela um sistema de biblioteca
class Biblioteca:
    def __init__(self):
        self.inventario = {}

    # Método para adicionar livros ao inventário
    def adicionar_livro(self, titulo, quantidade):
        if titulo in self.inventario:
            self.inventario[titulo] += quantidade
        else:
            self.inventario[titulo] = quantidade

    # Método para emprestar um livro, se estiver disponível
    def emprestar_livro(self, titulo):
        if titulo in self.inventario and self.inventario[titulo] > 0:
            self.inventario[titulo] -= 1
            print(f"Livro '{titulo}' emprestado.")
        else:
            print(f"O livro '{titulo}' não está disponível.")

    # Método para verificar o inventário de livros
    def verificar_inventario(self):
        for titulo, quantidade in  self.inventario.items():
            print(f"{titulo}: {quantidade} disponível(is)")

# Exemplo de uso
biblioteca = Biblioteca()
biblioteca.adicionar_livro("Python 101", 3)
biblioteca.adicionar_livro("Aprendendo POO", 2)
biblioteca.verificar_inventario()
biblioteca.emprestar_livro("Python 101")
biblioteca.verificar_inventario()
