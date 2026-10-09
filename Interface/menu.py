import io
import tkinter as tk
from contextlib import redirect_stdout
from tkinter import ttk, messagebox

from cardapio import buscar_item
from historico import registrar_acao, desfazer_ultima_acao


# ----------------------------------------------------------------------
# Funções do menu de console (mantidas apenas por compatibilidade)
# ----------------------------------------------------------------------
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


# ----------------------------------------------------------------------
# Interface gráfica
# ----------------------------------------------------------------------
COR_FUNDO = "#F5F1EA"
COR_TITULO = "#1F3A4D"
COR_OK = "#2E7D32"
COR_ERRO = "#C62828"
COR_AVISO = "#EF6C00"
COR_INFO = "#1F3A4D"


class AppRestaurante:
    """Janela principal. Recebe as estruturas de dados já criadas no main:
    - cardapio: list nativa
    - fila_cozinha: classe Fila
    - pilha_historico: classe Pilha
    A lógica das estruturas continua nos módulos originais; aqui fica só a tela.
    """

    def __init__(self, cardapio, fila_cozinha, pilha_historico):
        self.cardapio = cardapio
        self.fila = fila_cozinha
        self.pilha = pilha_historico
        self.itens_pedido = []  # IDs do pedido que está sendo montado

        self.janela = tk.Tk()
        self.janela.title("RESTAURANTE GREAT FILLET")
        self.janela.geometry("980x680")
        self.janela.minsize(900, 620)
        self.janela.configure(bg=COR_FUNDO)

        self._estilos()
        self._montar_cabecalho()
        self._montar_status()  # antes das abas, para o rodapé reservar espaço
        self._montar_abas()
        self.atualizar_tudo()

    # ------------------------------------------------------------------
    # Montagem da tela
    # ------------------------------------------------------------------
    def _estilos(self):
        estilo = ttk.Style(self.janela)
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass
        estilo.configure("TNotebook", background=COR_FUNDO)
        estilo.configure("TNotebook.Tab", padding=(18, 8), font=("Arial", 11, "bold"))
        estilo.configure("TFrame", background=COR_FUNDO)
        estilo.configure("TLabelframe", background=COR_FUNDO)
        estilo.configure("TLabelframe.Label", background=COR_FUNDO,
                         font=("Arial", 11, "bold"), foreground=COR_TITULO)
        estilo.configure("TLabel", background=COR_FUNDO, font=("Arial", 11))
        estilo.configure("Treeview", rowheight=26, font=("Arial", 10))
        estilo.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    def _botao(self, pai, texto, comando, cor):
        return tk.Button(
            pai, text=texto, command=comando, bg=cor, fg="white",
            activebackground=cor, activeforeground="white",
            font=("Arial", 11, "bold"), relief="flat", padx=12, pady=6,
            cursor="hand2",
        )

    def _montar_cabecalho(self):
        topo = tk.Frame(self.janela, bg=COR_TITULO)
        topo.pack(fill="x")
        tk.Label(
            topo, text="RESTAURANTE GREAT FILLET",
            font=("Arial", 22, "bold"), bg=COR_TITULO, fg="white", pady=14,
        ).pack()

    def _montar_status(self):
        rodape = tk.Frame(self.janela, bg="white", bd=1, relief="solid")
        rodape.pack(side="bottom", fill="x")
        self.var_status = tk.StringVar(value="Sistema pronto.")
        self.lbl_status = tk.Label(
            rodape, textvariable=self.var_status, anchor="w",
            font=("Arial", 11), bg="white", fg=COR_INFO, padx=10, pady=8,
        )
        self.lbl_status.pack(fill="x")

    def _montar_abas(self):
        self.abas = ttk.Notebook(self.janela)
        self.abas.pack(fill="both", expand=True, padx=10, pady=10)

        self.aba_cardapio = ttk.Frame(self.abas, padding=10)
        self.aba_cozinha = ttk.Frame(self.abas, padding=10)
        self.aba_historico = ttk.Frame(self.abas, padding=10)

        self.abas.add(self.aba_cardapio, text="Cardápio (list)")
        self.abas.add(self.aba_cozinha, text="Cozinha & Pedidos (Fila)")
        self.abas.add(self.aba_historico, text="Histórico (Pilha)")

        self._montar_aba_cardapio()
        self._montar_aba_cozinha()
        self._montar_aba_historico()

    # ----- Aba Cardápio ------------------------------------------------
    def _montar_aba_cardapio(self):
        form = ttk.LabelFrame(self.aba_cardapio, text="Cadastrar item", padding=10)
        form.pack(fill="x")

        self.var_id = tk.StringVar()
        self.var_nome = tk.StringVar()
        self.var_preco = tk.StringVar()

        ttk.Label(form, text="ID:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(form, textvariable=self.var_id, width=10).grid(row=0, column=1, padx=5)

        ttk.Label(form, text="Nome:").grid(row=0, column=2, sticky="e", padx=5)
        ttk.Entry(form, textvariable=self.var_nome, width=30).grid(row=0, column=3, padx=5)

        ttk.Label(form, text="Preço (R$):").grid(row=0, column=4, sticky="e", padx=5)
        ttk.Entry(form, textvariable=self.var_preco, width=12).grid(row=0, column=5, padx=5)

        self._botao(form, "Cadastrar", self.cadastrar_item, "#4CAF50").grid(
            row=0, column=6, padx=(15, 5))

        tabela = ttk.LabelFrame(self.aba_cardapio, text="Itens do cardápio", padding=10)
        tabela.pack(fill="both", expand=True, pady=(10, 0))

        self.tree_cardapio = ttk.Treeview(
            tabela, columns=("id", "nome", "preco"), show="headings",
            selectmode="browse",
        )
        self.tree_cardapio.heading("id", text="ID")
        self.tree_cardapio.heading("nome", text="Prato")
        self.tree_cardapio.heading("preco", text="Preço")
        self.tree_cardapio.column("id", width=80, anchor="center")
        self.tree_cardapio.column("nome", width=400)
        self.tree_cardapio.column("preco", width=120, anchor="e")

        barra = ttk.Scrollbar(tabela, orient="vertical", command=self.tree_cardapio.yview)
        self.tree_cardapio.configure(yscrollcommand=barra.set)
        self.tree_cardapio.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        botoes = tk.Frame(self.aba_cardapio, bg=COR_FUNDO)
        botoes.pack(fill="x", pady=(10, 0))
        self._botao(botoes, "Remover item selecionado", self.remover_item, "#f44336").pack(side="left")

    # ----- Aba Cozinha -------------------------------------------------
    def _montar_aba_cozinha(self):
        esquerda = ttk.LabelFrame(self.aba_cozinha, text="Lançar novo pedido", padding=10)
        esquerda.pack(side="left", fill="both", expand=True, padx=(0, 5))

        direita = ttk.LabelFrame(self.aba_cozinha, text="Fila da cozinha (FIFO)", padding=10)
        direita.pack(side="left", fill="both", expand=True, padx=(5, 0))

        # --- formulário de pedido
        linha = tk.Frame(esquerda, bg=COR_FUNDO)
        linha.pack(fill="x")
        ttk.Label(linha, text="Cliente:").pack(side="left")
        self.var_cliente = tk.StringVar()
        ttk.Entry(linha, textvariable=self.var_cliente, width=30).pack(
            side="left", padx=8, fill="x", expand=True)

        ttk.Label(esquerda, text="Cardápio (selecione um ou mais itens):").pack(
            anchor="w", pady=(10, 2))

        frame_card = tk.Frame(esquerda, bg=COR_FUNDO)
        frame_card.pack(fill="both", expand=True)
        self.tree_cardapio_pedido = ttk.Treeview(
            frame_card, columns=("id", "nome", "preco"), show="headings",
            selectmode="extended", height=5,
        )
        self.tree_cardapio_pedido.heading("id", text="ID")
        self.tree_cardapio_pedido.heading("nome", text="Prato")
        self.tree_cardapio_pedido.heading("preco", text="Preço")
        self.tree_cardapio_pedido.column("id", width=50, anchor="center")
        self.tree_cardapio_pedido.column("nome", width=170)
        self.tree_cardapio_pedido.column("preco", width=80, anchor="e")
        b1 = ttk.Scrollbar(frame_card, orient="vertical",
                           command=self.tree_cardapio_pedido.yview)
        self.tree_cardapio_pedido.configure(yscrollcommand=b1.set)
        self.tree_cardapio_pedido.pack(side="left", fill="both", expand=True)
        b1.pack(side="right", fill="y")

        self._botao(esquerda, "Adicionar ao pedido ↓", self.adicionar_ao_pedido,
                    "#2196F3").pack(fill="x", pady=8)

        ttk.Label(esquerda, text="Itens do pedido atual:").pack(anchor="w")
        frame_lista = tk.Frame(esquerda, bg=COR_FUNDO)
        frame_lista.pack(fill="both", expand=True)
        self.lista_pedido = tk.Listbox(frame_lista, height=5, font=("Arial", 10),
                                       selectmode="browse")
        b2 = ttk.Scrollbar(frame_lista, orient="vertical", command=self.lista_pedido.yview)
        self.lista_pedido.configure(yscrollcommand=b2.set)
        self.lista_pedido.pack(side="left", fill="both", expand=True)
        b2.pack(side="right", fill="y")

        botoes = tk.Frame(esquerda, bg=COR_FUNDO)
        botoes.pack(fill="x", pady=(8, 0))
        self._botao(botoes, "Remover do pedido", self.remover_do_pedido,
                    "#607D8B").pack(side="left")
        self._botao(botoes, "Lançar pedido", self.lancar_pedido,
                    "#FF9800").pack(side="right")

        # --- fila
        frame_fila = tk.Frame(direita, bg=COR_FUNDO)
        frame_fila.pack(fill="both", expand=True)
        self.tree_fila = ttk.Treeview(
            frame_fila, columns=("pos", "cliente", "itens"), show="headings",
            selectmode="none",
        )
        self.tree_fila.heading("pos", text="Nº")
        self.tree_fila.heading("cliente", text="Cliente")
        self.tree_fila.heading("itens", text="Itens")
        self.tree_fila.column("pos", width=40, anchor="center")
        self.tree_fila.column("cliente", width=110)
        self.tree_fila.column("itens", width=220)
        b3 = ttk.Scrollbar(frame_fila, orient="vertical", command=self.tree_fila.yview)
        self.tree_fila.configure(yscrollcommand=b3.set)
        self.tree_fila.pack(side="left", fill="both", expand=True)
        b3.pack(side="right", fill="y")

        self.var_tamanho_fila = tk.StringVar()
        ttk.Label(direita, textvariable=self.var_tamanho_fila).pack(anchor="w", pady=(8, 0))
        self._botao(direita, "Atender Próximo Pedido", self.atender_pedido,
                    "#FF5722").pack(fill="x", pady=(8, 0))

    # ----- Aba Histórico -----------------------------------------------
    def _montar_aba_historico(self):
        topo = tk.Frame(self.aba_historico, bg=COR_FUNDO)
        topo.pack(fill="x")
        self._botao(topo, "Desfazer Última Ação", self.desfazer_acao,
                    "#607D8B").pack(side="left")
        self.var_tamanho_pilha = tk.StringVar()
        ttk.Label(topo, textvariable=self.var_tamanho_pilha).pack(side="left", padx=15)

        quadro = ttk.LabelFrame(
            self.aba_historico,
            text="Histórico de ações (mais recente no topo - LIFO)", padding=10)
        quadro.pack(fill="both", expand=True, pady=(10, 0))

        self.tree_historico = ttk.Treeview(
            quadro, columns=("pos", "tipo", "dados"), show="headings",
            selectmode="none",
        )
        self.tree_historico.heading("pos", text="Nº")
        self.tree_historico.heading("tipo", text="Ação")
        self.tree_historico.heading("dados", text="Dados")
        self.tree_historico.column("pos", width=50, anchor="center")
        self.tree_historico.column("tipo", width=170)
        self.tree_historico.column("dados", width=600)
        b = ttk.Scrollbar(quadro, orient="vertical", command=self.tree_historico.yview)
        self.tree_historico.configure(yscrollcommand=b.set)
        self.tree_historico.pack(side="left", fill="both", expand=True)
        b.pack(side="right", fill="y")

    # ------------------------------------------------------------------
    # Mensagens
    # ------------------------------------------------------------------
    def _status(self, texto, cor=COR_INFO):
        self.var_status.set(texto)
        self.lbl_status.configure(fg=cor)

    def _erro(self, texto):
        self._status("Erro: " + texto, COR_ERRO)
        messagebox.showerror("Erro", texto, parent=self.janela)

    def _aviso(self, texto):
        self._status("Aviso: " + texto, COR_AVISO)
        messagebox.showwarning("Aviso", texto, parent=self.janela)

    # ------------------------------------------------------------------
    # Atualização das listas visuais
    # ------------------------------------------------------------------
    def atualizar_tudo(self):
        self.atualizar_cardapio()
        self.atualizar_fila()
        self.atualizar_historico()

    def atualizar_cardapio(self):
        for tree in (self.tree_cardapio, self.tree_cardapio_pedido):
            tree.delete(*tree.get_children())
            for item in self.cardapio:
                tree.insert("", "end", values=(
                    item["id"], item["nome"], f"R$ {item['preco']:.2f}"))

    def _descrever_itens(self, ids):
        partes = []
        for id_item in ids:
            item = buscar_item(self.cardapio, id_item)
            nome = item["nome"] if item else "(removido)"
            partes.append(f"{id_item}-{nome}")
        return ", ".join(partes)

    def atualizar_fila(self):
        self.tree_fila.delete(*self.tree_fila.get_children())
        for i, pedido in enumerate(self.fila._pacientes, start=1):
            self.tree_fila.insert("", "end", values=(
                i, pedido["CLIENTE"], self._descrever_itens(pedido["PEDIDOS"])))
        self.var_tamanho_fila.set(f"Pedidos aguardando: {self.fila.size()}")

    def atualizar_historico(self):
        self.tree_historico.delete(*self.tree_historico.get_children())
        total = self.pilha.size()
        for i, acao in enumerate(reversed(self.pilha._elementos), start=1):
            self.tree_historico.insert("", "end", values=(
                i, acao["tipo"], acao["dados"]))
        self.var_tamanho_pilha.set(f"Ações registradas: {total}")

    def atualizar_pedido_atual(self):
        self.lista_pedido.delete(0, "end")
        for id_item in self.itens_pedido:
            item = buscar_item(self.cardapio, id_item)
            nome = item["nome"] if item else "(removido)"
            self.lista_pedido.insert("end", f"{id_item} - {nome}")

    # ------------------------------------------------------------------
    # Ações: Cardápio
    # ------------------------------------------------------------------
    def cadastrar_item(self):
        try:
            id_item = int(self.var_id.get().strip())
        except ValueError:
            self._erro("O ID deve ser um número inteiro.")
            return

        if buscar_item(self.cardapio, id_item) is not None:
            self._erro("Já existe um item cadastrado com este ID!")
            return

        nome = self.var_nome.get().strip().title()
        if not nome:
            self._erro("O nome do prato não pode estar em branco.")
            return

        try:
            preco = float(self.var_preco.get().strip().replace(",", "."))
        except ValueError:
            self._erro("Preço inválido.")
            return
        if preco <= 0:
            self._erro("O preço deve ser maior que zero.")
            return

        self.cardapio.append({"id": id_item, "nome": nome, "preco": preco})
        registrar_acao(self.pilha, "cadastrar_item", self.cardapio[-1])

        self.var_id.set("")
        self.var_nome.set("")
        self.var_preco.set("")
        self.atualizar_tudo()
        self._status(f"Item '{nome}' cadastrado com sucesso!", COR_OK)

    def remover_item(self):
        selecao = self.tree_cardapio.selection()
        if not selecao:
            self._aviso("Selecione um item na lista para remover.")
            return

        id_item = int(self.tree_cardapio.item(selecao[0], "values")[0])
        item = buscar_item(self.cardapio, id_item)
        if item is None:
            self._erro("Item com este ID não foi encontrado no cardápio.")
            self.atualizar_tudo()
            return

        if not messagebox.askyesno(
                "Confirmar", f"Remover '{item['nome']}' do cardápio?",
                parent=self.janela):
            return

        item_removido = item.copy()
        self.cardapio.remove(item)
        registrar_acao(self.pilha, "remover_item", item_removido)

        self.itens_pedido = [i for i in self.itens_pedido if i != id_item]
        self.atualizar_pedido_atual()
        self.atualizar_tudo()
        self._status(f"Item ID {id_item} removido com sucesso!", COR_OK)

    # ------------------------------------------------------------------
    # Ações: Pedidos / Cozinha
    # ------------------------------------------------------------------
    def adicionar_ao_pedido(self):
        selecao = self.tree_cardapio_pedido.selection()
        if not selecao:
            self._aviso("Selecione ao menos um item do cardápio.")
            return

        for linha in selecao:
            id_item = int(self.tree_cardapio_pedido.item(linha, "values")[0])
            if buscar_item(self.cardapio, id_item) is None:
                self._erro(f"ID {id_item} não encontrado no cardápio!")
                continue
            self.itens_pedido.append(id_item)

        self.atualizar_pedido_atual()
        self._status("Item(ns) adicionado(s) ao pedido.", COR_INFO)

    def remover_do_pedido(self):
        selecao = self.lista_pedido.curselection()
        if not selecao:
            self._aviso("Selecione um item do pedido para remover.")
            return
        self.itens_pedido.pop(selecao[0])
        self.atualizar_pedido_atual()

    def lancar_pedido(self):
        nome = self.var_cliente.get().strip().title()
        if not nome:
            self._erro("Informe o nome do cliente.")
            return
        if not self.itens_pedido:
            self._erro("Adicione ao menos um item ao pedido.")
            return

        pedido = {"CLIENTE": nome, "PEDIDOS": list(self.itens_pedido)}
        self.fila.entrar(pedido)
        registrar_acao(self.pilha, "lancar_pedido", pedido)

        self.var_cliente.set("")
        self.itens_pedido = []
        self.atualizar_pedido_atual()
        self.atualizar_tudo()
        self._status(f"Pedido do cliente '{nome}' enviado para a cozinha!", COR_OK)

    def atender_pedido(self):
        if self.fila.isEmpty():
            self._aviso("Não há pedidos para atender.")
            return

        pedido = self.fila.chamar()
        if pedido is None:
            self._erro("Não foi possível obter o pedido.")
            return

        registrar_acao(self.pilha, "atender_pedido", pedido)
        self.atualizar_tudo()

        itens = self._descrever_itens(pedido["PEDIDOS"])
        self._status(
            f"Pedido atendido: CLIENTE -> {pedido['CLIENTE']} | PEDIDOS -> {pedido['PEDIDOS']}",
            COR_OK)
        messagebox.showinfo(
            "Pedido atendido",
            f"Cliente: {pedido['CLIENTE']}\nItens: {itens}",
            parent=self.janela)

    # ------------------------------------------------------------------
    # Ações: Histórico
    # ------------------------------------------------------------------
    def desfazer_acao(self):
        if self.pilha.isEmpty():
            self._aviso("Não há ações para desfazer.")
            return

        # A função original usa print(); capturamos o texto para mostrar na tela.
        saida = io.StringIO()
        with redirect_stdout(saida):
            desfazer_ultima_acao(self.pilha, self.fila, self.cardapio)
        mensagem = saida.getvalue().strip() or "Ação desfeita."

        self.atualizar_tudo()
        self.atualizar_pedido_atual()
        self._status(mensagem, COR_OK)

    # ------------------------------------------------------------------
    def executar(self):
        self.janela.mainloop()


def janelaprincipa(cardapio, fila_cozinha, pilha_historico):
    app = AppRestaurante(cardapio, fila_cozinha, pilha_historico)
    app.executar()