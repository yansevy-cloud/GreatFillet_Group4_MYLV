from Interface.menu import janelaprincipa
from Fila import Fila
from Pilha import Pilha


def main():
    cardapio = []
    fila_cozinha = Fila()
    pilha_historico = Pilha()

    janelaprincipa(cardapio, fila_cozinha, pilha_historico)


if __name__ == "__main__":
    main()