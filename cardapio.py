def cadastrar_item(cardapio):
    try:
        id_item = int(input("Digite o ID do item: "))
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.")
        return

    for item in cardapio:
        if item["id"] == id_item:
            print("Erro: Já existe um item cadastrado com este ID!")
            return

    nome = input("Digite o nome do prato: ").strip().title()

    try:
        preco = float(input("Digite o preço (R$): "))
    except ValueError:
        print("Erro: Preço inválido.")
        return

    cardapio.append({
        "id": id_item,
        "nome": nome,
        "preco": preco
        })
        
    print(f"Item '{nome}' cadastrado com sucesso!")


def remover_item(cardapio):
    try:
        id_item = int(input("Digite o ID do item a ser removido: "))
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.")
        return

    for item in cardapio:
        if item["id"] == id_item:
            cardapio.remove(item)
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