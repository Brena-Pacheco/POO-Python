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

# Função para criar um carro
def criar_carro():
    nome = input("Digite o nome do carro: ")
    ano = int(input("Digite o ano do carro: "))
    valor_diario = float(input("Digite o valor diário do aluguel: "))
    tipo_combustivel = input("Digite o tipo de combustível (gasolina, etanol, etc.): ")
    return Carro(nome, ano, valor_diario, tipo_combustivel)

# Função para criar uma moto
def criar_moto():
    nome = input("Digite o nome da moto: ")
    ano = int(input("Digite o ano da moto: "))
    valor_diario = float(input("Digite o valor diário do aluguel: "))
    cilindrada = int(input("Digite a cilindrada da moto (150cc, 250cc, etc.): "))
    return Moto(nome, ano, valor_diario, cilindrada)

# Função principal
def sistema_de_aluguel():
    veiculos = []  # Lista para armazenar os veículos
    while True:
        print("\n--- Sistema de Aluguel de Veículos ---")
        print("1. Cadastrar Carro")
        print("2. Cadastrar Moto")
        print("3. Calcular Aluguel")
        print("4. Exibir Total de Veículos Cadastrados")
        print("5. Aplicar Aumento Percentual no Valor Diário de Todos os Veículos")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            carro = criar_carro()
            veiculos.append(carro)
            print("Carro cadastrado com sucesso!")

        elif opcao == "2":
            moto = criar_moto()
            veiculos.append(moto)
            print("Moto cadastrada com sucesso!")

        elif opcao == "3":
            if not veiculos:
                print("Nenhum veículo cadastrado!")
            else:
                for i, veiculo in enumerate(veiculos):
                    print(f"{i + 1}. {veiculo.get_nome()} ({veiculo.get_ano()})")
                escolha = int(input("Escolha um veículo pelo número: ")) - 1
                dias = int(input("Digite o número de dias de aluguel: "))
                desconto = float(input("Digite o desconto (0 para nenhum): "))
                valor_total = veiculos[escolha].calcular_valor_total(dias, desconto)
                print(f"Valor total do aluguel: R${valor_total:.2f}")

        elif opcao == "4":
            print(f"Total de veículos cadastrados: {Veiculo.total_veiculos_cadastrados()}")

        elif opcao == "5":
            percentual = float(input("Digite o percentual de aumento: "))
            Veiculo.aplicar_aumento(veiculos, percentual)
            print("Aumento aplicado com sucesso!")

        elif opcao == "6":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o sistema de aluguel
sistema_de_aluguel()
