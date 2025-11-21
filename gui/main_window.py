import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import threading
import time
from PIL import Image, ImageDraw 
import pystray 
import sys
import os

from core.organizador import organizar_pasta
from core.utils import carregar_configuracoes, salvar_configuracoes
from core.logger import registrar_log_txt, gerar_dashboard_html
from gui.components.config_window import JanelaConfiguracoes
from gui.components.editor_window import JanelaEditor 

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class FileSortApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("FileSort Pro - 2025")
        self.geometry("900x700")
        self.minsize(800, 600)

        # intercepta o evento de clicar no X da janela
        self.protocol("WM_DELETE_WINDOW", self.ao_tentar_fechar)

        self.config_dados = carregar_configuracoes()
        self.checkboxes_vars = {} 
        self.monitoramento_ativo = False 

        # Interface
        self.criar_topo()
        self.criar_area_central()
        self.criar_console_logs()
        self.criar_rodape()
        
        # inicia o ícone na bandeja imediatamente
        self.iniciar_tray_icon()
        
        # inicia o loop que verifica se deve organizar automaticamente
        self.after(1000, self.loop_monitoramento)

    def criar_topo(self):
        frame_topo = ctk.CTkFrame(self)
        frame_topo.pack(pady=20, padx=20, fill="x")

        self.label_titulo = ctk.CTkLabel(frame_topo, text="Pasta Alvo:", font=("Roboto", 14))
        self.label_titulo.pack(side="left", padx=10)

        self.entry_caminho = ctk.CTkEntry(frame_topo, placeholder_text="Selecione a pasta...", width=350)
        self.entry_caminho.pack(side="left", padx=10, fill="x", expand=True)

        btn_selecionar = ctk.CTkButton(frame_topo, text="📂 Buscar", width=80, command=self.selecionar_pasta)
        btn_selecionar.pack(side="left", padx=5)

        btn_config = ctk.CTkButton(frame_topo, text="⚙️", width=40, fg_color="#444", hover_color="#666", command=self.abrir_configs)
        btn_config.pack(side="right", padx=5)

    def criar_area_central(self):
        # se o frame já existir (atualização), destrói para recriar
        if hasattr(self, 'frame_meio'):
            self.frame_meio.destroy()

        self.frame_meio = ctk.CTkFrame(self)
        self.frame_meio.pack(pady=10, padx=20, fill="both", expand=True)

        # ativar/desativar automação
        self.frame_switch = ctk.CTkFrame(self.frame_meio, fg_color="transparent")
        self.frame_switch.pack(pady=(15, 5))
        
        self.switch_var = ctk.BooleanVar(value=False)
        self.switch_monitor = ctk.CTkSwitch(self.frame_switch, text="ATIVAR MONITORAMENTO EM SEGUNDO PLANO (Automático)", 
                                            variable=self.switch_var, font=("Roboto", 14, "bold"), 
                                            command=self.toggle_monitoramento, progress_color="#2cc985")
        self.switch_monitor.pack()
        
        lbl_info = ctk.CTkLabel(self.frame_switch, text="(Organiza automaticamente a cada 60 segundos enquanto minimizado)", font=("Arial", 10), text_color="gray")
        lbl_info.pack()

        ctk.CTkLabel(self.frame_meio, text="_______________________________________________________", text_color="#444").pack(pady=5)

        lbl_filtro = ctk.CTkLabel(self.frame_meio, text="Categorias Ativas:", font=("Roboto", 16, "bold"))
        lbl_filtro.pack(pady=10)

        self.frame_checks = ctk.CTkFrame(self.frame_meio, fg_color="transparent")
        self.frame_checks.pack(pady=10)

        # cria checkboxes dinamicamente baseado no JSON
        regras = self.config_dados.get('regras', {})
        coluna = 0
        linha = 0
        
        for categoria, dados in regras.items():
            is_ativo = dados.get('ativo', True)
            var = ctk.BooleanVar(value=is_ativo)
            self.checkboxes_vars[categoria] = var

            chk = ctk.CTkCheckBox(self.frame_checks, text=categoria, variable=var, command=self.salvar_estado_checkbox)
            chk.grid(row=linha, column=coluna, padx=20, pady=10, sticky="w")
            
            # editar extensões
            btn_detalhe = ctk.CTkButton(self.frame_checks, text="...", width=30, height=20, fg_color="transparent", border_width=1, text_color="gray", 
                                      command=lambda c=categoria: self.abrir_editor_categoria(c))
            btn_detalhe.grid(row=linha, column=coluna+1, padx=(0, 20))

            coluna += 2
            if coluna >= 6:
                coluna = 0
                linha += 1

    def criar_console_logs(self):
        lbl_log = ctk.CTkLabel(self, text="Console de Execução:", anchor="w")
        lbl_log.pack(padx=20, pady=(10, 0), fill="x")

        self.textbox_log = ctk.CTkTextbox(self, height=100)
        self.textbox_log.pack(padx=20, pady=10, fill="x")
        self.textbox_log.configure(state="disabled")

    def criar_rodape(self):
        self.btn_organizar = ctk.CTkButton(self, text="ORGANIZAR AGORA (Manual)", height=50, font=("Roboto", 18, "bold"), fg_color="#2291e6", hover_color="#1a7ac2", command=self.iniciar_organizacao)
        self.btn_organizar.pack(padx=20, pady=20, fill="x")
        
        btn_dashboard = ctk.CTkButton(self, text="📊 Ver Relatório Gráfico", fg_color="transparent", border_width=1, text_color="#ccc", command=self.abrir_dashboard)
        btn_dashboard.pack(pady=(0, 20))


    def toggle_monitoramento(self):
        if self.switch_var.get():
            self.monitoramento_ativo = True
            self.log_na_tela("🟢 Monitoramento Automático INICIADO.")
            self.log_na_tela("O sistema irá organizar a pasta a cada 60 segundos.")
        else:
            self.monitoramento_ativo = False
            self.log_na_tela("🔴 Monitoramento PAUSADO.")

    def loop_monitoramento(self):
        if self.monitoramento_ativo:
            caminho = self.entry_caminho.get()
            if caminho:
                # thread para não travar a interface
                threading.Thread(target=lambda: organizar_pasta(caminho)).start()
        
        self.after(60000, self.loop_monitoramento)


    def iniciar_tray_icon(self):
        try:
            image = Image.open("assets/app.png")
        except:
            # ícone colorido se a imagem falhar
            image = Image.new('RGB', (64, 64), color="#2b2b2b") 
            d = ImageDraw.Draw(image)
            d.rectangle([(16, 16), (48, 48)], fill="#2cc985")

        menu = (pystray.MenuItem('Mostrar Janela do Filesort Pro', self.restaurar_janela),
                pystray.MenuItem('Sair', self.sair_app))
        
        self.tray_icon = pystray.Icon("FileSortPro", image, "FileSort Pro", menu)
        
        # ícone em thread separada para não bloquear o app principal
        threading.Thread(target=self.tray_icon.run, daemon=True).start()

    def ao_tentar_fechar(self):
        self.withdraw() 

    def restaurar_janela(self, icon, item):
        self.deiconify()
        self.lift()
        self.focus_force()

    def sair_app(self, icon, item):
        self.tray_icon.stop()
        self.quit()
        self.destroy()
        os._exit(0)

    def abrir_editor_categoria(self, categoria):
        dados = self.config_dados['regras'][categoria]
        JanelaEditor(self, categoria, dados, self.salvar_edicao_categoria)

    def salvar_edicao_categoria(self, categoria, novos_dados):
        self.config_dados['regras'][categoria] = novos_dados
        if salvar_configuracoes(self.config_dados):
            self.log_na_tela(f"✅ Categoria '{categoria}' atualizada!")
            self.criar_area_central()
        else:
            self.log_na_tela("❌ Erro ao salvar configurações.")

    def abrir_configs(self):
        JanelaConfiguracoes(self, self.config_dados, self.salvar_configuracoes_gerais)

    def salvar_configuracoes_gerais(self, novos_dados_completos):
        self.config_dados = novos_dados_completos
        if salvar_configuracoes(self.config_dados):
            self.log_na_tela("✅ Configurações globais salvas!")
        else:
            self.log_na_tela("❌ Erro ao salvar.")

    def salvar_estado_checkbox(self):
        for cat, var in self.checkboxes_vars.items():
            self.config_dados['regras'][cat]['ativo'] = var.get()
        salvar_configuracoes(self.config_dados)

    def log_na_tela(self, mensagem):
        self.textbox_log.configure(state="normal")
        self.textbox_log.insert("end", mensagem + "\n")
        self.textbox_log.see("end")
        self.textbox_log.configure(state="disabled")

    def selecionar_pasta(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.entry_caminho.delete(0, "end")
            self.entry_caminho.insert(0, pasta)
            self.log_na_tela(f"Pasta selecionada: {pasta}")

    def abrir_dashboard(self):
        import os
        import webbrowser
        if os.path.exists("Relatorio_Dashboard.html"):
            webbrowser.open("Relatorio_Dashboard.html")
            self.log_na_tela("Abrindo dashboard...")
        else:
            self.log_na_tela("Erro: Nenhum relatório encontrado.")

    def iniciar_organizacao(self):
        caminho = self.entry_caminho.get()
        if not caminho:
            self.log_na_tela("❌ Erro: Selecione uma pasta primeiro.")
            return

        self.log_na_tela("--- Iniciando Processo Manual... ---")
        self.btn_organizar.configure(state="disabled", text="Processando...")
        threading.Thread(target=self.processo_background, args=(caminho,)).start()

    def processo_background(self, caminho):
        try:
            organizar_pasta(caminho)
            gerar_dashboard_html()
            self.log_na_tela("✅ Sucesso! Pasta organizada.")
        except Exception as e:
            self.log_na_tela(f"❌ Erro crítico: {e}")
        finally:
            self.btn_organizar.configure(state="normal", text="ORGANIZAR AGORA (Manual)")

if __name__ == "__main__":
    app = FileSortApp()
    app.mainloop()