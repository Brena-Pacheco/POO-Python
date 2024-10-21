class Veiculo:
    contador_veiculos = 0
    
    def __init__(self, nome, ano, valor_diario):
        self._nome = nome
        self._ano = ano
        self._valor_diario = valor_diario
        Veiculo.contador_veiculos += 1
    
    # Métodos de acesso (Getters e Setters)
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano
    
    @property
    def valor_diario(self):
        return self._valor_diario
    
    @valor_diario.setter
    def valor_diario(self, novo_valor):
        self._valor_diario = novo_valor

    # Método para cálculo do valor total do aluguel
    def calcular_aluguel(self, dias, desconto=0):
        total = (self._valor_diario * dias) * (1 - desconto)
        return total

    @classmethod
    def ajustar_valores(cls, percentual):
        cls._valor_diario *= (1 + percentual)

    @classmethod
    def total_veiculos(cls):
        return cls.contador_veiculos
