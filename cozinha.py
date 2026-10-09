from Fila import Fila
from historico import registrar_acao



def popular_fila(filaCozinha, cardapio, pilha_historico):
    while True:
        nome = input(
            "\nInsira o nome do cliente "
            "(Enter para finalizar os pedidos): "
        ).strip().title()

        if nome == "":
            print("Finalizando inserção de clientes...")
            break

        PedidoCliente = {}
        ItensPedidos = []

        while True:
            try:
                ID_item = int(
                    input(
                        "Digite o ID do item "
                        "(0 para concluir o pedido): "
                    )
                )
            except ValueError:
                print("ERRO: digite um número inteiro.")
                continue

            if ID_item == 0:
                print("Finalizando pedido deste cliente...")
                break

            if ID_item < 0:
                print("Insira um ID válido!")
                continue

            ids_validos = [
                item["id"]
                for item in cardapio
                if isinstance(item, dict) and "id" in item
            ]

            if ID_item in ids_validos:
                ItensPedidos.append(ID_item)
                print(f"Item {ID_item} adicionado com sucesso!")
            else:
                print(
                    f"ERRO: ID {ID_item} "
                    "não encontrado no cardápio!"
                )

        if len(ItensPedidos) > 0:
            PedidoCliente["CLIENTE"] = nome
            PedidoCliente["PEDIDOS"] = ItensPedidos

            filaCozinha.entrar(PedidoCliente)

            registrar_acao(
                pilha_historico,
                "lancar_pedido",
                PedidoCliente
            )

            print(
                f"Sucesso: Pedido do cliente '{nome}' "
                "enviado para a cozinha!"
            )
        else:
            print(
                f"Nenhum item válido adicionado para {nome}. "
                "Pedido não registrado."
            )



def atender_pedido(filaCozinha, pilha_historico):
    if filaCozinha.isEmpty():
        print("\nNão há pedidos para atender.")
        return


    pedido = filaCozinha.chamar()

    if pedido is None:
        print("\nNão foi possível obter o pedido.")
        return

    registrar_acao(
        pilha_historico,
        "atender_pedido",
        pedido
    )

    print(
        f"\nPedido atendido: CLIENTE -> {pedido['CLIENTE']} "
        f"| PEDIDOS -> {pedido['PEDIDOS']}"
    )



def mostrar_pedidos(filaCozinha):
    print("\nPedidos a serem preparados:")

    if filaCozinha.isEmpty():
        print("Não há pedidos aguardando preparo.")
        return

    filaCozinha.verFila()
