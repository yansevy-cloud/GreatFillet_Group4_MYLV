from ClasseFila import Fila
# from Cardapio import a lista de cardapio depois pra eu validar o id

'''Fila da Cozinha (Estrutura: Classe Fila fornecida): 
Gerencia a ordem dos pedidos que aguardam preparo na cozinha.
 Garante o comportamento FIFO (First In, First Out) —
   o primeiro pedido cadastrado é o primeiro a ser preparado.'''

'''RF-04 (Lançar Pedido - Enfileirar):
 Registrar um pedido informando o Nome do Cliente 
 e os IDs dos Itens (validados no cardápio). 
 O pedido deve ser enfileirado na Fila da Cozinha.

RF-05 (Atender Pedido - Desenfileirar): 
Processar o próximo pedido da fila usando o método de 
desenfileirar e exibir os dados do pedido finalizado.

RF-06 (Visualizar Fila): 
Exibir no terminal os pedidos aguardando preparo na cozinha'''

filaCozinha = Fila()

# Requisito RF-04, enfileirar, semicompleto, falta validações finais e comparação com ID do arquivo de Cardápio, mas quase pronto
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
                ID_item = int(input(...))
            except ValueError:
                print("ERRO: digite um número inteiro.")
                continue

            if ID_item == 0:
                print("Finalizando pedido...")
                break

            if ID_item < 0:
                print("Insira um ID válido!")
                continue

            else:
                ItensPedidos.append(ID_item)

        PedidoCliente["CLIENTE"] = nome
        PedidoCliente["PEDIDOS"] = ItensPedidos

        filaCozinha.entrar(PedidoCliente)

popular_fila(filaCozinha, None)
pedido = filaCozinha.chamar()

# Requisito RF-05, pedido atendido. Chamado posteriormente no menu/interface
def antender_pedido(filaCozinha):
    pedido = filaCozinha.chamar()
    print(f"\nPedido atendido: CLIENTE -> {pedido['CLIENTE']} | PEDIDOS: -> {pedido['PEDIDOS']}")

# Requisito RF-06, visualizar itens que estão a ser preparados. Chamado posteriormente no menu/interface
def mostrar_pedidos(filaCozinha):
    print("\nPedidos a serem preparados:")
    filaCozinha.verFila()
