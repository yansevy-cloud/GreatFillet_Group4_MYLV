# Arquivo Principal: main.py
# Ponto de entrada do sistema.

# Função: main()
# 1. Inicializa as estruturas na memória:
#    - cardapio = []
#    - fila_cozinha = criar_fila()
#    - pilha_historico = criar_pilha()
#
# 2. Executa o laço de repetição (while True):
#    - Chama exibir_menu()
#    - Lê opcao com obter_opcao()
#    - Chama a função correspondente (opções 1 a 8)
#    - Opção 0 encerra o sistema
#
# 3. Execução: chamar main() no final.

from Interface.menu import exibir_menu , obter_opcao
#from Modulos.ClasseFila import Fila
from Modulos.cardapio import cadastrar_item, remover_item, exibir_cardapio
#from Modulos.cozinha import popular_fila, antender_pedido, mostrar_pedidos
#from Modulos.historico import desfazer_ultima_acao, visualizar_historico

cardapio = []


while True:
    exibir_menu()
    opcao = obter_opcao()
    match opcao:
        case '1':
            cadastrar_item(cardapio)
        case '2':
            remover_item(cardapio)
        case '3':
            exibir_cardapio(cardapio)
        case '4':
            popular_fila(fila_cozinha, cardapio)
        case '5':
            antender_pedido(fila_cozinha)
        case '6':
            mostrar_pedidos(fila_cozinha)
        case '7':
            desfazer_ultima_acao(pilha_historico, fila_cozinha)
        case '8':
            visualizar_historico(pilha_historico)
        case '0':
            print("Encerrando o sistema...")
            break
        case _:
            print("Opção inválida!")
            
    