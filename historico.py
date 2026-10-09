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


# Desfaz a última ação registrada
def desfazer_ultima_acao(pilha_historico, fila_cozinha, cardapio=None):
    if pilha_historico.isEmpty():
        print("Não há ações para desfazer.")
        return

    acao = pilha_historico.pop()
    tipo_acao = acao["tipo"]
    dados = acao["dados"]

    # Desfaz o cadastro de um prato
    if tipo_acao == "cadastrar_item":
        if cardapio is None:
            pilha_historico.push(acao)
            print("Cardápio não disponível para desfazer.")
            return

        item = next(
            (item for item in cardapio if item["id"] == dados["id"]),
            None
        )

        if item is not None:
            cardapio.remove(item)
            print(f"Cadastro do prato '{dados['nome']}' desfeito.")
        else:
            pilha_historico.push(acao)
            print("Prato não encontrado no cardápio.")

    # Desfaz a remoção de um prato
    elif tipo_acao == "remover_item":
        if cardapio is None:
            pilha_historico.push(acao)
            print("Cardápio não disponível para desfazer.")
            return

        if not any(item["id"] == dados["id"] for item in cardapio):
            cardapio.append(dados.copy())
            print(f"Prato '{dados['nome']}' restaurado ao cardápio.")
        else:
            pilha_historico.push(acao)
            print("Já existe um prato com esse ID no cardápio.")

    # Desfaz o lançamento de um pedido
    elif tipo_acao == "lancar_pedido":
        pedidos = fila_cozinha._pacientes

        # Procura da última posição para a primeira
        indice = next(
            (
                i for i in range(len(pedidos) - 1, -1, -1)
                if pedidos[i] == dados
            ),
            None
        )

        if indice is not None:
            pedidos.pop(indice)
            print("Último pedido lançado foi cancelado.")
        else:
            pilha_historico.push(acao)
            print("Pedido não encontrado na fila.")

    # Desfaz o atendimento de um pedido
    elif tipo_acao == "atender_pedido":
        fila_cozinha._pacientes.insert(0, dados.copy())
        print("Pedido devolvido ao início da fila.")

    else:
        pilha_historico.push(acao)
        print(f"Tipo de ação não reconhecido: {tipo_acao}")


# Visualiza o histórico sem retirar as ações da pilha
def visualizar_historico(pilha_historico):
    if pilha_historico.isEmpty():
        print("\nO histórico está vazio.")
        return

    print("\n===== HISTÓRICO DE AÇÕES =====")

    for i, acao in enumerate(
        reversed(pilha_historico._elementos), start=1
    ):
        tipo_acao = acao["tipo"]
        dados = acao["dados"]

        if tipo_acao == "lancar_pedido":
            descricao = (
                f"Pedido lançado - Cliente: {dados['CLIENTE']} - "
                f"Itens: {dados['PEDIDOS']}"
            )

        elif tipo_acao == "atender_pedido":
            descricao = (
                f"Pedido atendido - Cliente: {dados['CLIENTE']} - "
                f"Itens: {dados['PEDIDOS']}"
            )

        elif tipo_acao == "cadastrar_item":
            descricao = (
                f"Prato cadastrado - {dados['nome']} "
                f"(ID: {dados['id']})"
            )

        elif tipo_acao == "remover_item":
            descricao = (
                f"Prato removido - {dados['nome']} "
                f"(ID: {dados['id']})"
            )

        else:
            descricao = f"Ação: {tipo_acao}"

        print(f"{i}. {descricao}")
