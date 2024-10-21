# Classe Veiculo
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método para exibir informações do veículo
    def informacao(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Classe Carro que herda de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    # Método para exibir todas as informações, incluindo o número de portas
    def informacao(self):
        super().informacao()
        print(f"Número de portas: {self.numero_portas}")

# Exemplo de uso
carro = Carro("Toyota", "Corolla", 4)
carro.informacao()
