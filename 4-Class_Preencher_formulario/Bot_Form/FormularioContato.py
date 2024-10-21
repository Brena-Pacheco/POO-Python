from FormBase import FormBase

class FormularioContato(FormBase):
    def __init__(self):
        super().__init__()

    def preencher_formulario(self, dados):
        # Implementar lógica de preenchimento para o formulário de contato
        print("Preenchendo o formulário de contato com os dados:", dados)
