# FormBase.py
class FormBase:
    def __init__(self):
        pass

    def fill_form(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses")

# FormularioContato.py
class FormularioContato(FormBase):
    def __init__(self, nome, email, mensagem):
        super().__init__()
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

    def fill_form(self):
        return {
            "Nome": self.nome,
            "Email": self.email,
            "Mensagem": self.mensagem
        }

# FormularioLogin.py
class FormularioLogin(FormBase):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def fill_form(self):
        return {
            "Username": self.username,
            "Password": self.password
        }
