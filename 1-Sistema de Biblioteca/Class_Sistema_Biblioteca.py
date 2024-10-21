# Classe que modela um sistema de biblioteca
class Biblioteca:
    def __init__(self):
        # Dicionário para armazenar o inventário de livros. O título do livro é a chave, e a quantidade é o valor.
        self.inventario = {}

    # Método para adicionar livros ao inventário
    def adicionar_livro(self, titulo, quantidade):
        # Verifica se o livro já está no inventário
        if titulo in self.inventario:
            # Se o livro já existe, aumenta a quantidade
            self.inventario[titulo] += quantidade
        else:
            # Se o livro não existe, adiciona com a quantidade inicial
            self.inventario[titulo] = quantidade
        print(f"{quantidade} unidade(s) do livro '{titulo}' adicionada(s) ao inventário.")

    # Método para emprestar um livro
    def emprestar_livro(self, titulo):
        # Verifica se o livro está disponível no inventário
        if titulo in self.inventario and self.inventario[titulo] > 0:
            # Se disponível, diminui a quantidade em 1
            self.inventario[titulo] -= 1
            print(f"Livro '{titulo}' emprestado com sucesso.")
        elif titulo in self.inventario:
            # Se o livro existe mas está com quantidade 0
            print(f"O livro '{titulo}' está indisponível para empréstimo.")
        else:
            # Se o livro não existe no inventário
            print(f"O livro '{titulo}' não está no inventário.")

    # Método para verificar o inventário de livros
    def verificar_inventario(self):
        # Verifica se o inventário está vazio
        if not self.inventario:
            print("O inventário está vazio.")
        else:
            # Imprime a lista de livros e suas quantidades
            print("Inventário de livros:")
            for titulo, quantidade in self.inventario.items():
                print(f"Livro: '{titulo}', Quantidade disponível: {quantidade}")

# Exemplo de uso do sistema de biblioteca
biblioteca = Biblioteca()

# Adicionando livros ao inventário
biblioteca.adicionar_livro("Python 101", 5)
biblioteca.adicionar_livro("Aprendendo POO", 3)

# Verificando o inventário
biblioteca.verificar_inventario()

# Emprestando um livro
biblioteca.emprestar_livro("Python 101")

# Verificando o inventário após o empréstimo
biblioteca.verificar_inventario()

# Tentativa de emprestar um livro inexistente
biblioteca.emprestar_livro("Python Avançado")

# Tentativa de emprestar um livro que está esgotado
biblioteca.emprestar_livro("Aprendendo POO")
biblioteca.emprestar_livro("Aprendendo POO")
biblioteca.emprestar_livro("Aprendendo POO")
biblioteca.emprestar_livro("Aprendendo POO")  # Esse deve falhar
