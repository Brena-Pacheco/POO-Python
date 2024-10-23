from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    def mostrar_area(self):
        print(f"A área é: {self.area()}")

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

# Testando as classes
quadrado = Quadrado(4)
circulo = Circulo(3)
quadrado.mostrar_area()
circulo.mostrar_area()
