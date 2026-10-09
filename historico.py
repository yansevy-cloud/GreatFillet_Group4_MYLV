# Módulo de Histórico: Gerenciamento da Pilha de Ações (LIFO)
# Responsável por registrar, visualizar e desfazer ações do sistema

# Função: registrar_acao
# Onde fica: Chamada sempre que uma ação que pode ser desfeita for executada (ex: cadastrar item, remover item, lançar pedido, atender pedido)
    # TODO: Implementar o registro da ação empilhando na pilha_historico (push)
def registrar_acao(pilha_historico, tipo_acao, dados):
    acao = {
        "tipo": tipo_acao,
        "dados": dados.copy()
    }
    pilha_historico.push(acao) 
    pass


# Requisito RF-07: Desfazer Última Ação
# Onde fica: Opção 7 do menu principal (main.py)
def desfazer_ultima_acao(pilha_historico, fila_cozinha, cardapio=None):
    if pilha_historico.isEmpty():
        print("Não há ações para desfazer.")
        return

    acao = pilha_historico.pop()

    tipo_acao = acao["tipo"]
    dados = acao["dados"]

    # Desfaz o lançamento de um pedido
    if tipo_acao == "lancar_pedido":
        pedidos = fila_cozinha._pacientes

        if dados in pedidos:
            pedidos.remove(dados)
            print("Último pedido lançado foi cancelado.")
        else:
            print("Pedido não encontrado na fila.")
            pilha_historico.push(acao)

    # Desfaz o atendimento de um pedido
    elif tipo_acao == "atender_pedido":
        fila_cozinha._pacientes.insert(0, dados)
        print("Pedido devolvido ao início da fila.")

    else:
        print("Tipo de ação não reconhecido.")
        pilha_historico.push(acao)

# Requisito RF-08: Visualizar Histórico de Ações
# Onde fica: Opção 8 do menu principal (main.py)
def visualizar_historico(pilha_historico):
    if pilha_historico.isEmpty():
        print("\nO histórico está vazio.")
        return

    print("\n===== HISTÓRICO DE AÇÕES =====")

    # Percorre a pilha do topo até a base, sem remover os registros
    for i, acao in enumerate(
        reversed(pilha_historico._elementos), start=1
    ):
        tipo_acao = acao["tipo"]
        dados = acao["dados"]

        if tipo_acao == "lancar_pedido":
            print(
                f"{i}. Pedido lançado - "
                f"Cliente: {dados['CLIENTE']} - "
                f"Itens: {dados['PEDIDOS']}"
            )

        elif tipo_acao == "atender_pedido":
            print(
                f"{i}. Pedido atendido - "
                f"Cliente: {dados['CLIENTE']} - "
                f"Itens: {dados['PEDIDOS']}"
            )

        else:
            print(f"{i}. Ação realizada: {tipo_acao}")
