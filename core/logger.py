import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
HISTORY_FILE = os.path.join(LOGS_DIR, 'historico_global.json')

os.makedirs(LOGS_DIR, exist_ok=True)

def registrar_log_txt(mensagem):
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    arquivo_log = os.path.join(LOGS_DIR, f"log_{data_hoje}.txt")
    
    hora_agora = datetime.now().strftime("%H:%M:%S")
    linha = f"[{hora_agora}] {mensagem}\n"
    
    try:
        with open(arquivo_log, 'a', encoding='utf-8') as f:
            f.write(linha)
    except Exception as e:
        print(f"Erro ao gravar log TXT: {e}")

def atualizar_historico_json(dados_execucao):
    # salva os dados numerics
    historico = []

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                historico = json.load(f)
        except:
            historico = []

    dados_completos = {
        "timestamp": datetime.now().isoformat(),
        "data_legivel": datetime.now().strftime("%d/%m/%Y"),
        "hora_legivel": datetime.now().strftime("%H:%M"),
        **dados_execucao # mescla com os dados passados
    }

    historico.append(dados_completos)

    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(historico, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar histórico JSON: {e}")

def gerar_dashboard_html():
    # lê o template e gera o HTML final (substitui o marcador {{DADOS_JSON}})
    template_path = os.path.join(BASE_DIR, 'assets', 'dashboard_template.html')
    output_path = os.path.join(BASE_DIR, 'Relatorio_Dashboard.html')
    
    if not os.path.exists(HISTORY_FILE):
        print("Nenhum histórico para gerar dashboard.")
        return

    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            dados_json = f.read()
            
        if not os.path.exists(template_path):
            print("Erro: Template HTML não encontrado em assets/.")
            return

        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # injeção de dados no HTML
        html_final = template_content.replace('{{DADOS_JSON}}', dados_json)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_final)
            
        print(f"\n[DASHBOARD] Relatório gerado com sucesso: {output_path}")

    except Exception as e:
        print(f"Erro ao gerar dashboard: {e}")