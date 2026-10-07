# Módulo 3: Histórico e Auditoria (usa a pilha de ações)

# Função: desfazer_ultima_acao(pilha, fila)  [RF-08]
# - Desempilha a última ação registrada (desempilhar()).
# - Se a ação foi 'LANCAR_PEDIDO', cancela e remove o pedido da fila.
# - Se a ação foi 'ATENDER_PEDIDO', devolve o pedido ao início da fila.
# - Avisa caso a pilha esteja vazia (nada para desfazer).

# Função: visualizar_historico(pilha)  [Opção 8 do menu]
# - Exibe todas as ações registradas na pilha (auditoria).
# - Avisa caso a pilha esteja vazia.
