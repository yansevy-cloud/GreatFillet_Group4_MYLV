def registrar_acao(pilha_historico, tipo_acao, dados):
    acao = {
        "tipo": tipo_acao,
        "dados": dados.copy()
    }
    pilha_historico.push(acao)

def desfazer_ultima_acao(pilha_historico, fila_cozinha, cardapio=None):
    if pilha_historico.isEmpty():
        print("Não há ações para desfazer.")
        return

    acao = pilha_historico.pop()
    tipo_acao = acao["tipo"]
    dados = acao["dados"]

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

    elif tipo_acao == "lancar_pedido":
        pedidos = fila_cozinha._pacientes

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

    elif tipo_acao == "atender_pedido":
        fila_cozinha._pacientes.insert(0, dados.copy())
        print("Pedido devolvido ao início da fila.")

    else:
        pilha_historico.push(acao)
        print(f"Tipo de ação não reconhecido: {tipo_acao}")

def exibir_historico(pilha_historico):
    if pilha_historico.isEmpty():
        print("Não há ações para exibir.")
        return

    print("\nHistórico de Ações (do mais recente para o mais antigo):")
    print("-" * 40)

    for acao in reversed(pilha_historico._elementos):
        print(f"{acao['tipo']}: {acao['dados']}")

    print("\n" * 2)    
