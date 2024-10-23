class Motor:
    def ligar(self):
        print("Motor ligado.")

class Roda:
    def girar(self):
        print("Rodas girando.")

class Carro:
    def __init__(self):
        self.motor = Motor()
        self.rodas = [Roda() for _ in range(4)]  # Quatro rodas

    def ligar_motor(self):
        self.motor.ligar()

    def girar_rodas(self):
        for roda in self.rodas:
            roda.girar()

# Testando a classe Carro
carro = Carro()
carro.ligar_motor()
carro.girar_rodas()
