# Classe Veiculo representa um veículo com marca e modelo
class Veiculo:
    # Método construtor que inicializa os atributos marca e modelo
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método que exibe as informações do veículo
    def informacao(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Classe Carro que herda da classe Veiculo e adiciona o atributo numero_portas
class Carro(Veiculo):
    # Método construtor que inicializa os atributos marca, modelo e numero_portas
    def __init__(self, marca, modelo, numero_portas):
        # Chama o construtor da classe pai (Veiculo) para inicializar marca e modelo
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    # Método que exibe todas as informações do carro, incluindo o número de portas
    def informacao_completa(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Número de portas: {self.numero_portas}")

# Função principal para solicitar dados do usuário e criar um carro
def main():
    # Solicitando as informações do carro ao usuário
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    numero_portas = int(input("Digite o número de portas do carro: "))

    # Criando um objeto da classe Carro com as informações fornecidas
    carro = Carro(marca, modelo, numero_portas)

    # Exibindo as informações completas do carro
    carro.informacao_completa()

# Executando a função principal
if __name__ == "__main__":
    main()
