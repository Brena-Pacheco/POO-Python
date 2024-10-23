# Importações para o Web Bot
from botcity.web import WebBot, Browser, By

# Importações para integração com o BotCity Maestro SDK
from botcity.maestro import *

# Desativar erros se não estivermos conectados ao Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Inicializa a conexão com o Maestro (se aplicável)
    maestro = BotMaestroSDK.from_sys_args()

    # Pega os detalhes da execução, incluindo parâmetros da tarefa
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Inicializa o Bot Web
    bot = WebBot()

    # Configurar para rodar com ou sem headless (sem interface gráfica)
    bot.headless = False

    # Definir navegador como Chrome (padrão)
    bot.browser = Browser.CHROME

    # Abrir a página do formulário de empréstimos
    bot.browse("http://localhost:8000/emprestimo.html")  # Substitua pelo seu endereço do formulário

    # Aguardar até que os elementos estejam disponíveis antes de prosseguir
    bot.wait_for_element("//*[@id='codigo']", By.XPATH, timeout=5000)
    
    # Preencher o código do livro usando send_keys
    bot.send_keys("//*[@id='codigo']", "12345")  # Substitua pelo código real do livro
    
    # Preencher o nome do cliente usando send_keys
    bot.send_keys("//*[@id='nome-cliente']", "João Silva")  # Substitua pelo nome real do cliente

    # Clicar no botão para registrar o empréstimo
    bot.click("//*[@id='submit-emprestimo']")

    # Aguardar 3 segundos antes de fechar
    bot.wait(3000)

    # Fechar o navegador para evitar processos abertos
    bot.stop_browser()

    # Finalizar a tarefa no Maestro (se aplicável)
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


# Função de callback caso um elemento não seja encontrado
def not_found(label):
    print(f"Elemento não encontrado: {label}")


if __name__ == '__main__':
    main()
