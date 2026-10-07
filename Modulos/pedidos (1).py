# Módulo 2: Atendimento e Cozinha (usa a fila de pedidos)

# Função: lancar_pedido(cardapio, fila, pilha)  [RF-04 e RF-07]
# - Pede o nome do cliente e os IDs dos pratos pedidos.
# - Valida se os pratos existem no cardápio e calcula o valor total.
# - Cria o dicionário do pedido e adiciona na fila usando enfileirar().
# - Registra a ação na pilha de histórico usando empilhar().

# Função: atender_pedido(fila, pilha)  [RF-05 e RF-07]
# - Verifica se a fila está vazia.
# - Remove o próximo pedido da fila usando desenfileirar().
# - Exibe os dados do pedido atendido na tela.
# - Registra a ação na pilha de histórico usando empilhar().

# Função: visualizar_fila(fila)  [RF-06]
# - Mostra todos os pedidos aguardando na cozinha por ordem de chegada.
# - Avisa caso a fila esteja vazia.
