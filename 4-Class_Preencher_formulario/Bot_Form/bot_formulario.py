"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from FormularioContato import FormularioContato
from FormularioLogin import FormularioLogin
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Configura o bot para usar o ChromeDriver
    webbot = WebBot()
    webbot.headless = False  # Modo de visualização

    # Instala e configura o ChromeDriver automaticamente
    driver = webdriver.Chrome(ChromeDriverManager().install())
    webbot.driver_path(driver)

    # Preenchendo um formulário de contato
    contato = FormularioContato("John Doe", "johndoe@example.com", "Hello, I would like to inquire about...")
    preencher_formulario_contato(webbot, contato)

    # Preenchendo um formulário de login
    login = FormularioLogin("johndoe", "s3cret")
    preencher_formulario_login(webbot, login)

    webbot.wait(3000)  # Esperar 3 segundos antes de fechar
    webbot.stop_browser()  # Para o navegador

def preencher_formulario_contato(webbot, contato):
    webbot.browse("C:\\Users\\matutino\\Desktop\\POO\\Exercicios_Individuais\\4-Class_Preencher_formulario\\Bot_Form\\formulario.html")  
    webbot.wait(3000)  # Esperar a página carregar

    # Usando o método fill_form para obter os dados
    dados_contato = contato.fill_form()
    webbot.type_text(dados_contato["Nome"], By.CSS_SELECTOR, "input[name='nome']")
    webbot.type_text(dados_contato["Email"], By.CSS_SELECTOR, "input[name='email']")
    webbot.type_text(dados_contato["Mensagem"], By.CSS_SELECTOR, "textarea[name='mensagem']")
    webbot.click(By.CSS_SELECTOR, "button[type='submit']")
    print("Formulário de contato preenchido e enviado!")

def preencher_formulario_login(webbot, login):
    webbot.browse("C:\\Users\\matutino\\Desktop\\POO\\Exercicios_Individuais\\4-Class_Preencher_formulario\\Bot_Form\\formulario.html")  
    webbot.wait(3000)  # Esperar a página carregar

    # Usando o método fill_form para obter os dados
    dados_login = login.fill_form()
    webbot.type_text(dados_login["Username"], By.CSS_SELECTOR, "input[name='username']")
    webbot.type_text(dados_login["Password"], By.CSS_SELECTOR, "input[name='password']")
    webbot.click(By.CSS_SELECTOR, "button[type='submit']")
    print("Formulário de login preenchido e enviado!")

if __name__ == "__main__":
    main()


    