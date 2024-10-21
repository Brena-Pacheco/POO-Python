class Carro(Veiculo):
    def __init__(self, nome, ano, valor_diario, combustivel):
        super().__init__(nome, ano, valor_diario)
        self._combustivel = combustivel
    
    @property
    def combustivel(self):
        return self._combustivel

    @combustivel.setter
    def combustivel(self, novo_combustivel):
        self._combustivel = novo_combustivel

    def calcular_aluguel(self, dias, desconto=0):
        # Regra de desconto se for mais de 7 dias
        if dias > 7:
            desconto += 0.10
        return super().calcular_aluguel(dias, desconto)
