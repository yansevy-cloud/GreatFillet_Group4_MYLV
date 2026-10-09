from historico import registrar_acao
def cadastrar_item(cardapio, pilha_historico):
    while True:
        try:
            id_item = int(input("Digite o ID do item: "))
            break  
        except ValueError:
            print("Erro: O ID deve ser um número inteiro.")

    # Verifica se o ID já existe
    for item in cardapio:
        if item["id"] == id_item:
            print("Erro: Já existe um item cadastrado com este ID!")
            return

    while True:
        nome = input("Digite o nome do prato: ").strip().title()
        if nome:
            break 
        print("Erro: O nome do prato não pode estar em branco.")

    # Validação do Preço
    while True:
        try:
            preco = float(input("Digite o preço (R$): "))
            if preco > 0:
                break  
            print("Erro: O preço deve ser maior que zero.")
        except ValueError:
            print("Erro: Preço inválido.")

    cardapio.append({
        "id": id_item,
        "nome": nome,
        "preco": preco
    })

    print(f"Item '{nome}' cadastrado com sucesso!")
    registrar_acao(
    pilha_historico,
    "cadastrar_item",
    cardapio[-1]
    )
    


def remover_item(cardapio, pilha_historico):
    while True:
        try:
            id_item = int(input("Digite o ID do item a ser removido: "))
            break
        except ValueError:
            print("Erro: O ID deve ser um número inteiro.")

    for item in cardapio:
        if item["id"] == id_item:
            item_removido = item.copy()
            cardapio.remove(item)

            registrar_acao(
                pilha_historico,
                "remover_item",
                item_removido
            )

            print(f"Item ID {id_item} removido com sucesso!")
            return

    print("Erro: Item com este ID não foi encontrado no cardápio.")
    


def exibir_cardapio(cardapio):
    if not cardapio:
        print("\nO cardápio está vazio.")
        return  

    print("\n           CARDÁPIO")

    for item in cardapio:
        print(f"ID: {item['id']}")
        print(f"Prato: {item['nome']}")
        print(f"Preço: R$ {item['preco']:.2f}")


# Função: buscar_item
# Onde fica: Função auxiliar do cardápio para pesquisar e retornar um item pelo seu ID
def buscar_item(cardapio, id_item):
    for item in cardapio:
        if item["id"] == id_item:
            return item

    return None
