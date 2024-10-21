class Veiculo:
    total_veiculos = 0  # Variável de classe para contar o total de veículos

    def __init__(self, nome, ano, valor_diario):
        self.__nome = nome  # Propriedades privadas
        self.__ano = ano
        self.__valor_diario = valor_diario
        Veiculo.total_veiculos += 1  # Incrementa o total de veículos cadastrados

    # Métodos para obter e definir os valores encapsulados
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_valor_diario(self):
        return self.__valor_diario

    def set_valor_diario(self, valor):
        self.__valor_diario = valor

    # Método de cálculo do valor total do aluguel com desconto opcional
    def calcular_valor_total(self, dias, desconto=0):
        return (self.__valor_diario * dias) * (1 - desconto)

    # Método de classe para contar veículos cadastrados
    @classmethod
    def total_veiculos_cadastrados(cls):
        return cls.total_veiculos

    # Método de classe para aplicar um aumento percentual no valor diário de todos os veículos
    @classmethod
    def aplicar_aumento(cls, lista_veiculos, percentual):
        for veiculo in lista_veiculos:
            veiculo.set_valor_diario(veiculo.get_valor_diario() * (1 + percentual / 100))


class Carro(Veiculo):
    def __init__(self, nome, ano, valor_diario, tipo_combustivel):
        super().__init__(nome, ano, valor_diario)
        self.tipo_combustivel = tipo_combustivel  # Propriedade específica

    # Sobrescreve o método de cálculo para aplicar desconto extra para aluguel acima de 7 dias
    def calcular_valor_total(self, dias, desconto=0):
        valor_total = super().calcular_valor_total(dias, desconto)
        if dias > 7:
            valor_total *= 0.9  # 10% de desconto extra
        return valor_total


class Moto(Veiculo):
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self.cilindrada = cilindrada  # Propriedade específica

    # Sobrescreve o método de cálculo para aumentar o custo se a cilindrada for maior que 200cc
    def calcular_valor_total(self, dias, desconto=0):
        valor_total = super().calcular_valor_total(dias, desconto)
        if self.cilindrada > 200:
            valor_total *= 1.2  # Aumento de 20% no custo
        return valor_total

# Exemplo de uso do sistema

# Criação de alguns veículos
carro1 = Carro("Toyota Corolla", 2020, 150, "Gasolina")
moto1 = Moto("Honda CB300", 2022, 100, 300)

# Lista de veículos
veiculos = [carro1, moto1]

# Exibindo informações e calculando aluguel
print(f"Nome: {carro1.get_nome()}, Valor Total (5 dias): R${carro1.calcular_valor_total(5):.2f}")
print(f"Nome: {moto1.get_nome()}, Valor Total (10 dias): R${moto1.calcular_valor_total(10):.2f}")

# Exemplo de aumento de preço para todos os veículos
Veiculo.aplicar_aumento(veiculos, 10)
print(f"Novo valor diário do {carro1.get_nome()}: R${carro1.get_valor_diario():.2f}")
print(f"Novo valor diário da {moto1.get_nome()}: R${moto1.get_valor_diario():.2f}")

# Exibindo total de veículos cadastrados
print(f"Total de veículos cadastrados: {Veiculo.total_veiculos_cadastrados()}")
