class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando objetos da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

# Chamando o método apresentar
pessoa1.apresentar()
pessoa2.apresentar()
