class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros / 100

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos, Peso: {self.peso:.1f} kg, Altura: {self.altura:.2f} m"


def main():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa (kg): "))
    altura = float(input("Digite a altura da pessoa (m): "))

    pessoa = Pessoa(nome, idade, peso, altura)
    print(pessoa)

    pessoa.envelhecer(3)
    print(pessoa)

    pessoa.engordar(5)
    print(pessoa)

    pessoa.emagrecer(2)
    print(pessoa)


if __name__ == "__main__":
    main()