from FormBase import FormBase

class FormularioLogin(FormBase):
    def __init__(self):
        super().__init__()

    def preencher_formulario(self, dados):
        # Implementar lógica de preenchimento para o formulário de login
        print("Preenchendo o formulário de login com os dados:", dados)
