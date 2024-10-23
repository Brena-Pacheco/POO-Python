class ContaBancaria:
    def __init__(self, titular):
        self._saldo = 0.0  # Atributo privado
        self.titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor

# Testando a classe ContaBancaria
conta = ContaBancaria("Carlos")
conta.saldo = 100.0  # Definindo saldo
print(conta.saldo)

try:
    conta.saldo = -50.0  # Tentando definir saldo negativo
except ValueError as e:
    print(e)
