from ClasseFila import Fila

'''
Fila da Cozinha (Estrutura: Classe Fila fornecida): 
Gerencia a ordem dos pedidos que aguardam preparo na cozinha.
Garante o comportamento FIFO (First In, First Out) —
o primeiro pedido cadastrado é o primeiro a ser preparado.
'''

'''
RF-04 (Lançar Pedido - Enfileirar):
Registrar um pedido informando o Nome do Cliente 
e os IDs dos Itens (validados no cardápio). 
O pedido deve ser enfileirado na Fila da Cozinha.

RF-05 (Atender Pedido - Desenfileirar): 
Processar o próximo pedido da fila usando o método de 
desenfileirar e exibir os dados do pedido finalizado.

RF-06 (Visualizar Fila): 
Exibir no terminal os pedidos aguardando preparo na cozinha.
'''

# Requisito RF-04: Lançar Pedido
def popular_fila(filaCozinha, cardapio):
    while True:
        nome = input("\nInsira o nome do seu cliente (Enter para finalizar os pedidos): ").strip().title()

        if nome == "":
            print("Finalizando inserção de clientes...")
            break

        PedidoCliente = {}
        ItensPedidos = []

        while True:
            try:
                ID_item = int(input("Digite o ID do item (0 para concluir o pedido do cliente): "))
            except ValueError:
                print("ERRO: digite um número inteiro.")
                continue

            if ID_item == 0:
                print("Finalizando pedido deste cliente...")
                break

            if ID_item < 0:
                print("Insira um ID válido!")
                continue

            ids_validos = [item["id"] for item in cardapio] if cardapio and isinstance(cardapio[0], dict) else []

            if ID_item in ids_validos:
                ItensPedidos.append(ID_item)
                print(f"Item {ID_item} adicionado com sucesso!")
            else:
                print(f"ERRO: ID {ID_item} não encontrado no cardápio!")

        if len(ItensPedidos) > 0:
            PedidoCliente["CLIENTE"] = nome
            PedidoCliente["PEDIDOS"] = ItensPedidos

            filaCozinha.entrar(PedidoCliente)
            print(f"Sucesso: Pedido do cliente '{nome}' enviado para a cozinha!")
        else:
            print(f"Nenhum item válido adicionado para {nome}. Pedido não registrado.")


# Requisito RF-05: Atender Pedido
def atender_pedido(filaCozinha):
    if filaCozinha.isEmpty():
        print("\nNão há pedidos para atender.")
        return
    
    pedido = filaCozinha.chamar()
    print(f"\nPedido atendido: CLIENTE -> {pedido['CLIENTE']} | PEDIDOS -> {pedido['PEDIDOS']}")


# Requisito RF-06: Visualizar Fila
def mostrar_pedidos(filaCozinha):
    print("\nPedidos a serem preparados:")
    filaCozinha.verFila()