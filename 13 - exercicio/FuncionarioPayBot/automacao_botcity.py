from botcity.core import DesktopBot
import time

class AutomacaoBot(DesktopBot):
    def action(self):
        # Abre a aplicação de cadastro de funcionários
        self.start_application("python", r"C:\Users\matutino\OneDrive\Área de Trabalho\POO\Exercicios_Individuais\13 - exercicio\FuncionarioPayBot\cadastro_funcionarios.py")

        # Aguarda a janela carregar
        time.sleep(5)

        # Preenche os campos
        self.fill_fields()

        # Clica no botão "Cadastrar Funcionário"
        self.click_button("Cadastrar Funcionário")

        # Aguarda o cadastro ser processado
        time.sleep(2)

        # Processar pagamentos, se necessário
        self.processar_pagamentos()

    def fill_fields(self):
        # Insira os dados do funcionário
        self.write("Nome do Funcionário")  # Nome
        self.tab()  # Move para o próximo campo
        self.write("123456")  # Matrícula
        self.tab()  # Move para o próximo campo
        self.write("3")  # Número de Projetos
        self.tab()  # Move para o próximo campo
        self.write("3000")  # Salário Base

        # Escolher tipo de funcionário
        self.tab()  # Move para o tipo de funcionário
        self.write("Mensalista")  # ou "Comissionado" ou "Horista"
        time.sleep(1)

        # Preencher os campos adicionais conforme o tipo
        if "Mensalista" in self.get_last_text():
            self.tab()  # Move para Salário (apenas se mensalista)
            self.write("3000")  # Salário Mensal
        elif "Comissionado" in self.get_last_text():
            self.tab()  # Move para Comissão
            self.write("500")  # Comissão
            self.tab()  # Move para Total de Vendas
            self.write("10000")  # Total de Vendas
        elif "Horista" in self.get_last_text():
            self.tab()  # Move para Valor por Hora
            self.write("50")  # Valor por Hora
            self.tab()  # Move para Horas por Dia
            self.write("8")  # Horas por Dia

    def click_button(self, button_text):
        # Clica no botão especificado
        self.click_button_by_text(button_text)

    def processar_pagamentos(self):
        # Clica no botão "Processar Pagamentos" se necessário
        self.click_button("Processar Pagamentos")
        time.sleep(2)

if __name__ == "__main__":
    bot = AutomacaoBot()
    bot.start()
