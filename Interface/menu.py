import tkinter as tk

def exibir_menu():
    print("""
    1. Cadastrar Item no Cardápio
    2. Remover Item do Cardápio
    3. Listar Cardápio
    4. Lançar Novo Pedido
    5. Atender Próximo Pedido
    6. Visualizar Fila da Cozinha
    7. Desfazer Última Ação
    8. Visualizar Histórico de Ações
    0. Sair
    """)

def obter_opcao():
    return input("Digite o número da opção desejada: ")

def janelaprincipa():
    """
    explicação do formato e dos comando 
    janela = tk.Tk()
    é a janela principal
    janela.title("Restaurante GreatFillet")
    é o titulo da janela
    janela.geometry("600x400")
    é o tamanho da janela
    """


    janela = tk.Tk()
    janela.title("Restaurante GreatFillet")
    janela.geometry("600x400")
    """
    label_titulo = tk.Label(janela, text="Restaurante GreatFillet", font=("Arial", 24, "bold"))
    é um rótulo que vai mostrar o titulo da janela
    """
    label_titulo = tk.Label(
        janela,
        text="Restaurante GreatFillet",
        font=("Arial", 24, "bold"),
        pady=20
    )
    label_titulo.pack()

    def cadastrar():
        print("Ação: Cadastrar Item")
    
    def remover():
        print("Ação: Remover Item")

    def exibir_cardapio():
        print("Ação: Listar Cardápio")
    
    def lancar_pedido():
        print("Ação: Lançar Pedido")

    def atender_pedido():
        print("Ação: Atender Pedido")

    def mostrar_fila():
        print("Ação: Visualizar Fila")
    
    def desfazer_acao():
        print("Ação: Desfazer Ação")
    
    def exibir_historico():
        print("Ação: Visualizar Histórico")

    def sair():
        janela.destroy()

    """
    btn_cadastrar = tk.Button()
    janela
    é a janela onde vai ser inserido o botão
    text
    é o texto que vai aparecer no botão
    command
    é a função que vai ser chamada quando o botão for clicado
    width
    é a largura do botão
    height
    é a altura do botão
    bg
    é a cor de fundo do botão
    fg
    é a cor do texto do botão
    font
    é a fonte do texto do botão
    pack
    é a função que vai ser chamada para mostrar o botão
    pady
    é o espaçamento entre os botões
    """
    btn_cadastrar = tk.Button(
        janela,
        text="1. Cadastrar Item no Cardápio",
        command=cadastrar,
        width=30,
        height=2,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12)
    )
    btn_cadastrar.pack(pady=5)

    btn_remover = tk.Button(
        janela,
        text="2. Remover Item do Cardápio",
        command=remover,
        width=30,
        height=2,
        bg="#f44336",
        fg="white",
        font=("Arial", 12)
    )
    btn_remover.pack(pady=5)

    btn_exibir = tk.Button(
        janela,
        text="3. Listar Cardápio",
        command=exibir_cardapio,
        width=30,
        height=2,
        bg="#2196F3",
        fg="white",
        font=("Arial", 12)
    )
    btn_exibir.pack(pady=5)

    btn_lancar = tk.Button(
        janela,
        text="4. Lançar Novo Pedido",
        command=lancar_pedido,
        width=30,
        height=2,
        bg="#FF9800",
        fg="white",
        font=("Arial", 12)
    )
    btn_lancar.pack(pady=5)

    btn_atender = tk.Button(
        janela,
        text="5. Atender Próximo Pedido",
        command=atender_pedido,
        width=30,
        height=2,
        bg="#FF5722",
        fg="white",
        font=("Arial", 12)
    )
    btn_atender.pack(pady=5)

    btn_fila = tk.Button(
        janela,
        text="6. Visualizar Fila da Cozinha",
        command=mostrar_fila,
        width=30,
        height=2,
        bg="#9C27B0",
        fg="white",
        font=("Arial", 12)
    )
    btn_fila.pack(pady=5)

    btn_desfazer = tk.Button(
        janela,
        text="7. Desfazer Última Ação",
        command=desfazer_acao,
        width=30,
        height=2,
        bg="#607D8B",
        fg="white",
        font=("Arial", 12)
    )
    btn_desfazer.pack(pady=5)

    btn_historico = tk.Button(
        janela,
        text="8. Visualizar Histórico de Ações",
        command=exibir_historico,
        width=30,
        height=2,
        bg="#00BCD4",
        fg="white",
        font=("Arial", 12)
    )
    btn_historico.pack(pady=5)

    btn_sair = tk.Button(
        janela,
        text="0. Sair",
        command=sair,
        width=30,
        height=2,
        bg="#f44336",
        fg="white",
        font=("Arial", 12)
    )
    btn_sair.pack(pady=5)

    
    janela.mainloop()
    
