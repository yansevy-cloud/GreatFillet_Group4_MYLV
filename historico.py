# Módulo de Histórico: Gerenciamento da Pilha de Ações (LIFO)
# Responsável por registrar, visualizar e desfazer ações do sistema

# Função: registrar_acao
# Onde fica: Chamada sempre que uma ação que pode ser desfeita for executada (ex: cadastrar item, remover item, lançar pedido, atender pedido)
def registrar_acao(pilha_historico, tipo_acao, dados):
    # TODO: Implementar o registro da ação empilhando na pilha_historico (push)
    pass


# Requisito RF-07: Desfazer Última Ação
# Onde fica: Opção 7 do menu principal (main.py)
def desfazer_ultima_acao(pilha_historico, fila_cozinha, cardapio=None):
    # TODO: Implementar a lógica de desempilhar (pop) a última ação e reverter seu efeito
    pass


# Requisito RF-08: Visualizar Histórico de Ações
# Onde fica: Opção 8 do menu principal (main.py)
def visualizar_historico(pilha_historico):
    # TODO: Implementar a exibição de todas as ações registradas na pilha_historico
    pass
