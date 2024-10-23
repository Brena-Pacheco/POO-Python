class Pessoa:
    def __init__(self, nome, idade, peso, altura_cm, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura_cm / 100  
        self.sexo = sexo.lower() 

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def faixa_de_peso(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade Grau I"
        elif 35 <= imc < 39.9:
            return "Obesidade Grau II"
        else:
            return "Obesidade Grau III"

    def peso_ideal(self):
        peso_ideal_min = 18.5 * (self.altura ** 2)
        peso_ideal_max = 24.9 * (self.altura ** 2)
        return peso_ideal_min, peso_ideal_max

    def estimar_gordura_corporal(self):
        imc = self.calcular_imc()
        if self.sexo == 'masculino':
            percentual_gordura = 1.20 * imc + 0.23 * self.idade - 16.2
        else:
            percentual_gordura = 1.20 * imc + 0.23 * self.idade - 5.4
        return percentual_gordura

    def envelhecer(self, anos=1):
        for _ in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.altura += 0.005  # 0.5 cm = 0.005 metros

    def engordar(self, kilos):
        self.peso += kilos

    def emagrecer(self, kilos):
        if kilos <= self.peso:
            self.peso -= kilos

    def crescer(self, centimetros):
        self.altura += centimetros / 100  

def main():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (masculino/feminino): ")
    peso = float(input("Digite o peso da pessoa (kg): "))
    altura_cm = float(input("Digite a altura da pessoa (cm): "))  

    pessoa = Pessoa(nome, idade, peso, altura_cm, sexo)
    
    imc = pessoa.calcular_imc()
    faixa = pessoa.faixa_de_peso()
    peso_ideal_min, peso_ideal_max = pessoa.peso_ideal()
    gordura_corporal = pessoa.estimar_gordura_corporal()

    print(f"O IMC de {pessoa.nome} é: {imc:.2f}")
    print(f"Faixa de peso: {faixa}")
    print(f"O peso ideal está entre {peso_ideal_min:.2f} kg e {peso_ideal_max:.2f} kg")
    print(f"A porcentagem estimada de gordura corporal é: {gordura_corporal:.2f}%")

if __name__ == "__main__":
    main()
