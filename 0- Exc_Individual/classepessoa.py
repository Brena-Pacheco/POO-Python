class Pessoa:
    def __init__(self, nome, idade, peso, altura_cm):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura_cm / 100 

    def envelhecer(self, anos=1):
        for _ in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.altura += 0.005  
        print(f"{self.nome} envelheceu {anos} anos e agora tem {self.idade} anos.")

    def engordar(self, kilos):
        self.peso += kilos
        print(f"{self.nome} engordou {kilos} kg e agora pesa {self.peso} kg.")

    def emagrecer(self, kilos):
        if kilos <= self.peso:
            self.peso -= kilos
            print(f"{self.nome} emagreceu {kilos} kg e agora pesa {self.peso} kg.")
        else:
            print(f"{self.nome} não pode emagrecer mais do que o peso atual.")

    def crescer(self, centimetros):
        self.altura += centimetros / 100  
        print(f"{self.nome} cresceu {centimetros} cm e agora tem {self.altura * 100:.2f} cm.")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura * 100:.2f} cm") 


def main():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa (kg): "))
    altura_cm = float(input("Digite a altura da pessoa (cm): ")) 

    pessoa = Pessoa(nome, idade, peso, altura_cm)

    while True:
        print("\nEscolha uma ação:")
        print("1. Envelhecer")
        print("2. Engordar")
        print("3. Emagrecer")
        print("4. Crescer")
        print("5. Exibir informações")
        print("6. Sair")
        opcao = input("Digite o número da ação: ")

        if opcao == '1':
            anos = int(input("Quantos anos você quer envelhecer? "))
            pessoa.envelhecer(anos)
        elif opcao == '2':
            kilos = float(input("Quantos quilos a pessoa ganhou? "))
            pessoa.engordar(kilos)
        elif opcao == '3':
            kilos = float(input("Quantos quilos a pessoa perdeu? "))
            pessoa.emagrecer(kilos)
        elif opcao == '4':
            centimetros = float(input("Quantos centímetros a pessoa cresceu? "))
            pessoa.crescer(centimetros)
        elif opcao == '5':
            pessoa.exibir_informacoes()
        elif opcao == '6':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()