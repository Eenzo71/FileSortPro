import customtkinter as ctk
from tkinter import filedialog
import os

class JanelaConfiguracoes(ctk.CTkToplevel):
    def __init__(self, parent, dados_config, callback_salvar):
        super().__init__(parent)
        self.title("Configurações Gerais")
        self.geometry("600x500")
        
        self.dados = dados_config
        self.callback_salvar = callback_salvar
        # cria uma cópia da lista para não alterar os dados originais antes de salvar
        self.blacklist_atual = list(self.dados['diretorios']['ignorar_pastas'])

        self.grab_set()
        self.focus_force()

        ctk.CTkLabel(self, text="Pastas Ignoradas (Blacklist)", font=("Roboto", 20, "bold")).pack(pady=(20, 5))
        ctk.CTkLabel(self, text="O FileSort Pro NÃO vai tocar nestas pastas nem no que tem dentro delas.", text_color="gray").pack(pady=(0, 20))

        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Lista de Proteção", height=250)
        self.scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.renderizar_lista()

        frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_botoes.pack(padx=20, pady=20, fill="x")

        btn_add = ctk.CTkButton(frame_botoes, text="➕ Adicionar Pasta", fg_color="#444", hover_color="#555", command=self.adicionar_pasta)
        btn_add.pack(side="left", expand=True, fill="x", padx=(0, 10))

        btn_save = ctk.CTkButton(frame_botoes, text="Salvar e Fechar", fg_color="#2cc985", hover_color="#26ab71", font=("Roboto", 14, "bold"), command=self.salvar)
        btn_save.pack(side="left", expand=True, fill="x")

    def renderizar_lista(self):
        # limpa a tela antes de redesenhar a lista
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        for i, pasta in enumerate(self.blacklist_atual):
            frame_item = ctk.CTkFrame(self.scroll_frame, fg_color="#2b2b2b")
            frame_item.pack(fill="x", pady=5, padx=5)

            lbl = ctk.CTkLabel(frame_item, text=f"📂 {pasta}", anchor="w")
            lbl.pack(side="left", padx=10, pady=10)

            # botão de deletar com lambda para identificar qual item apagar
            btn_del = ctk.CTkButton(frame_item, text="🗑️", width=40, fg_color="#c92c2c", hover_color="#ab2626", command=lambda index=i: self.remover_item(index))
            btn_del.pack(side="right", padx=10)

    def adicionar_pasta(self):
        caminho = filedialog.askdirectory()
        if caminho:
            nome_pasta = os.path.basename(caminho)
            if nome_pasta and nome_pasta not in self.blacklist_atual:
                self.blacklist_atual.append(nome_pasta)
                self.renderizar_lista()

    def remover_item(self, index):
        del self.blacklist_atual[index]
        self.renderizar_lista()

    def salvar(self):
        # atualiza o objeto de configuração principal e salva em disco
        self.dados['diretorios']['ignorar_pastas'] = self.blacklist_atual
        
        self.callback_salvar(self.dados)
        self.destroy()