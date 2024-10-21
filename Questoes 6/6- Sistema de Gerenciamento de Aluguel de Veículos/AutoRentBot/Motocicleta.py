class Motocicleta(Veiculo):
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self._cilindrada = cilindrada
    
    @property
    def cilindrada(self):
        return self._cilindrada

    @cilindrada.setter
    def cilindrada(self, nova_cilindrada):
        self._cilindrada = nova_cilindrada

    def calcular_aluguel(self, dias, desconto=0):
        # Regra de aumento se a cilindrada for maior que 200cc
        if self._cilindrada > 200:
            desconto -= 0.05  # Aumento de 5%
        return super().calcular_aluguel(dias, desconto)
