import os
import shutil
from pathlib import Path
from .utils import carregar_configuracoes, resolver_conflito
from .logger import registrar_log_txt, atualizar_historico_json

def organizar_pasta(caminho_base):
    config = carregar_configuracoes()
    if not config:
        return

    caminho_base = str(Path(caminho_base))
    blacklist = config['diretorios']['ignorar_pastas']
    regras = config['regras']
    
    # --- caminho ---
    destino_raw = config['diretorios']['padrao_destino']
    
    if destino_raw is None:
        caminho_docs_sistema = os.path.join(os.path.expanduser("~"), "Documents")
        destino_padrao_root = os.path.join(caminho_docs_sistema, "FileSort_Organizado")
    else:
        destino_padrao_root = destino_raw

    registrar_log_txt(f"--- INICIO DA OPERAÇÃO EM: {caminho_base} ---")
    print(f"--- Iniciando organização em: {caminho_base} ---")

    stats_total_movidos = 0
    stats_por_categoria = {}
    stats_bytes_movidos = 0

    # os.walk percorre todas as subpastas recursivamente
    for root, dirs, files in os.walk(caminho_base):
        # modifica a lista 'dirs' para impedir que o loop entre nas pastas da Blacklist
        dirs[:] = [d for d in dirs if d not in blacklist]

        for arquivo in files:
            caminho_completo_origem = os.path.join(root, arquivo)
            nome_arquivo_lower = arquivo.lower()
            _, extensao = os.path.splitext(nome_arquivo_lower)

            # verifica a extensão e a categoria correspondente
            categoria_encontrada = None
            config_categoria = None
            for nome_cat, dados in regras.items():
                if dados['ativo'] and extensao in dados['extensoes']:
                    categoria_encontrada = nome_cat
                    config_categoria = dados
                    break
            
            if not categoria_encontrada:
                continue

            # define qual destino usar
            if config_categoria['caminho_personalizado']:
                destino_base = config_categoria['caminho_personalizado']
            else:
                destino_base = os.path.join(destino_padrao_root, categoria_encontrada)

            # mantém a estrutura de pastas
            caminho_relativo = os.path.relpath(root, caminho_base)
            if caminho_relativo == ".":
                pasta_final = destino_base
            else:
                pasta_final = os.path.join(destino_base, caminho_relativo)

            os.makedirs(pasta_final, exist_ok=True)

            caminho_destino_final = os.path.join(pasta_final, arquivo)
            
            # resolve conflito de nomes
            if os.path.exists(caminho_destino_final):
                caminho_destino_final = resolver_conflito(caminho_destino_final, caminho_completo_origem)

            try:
                tamanho_arquivo = os.path.getsize(caminho_completo_origem)
                
                shutil.move(caminho_completo_origem, caminho_destino_final)
                
                # atualiza a estatística para o deshboard
                stats_total_movidos += 1
                stats_bytes_movidos += tamanho_arquivo
                stats_por_categoria[categoria_encontrada] = stats_por_categoria.get(categoria_encontrada, 0) + 1
                
                msg = f"Movido: {arquivo} -> {categoria_encontrada} (Destino: {caminho_destino_final})"
                print(f"[SUCESSO] {msg}")
                registrar_log_txt(msg)

            except Exception as e:
                erro_msg = f"Falha ao mover {arquivo}: {e}"
                print(f"[ERRO] {erro_msg}")
                registrar_log_txt(f"[ERRO] {erro_msg}")

    # salva no json depois de finalizar
    if stats_total_movidos > 0:
        dados_final = {
            "total_movidos": stats_total_movidos,
            "categorias": stats_por_categoria,
            "tamanho_total_bytes": stats_bytes_movidos,
            "pasta_origem": caminho_base
        }
        atualizar_historico_json(dados_final)
        registrar_log_txt(f"--- FIM DA OPERAÇÃO. Total: {stats_total_movidos} arquivos. ---")
    else:
        registrar_log_txt("--- FIM. Nenhum arquivo elegível encontrado. ---")