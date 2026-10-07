# Módulo 1: Gestão do Cardápio (usa lista nativa do Python)
# Cada item é um dicionário: {"id": int, "nome": str, "preco": float}

# Função: buscar_item_por_id(cardapio, id_item)
# - Percorre o cardápio e retorna o item com o ID informado, ou None.

# Função: cadastrar_item(cardapio)  [RF-01]
# - Pede ID, Nome e Preço do prato.
# - Valida se o ID já existe e se o preço é positivo.
# - Adiciona o dicionário do prato na lista do cardápio.

# Função: remover_item(cardapio)  [RF-02]
# - Pede o ID do prato e remove da lista se existir.
# - Exibe mensagem de erro se o ID não for encontrado.

# Função: exibir_cardapio(cardapio)  [RF-03]
# - Imprime todos os pratos formatados (ID, Nome e Preço).
# - Avisa caso o cardápio esteja vazio.
