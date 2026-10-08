# Módulo de Interface: Menu e Telas do Terminal

# Função: exibir_menu()
# - Imprime as opções do menu no terminal (opções 0 a 8):
#   1. Cadastrar Item no Cardápio
#   2. Remover Item do Cardápio
#   3. Listar Cardápio
#   4. Lançar Novo Pedido
#   5. Atender Próximo Pedido
#   6. Visualizar Fila da Cozinha
#   7. Desfazer Última Ação
#   8. Visualizar Histórico de Ações
#   0. Sair

# Função: obter_opcao()
# - Lê a opção digitada pelo usuário e valida se está entre '0' e '8'.

def exibir_menu():
    print("""
    1. Cadastrar Item no Cardápio
    2. Remover Item do Cardápio
    3. Listar Cardápio
    4. Lançar Novo Pedido
    5. Atender Próximo Pedido
    6. Visualizar Fila da Cozinha
    7. Desfazer Última Ação
    8. Visualizar Histórico de Ações
    0. Sair
    """)

def obter_opcao():
    return input("Digite o número da opção desejada: ")