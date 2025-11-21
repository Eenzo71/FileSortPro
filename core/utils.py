import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')

# --- backup ---
# caso o config.json seja deletado ou corrompido.
DEFAULT_CONFIG = {
    "app_settings": {
        "versao": "1.0.0",
        "modo_escuro": True,
        "iniciar_minimizado": False
    },
    "diretorios": {
        "padrao_destino": None,
        "ignorar_pastas": []
    },
    "regras": {
        "Documentos": {
            "extensoes": [
                ".abi", ".abw", ".accdb", ".ade", ".adoc", ".ait", ".ans", ".apkg", ".azw",
                ".azw3", ".bdoc", ".bib", ".bna", ".cbc", ".chm", ".cnt", ".csv", ".dbk",
                ".dcx", ".dif", ".djvu", ".doc", ".docb", ".docm", ".docs", ".docx", ".dot",
                ".dotm", ".dotx", ".dvi", ".epub", ".ett", ".fb2", ".fdf", ".fdx", ".fdr",
                ".fodt", ".gdoc", ".gslides", ".gsheet", ".gs", ".ibooks", ".key", ".keynote",
                ".kml", ".kmz", ".latex", ".lit", ".lrf", ".lts", ".lwp", ".markdown", ".md",
                ".mobi", ".nb", ".nbk", ".notebook", ".numbers", ".odf", ".odp", ".ods",
                ".odt", ".oft", ".one", ".onetoc", ".ott", ".pages", ".pamp", ".pdb", ".pdf",
                ".pm6", ".pm7", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt",
                ".pptm", ".pptx", ".prn", ".ps", ".psw", ".pub", ".pwi", ".rtf", ".sda",
                ".sdc", ".sgml", ".shtml", ".sla", ".slk", ".snb", ".stw", ".sxc", ".sxw",
                ".tex", ".text", ".tsv", ".txt", ".uof", ".uot", ".vcs", ".vsd", ".vsdx",
                ".wks", ".wpd", ".wps", ".wri", ".xht", ".xhtml", ".xls", ".xlsb", ".xlsm",
                ".xlsx", ".xlt", ".xltm", ".xltx", ".xps"
            ],
            "caminho_personalizado": None,
            "ativo": True
        },

        "Imagens": {
            "extensoes": [
                ".3fr", ".ai", ".arw", ".avif", ".bay", ".blp", ".bmp", ".cap", ".cin",
                ".clip", ".cr2", ".cr3", ".crw", ".ct", ".cur", ".cut", ".dcm", ".dcr",
                ".dds", ".dng", ".drf", ".ecw", ".emf", ".erf", ".exr", ".fits", ".fpx",
                ".gbr", ".gif", ".gih", ".hdp", ".hdr", ".heic", ".heif", ".ico", ".iiq",
                ".j2c", ".j2k", ".jfif", ".jp2", ".jpc", ".jpeg", ".jpf", ".jpg", ".jps",
                ".kdc", ".liff", ".mac", ".mef", ".mng", ".mos", ".mrw", ".nef", ".nrw",
                ".orf", ".pbm", ".pcd", ".pcx", ".pef", ".pfm", ".pgf", ".pgm", ".png",
                ".ppm", ".psb", ".psd", ".pts", ".ptx", ".qoi", ".raf", ".raw", ".rw2",
                ".rwl", ".sfw", ".sgi", ".sr2", ".srf", ".srw", ".svg", ".svgz", ".tga",
                ".tif", ".tiff", ".vicar", ".viff", ".webp", ".wmf", ".x3f", ".xbm", ".xcf",
                ".xpm"
            ],
            "caminho_personalizado": None,
            "ativo": True
        },

        "Audios": {
            "extensoes": [
                ".aac", ".ac3", ".adts", ".aif", ".aifc", ".aiff", ".alac", ".amr", ".ape",
                ".au", ".aud", ".caf", ".cda", ".dts", ".flac", ".gsm", ".it", ".m4a",
                ".m4b", ".m4p", ".m4r", ".mka", ".mlp", ".mod", ".mp2", ".mp3", ".mpa",
                ".mpc", ".msv", ".oga", ".ogg", ".opus", ".ra", ".ram", ".rm", ".sam",
                ".snd", ".spx", ".tak", ".tta", ".voc", ".vqf", ".wav", ".wave", ".wma",
                ".wv", ".xm"
            ],
            "caminho_personalizado": None,
            "ativo": True
        },

        "Videos": {
            "extensoes": [
                ".3g2", ".3gp", ".amv", ".asf", ".avi", ".bik", ".bsf", ".dav", ".divx",
                ".drc", ".dv", ".dvr-ms", ".evo", ".f4v", ".flv", ".gxf", ".h261", ".h263",
                ".h264", ".h265", ".hevc", ".ifo", ".ismv", ".ivf", ".m1v", ".m2t", ".m2ts",
                ".m2v", ".m4v", ".mkv", ".mod", ".mov", ".mp2v", ".mp4", ".mp4v", ".mpeg",
                ".mpeg4", ".mpg", ".mpv", ".mts", ".mxf", ".ogm", ".ogv", ".ps", ".qt",
                ".rm", ".rmvb", ".swf", ".ts", ".vob", ".webm", ".wmv", ".wtv", ".y4m"
            ],
            "caminho_personalizado": None,
            "ativo": True
        },

        "Executaveis": {
            "extensoes": [
                ".action", ".apk", ".apkm", ".app", ".bat", ".bin", ".bundle", ".cgi",
                ".cmd", ".com", ".cpl", ".deb", ".dmg", ".elf", ".exe", ".ipa", ".isu",
                ".jar", ".jnlp", ".kexe", ".lnk", ".msi", ".msix", ".mst", ".pkg", ".ps1",
                ".psm1", ".pyz", ".rpm", ".run", ".scexe", ".scr", ".sh", ".sys", ".uif",
                ".vbs", ".vxd", ".wsf", ".xapk", ".xip", ".xpi", ".zxp"
            ],
            "caminho_personalizado": None,
            "ativo": False
        },

        "Compactados": {
            "extensoes": [
                ".7z", ".ace", ".apkx", ".arc", ".arj", ".bz", ".bz2", ".cab", ".car",
                ".cpgz", ".cpio", ".gz", ".hqx", ".img", ".iso", ".lha", ".lrz", ".lz",
                ".lz4", ".lzma", ".lzo", ".pak", ".par", ".par2", ".rar", ".sit", ".sitx",
                ".tar", ".taz", ".tbz", ".tbz2", ".tgz", ".tlz", ".txz", ".uc2", ".war",
                ".xar", ".xz", ".zip", ".zipx", ".zst"
            ],
            "caminho_personalizado": None,
            "ativo": False
        },

        "Codigos": {
            "extensoes": [
                ".ahk", ".asm", ".asp", ".aspx", ".bash", ".bas", ".c", ".cc", ".cfg", ".clj",
                ".cmake", ".coffee", ".cpp", ".cs", ".csh", ".css", ".cson", ".dart", ".env",
                ".fs", ".fsi", ".fsscript", ".fsx", ".go", ".gradle", ".h", ".hpp", ".hs",
                ".html", ".htm", ".ini", ".ipynb", ".java", ".jl", ".js", ".json", ".jsp",
                ".jsx", ".kt", ".kts", ".less", ".lisp", ".lua", ".m", ".php", ".pl", ".py",
                ".pyw", ".r", ".rb", ".rs", ".sass", ".scala", ".scss", ".sql", ".swift",
                ".toml", ".ts", ".tsx", ".vb", ".vue", ".xml", ".yaml", ".yml"
            ],
            "caminho_personalizado": None,
            "ativo": False
        }
    }
}

def carregar_configuracoes():
    # se não encontrar o arquivo cria um novo baseado no padrão
    if not os.path.exists(CONFIG_PATH):
        print(f"⚠️ Configuração não encontrada. Criando novo arquivo em: {CONFIG_PATH}")
        salvar_configuracoes(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except Exception as e:
        # lógica de Auto-Reparo
        print(f"❌ ERRO CRÍTICO AO LER CONFIG: {e}")
        print("♻️ Restaurando configuração padrão para evitar travamento...")
        salvar_configuracoes(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

def salvar_configuracoes(novos_dados):
    try:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as arquivo:
            json.dump(novos_dados, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar configurações: {e}")
        return False