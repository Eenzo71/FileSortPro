# 📂 FileSort Pro

> Um organizador de arquivos inteligente, visual e automatizado feito em Python.

![Badge Status](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)
![Badge Python](http://img.shields.io/static/v1?label=Python&message=3.14&color=blue&style=for-the-badge)
![Badge License](http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge)

## 💻 Sobre o projeto

O **FileSort Pro** é uma aplicação Desktop moderna desenvolvida para acabar com o caos da pasta "Downloads" ou de qualquer diretório do seu computador.

Diferente de scripts simples, ele oferece uma **Interface Gráfica (GUI)** completa, roda em **segundo plano** (System Tray) e gera um **Dashboard de Relatórios** visual em HTML para você saber exatamente o que foi organizado.

---

## ⚙️ Funcionalidades Principais

- [x] **Organização Inteligente:** Move arquivos automaticamente baseando-se na extensão (PDFs para Documentos, JPGs para Imagens, etc).
- [x] **Modo Background:** Minimiza para a bandeja do sistema (Tray Icon) e organiza a pasta automaticamente a cada 60 segundos.
- [x] **Dashboard HTML:** Gera gráficos visuais (Rosca e Linha do tempo) mostrando o volume de arquivos organizados.
- [x] **Editor de Regras:** Interface visual com checkboxes para escolher quais extensões ativar ou desativar.
- [x] **Auto-Configuração:** Detecta automaticamente a pasta "Documentos" do usuário para salvar os arquivos organizados.
- [x] **Blacklist (Proteção):** Impede que o programa toque em pastas sensíveis (ex: Jogos, Windows).
- [x] **Resiliência:** Sistema de auto-reparo do arquivo `config.json` caso ele seja corrompido.

---

## 🛠 Tecnologias Utilizadas

* **Python 3.x** - Linguagem base.
* **CustomTkinter** - Interface gráfica moderna (Dark Mode nativo).
* **Pystray & Pillow** - Para o ícone de bandeja e execução em segundo plano.
* **JSON** - Persistência de dados e configurações.
* **HTML/JS (Chart.js)** - Dashboard de relatórios offline.
* **Threading** - Para execução fluida sem travar a interface.