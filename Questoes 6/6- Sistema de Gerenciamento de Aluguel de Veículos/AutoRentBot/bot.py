# Importação do BotCity Web
from botcity.web import WebBot, Browser
from botcity.web import By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

# Desativar erros se não estiver conectado ao Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Importar pandas para manipulação de dados
import pandas as pd

class Form_Bot:
    def __init__(self):
        self.bot = WebBot()
        self.bot.headless = False
        self.bot.browser = Browser.CHROME
        self.bot.driver_path = ChromeDriverManager().install()

    def action(self, execution=None):
        print('estou aqui')
        # Caminho do ChromeDriver
        self.bot.driver_path = ChromeDriverManager().install()
        
        # Caminho do arquivo Excel
        caminho_excel = r'C:\\Users\\matutino\\OneDrive\\Área de Trabalho\\POO\\Exercicios_Individuais\\Questoes 6\\6- Sistema de Gerenciamento de Aluguel de Veículos\AutoRentBot\\veiculos.xlsx'
        
        # Ler a planilha Excel
        try:
            df = pd.read_excel(caminho_excel)
        except Exception as e:
            print(f"Erro ao ler o arquivo Excel: {e}")
            return
        print('li planilha')
        # Abrir o navegador e acessar o formulário local
        self.bot.browse("http://localhost:8000/form.html")  # Acesse o formulário

        # Preencher o formulário para cada veículo na planilha
        for index, row in df.iterrows():
            try:
                print('preencher form')

                # Preencher os campos do formulário na ordem correta usando XPath
                self.bot.send_keys("//*[@id='nome']", row['Nome do Veículo'])  # Nome do Veículo
                self.bot.type("//*[@id='ano']", str(row['Ano de Fabricação']))  # Ano de Fabricação
                self.bot.type("//*[@id='valor-diario']", str(row['Valor Diário de Aluguel']))  # Valor Diário de Aluguel
                self.bot.combo_select_by_value("//*[@id='tipo']", row['Tipo de Veículo'])  # Tipo de Veículo
                self.bot.type("//*[@id='opcao-adicional']", row['Opção de Combustível/Cilindrada'])  # Combustível ou Cilindrada

                # Clicar no botão de adicionar veículo
                self.bot.click("//*[@id='adicionar-veiculo']")

                # Opcional: Pausar entre as inserções para evitar sobrecarga na aplicação
                self.bot.wait(2000)  # Aumente a pausa se necessário

            except Exception as e:
                print(f"Erro ao preencher o formulário para o veículo na linha {index + 1}: {e}")

# Executar o bot
if __name__ == "__main__":
    form_bot = Form_Bot()
    form_bot.action()
    input("Pressione Enter para fechar o bot...")  # Aguarda a entrada do usuário antes de fechar
