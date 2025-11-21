import customtkinter as ctk
from tkinter import filedialog

# --- lista de extensões ---
# para os checkboxes se o JSON estiver vazio ou incompleto
LISTA_PADRAO = {
    "Documentos": [
        ".abi", ".abw", ".accdb", ".ade", ".adoc", ".ait", ".ans",
        ".apkg", ".azw", ".azw3", ".bdoc", ".bib", ".bna", ".cbc",
        ".chm", ".cnt", ".csv", ".dbk", ".dcx", ".dif", ".djvu",
        ".doc", ".docb", ".docm", ".docs", ".docx", ".dot", ".dotm",
        ".dotx", ".dvi", ".epub", ".ett", ".fb2", ".fdf", ".fdx", ".fdr",
        ".fodt", ".gdoc", ".gslides", ".gsheet", ".gs",
        ".ibooks", ".key", ".keynote", ".kml", ".kmz", ".latex", ".lit",
        ".lrf", ".lts", ".lwp", ".markdown", ".md", ".mobi", ".nb",
        ".nbk", ".notebook", ".numbers", ".odf", ".odp", ".ods",
        ".odt", ".oft", ".one", ".onetoc", ".ott", ".pages", ".pamp",
        ".pdb", ".pdf", ".pm6", ".pm7", ".pot", ".potm", ".potx",
        ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".prn",
        ".ps", ".psw", ".pub", ".pwi", ".rtf", ".sda", ".sdc",
        ".sgml", ".shtml", ".sla", ".slk", ".snb", ".stw", ".sxc",
        ".sxw", ".tex", ".text", ".tsv", ".txt", ".uof", ".uot",
        ".vcs", ".vsd", ".vsdx", ".wks", ".wpd", ".wps", ".wri",
        ".xht", ".xhtml", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt",
        ".xltm", ".xltx", ".xps"
    ],
    "Imagens": [
        ".3fr", ".ai", ".arw", ".avif", ".bay", ".bmp", ".blp", ".cap",
        ".cin", ".clip", ".cr2", ".cr3", ".crw", ".ct", ".cur", ".cut",
        ".dcm", ".dcr", ".dds", ".dng", ".drf", ".ecw", ".emf",
        ".erf", ".exr", ".fits", ".fpx", ".gbr", ".gif", ".gih",
        ".hdp", ".hdr", ".heic", ".heif", ".ico", ".iiq", ".j2c",
        ".j2k", ".jfif", ".jp2", ".jpc", ".jpf", ".jpg", ".jpeg",
        ".jps", ".kdc", ".liff", ".mac", ".mef", ".mng", ".mos",
        ".mrw", ".nef", ".nrw", ".orf", ".pbm", ".pcd", ".pcx",
        ".pef", ".pfm", ".pgf", ".pgm", ".png", ".ppm", ".psb",
        ".psd", ".pts", ".ptx", ".qoi", ".raf", ".raw", ".rw2",
        ".rwl", ".sfw", ".sgi", ".sr2", ".srf", ".srw", ".svg",
        ".svgz", ".tga", ".tif", ".tiff", ".vicar", ".viff",
        ".webp", ".wmf", ".x3f", ".xbm", ".xcf", ".xpm"
    ],
    "Audios": [
        ".aac", ".ac3", ".adts", ".aif", ".aifc", ".aiff", ".alac",
        ".amr", ".ape", ".au", ".aud", ".caf", ".cda", ".dts",
        ".flac", ".gsm", ".it", ".m4a", ".m4b", ".m4p", ".m4r",
        ".mka", ".mlp", ".mod", ".mp2", ".mp3", ".mpa", ".mpc",
        ".msv", ".oga", ".ogg", ".opus", ".ra", ".ram", ".rm",
        ".sam", ".snd", ".spx", ".tak", ".tta", ".voc", ".vqf",
        ".wav", ".wave", ".wma", ".wv", ".xm"
    ],
    "Videos": [
        ".3g2", ".3gp", ".amv", ".asf", ".avi", ".bik", ".bsf",
        ".dav", ".divx", ".drc", ".dv", ".dvr-ms", ".evo",
        ".f4v", ".flv", ".gxf", ".h261", ".h263", ".h264", ".h265",
        ".hevc", ".ifo", ".ismv", ".ivf", ".m1v", ".m2t", ".m2ts",
        ".m2v", ".m4v", ".mkv", ".mod", ".mov", ".mp2v", ".mp4",
        ".mp4v", ".mpeg", ".mpeg4", ".mpg", ".mpv", ".mts",
        ".mxf", ".ogm", ".ogv", ".ps", ".qt", ".rm", ".rmvb",
        ".swf", ".ts", ".vob", ".webm", ".wmv", ".wtv", ".y4m"
    ],
    "Executaveis": [
        ".action", ".apk", ".apkm", ".app", ".bat", ".bin", ".bundle",
        ".cgi", ".cmd", ".com", ".cpl", ".deb", ".dmg", ".elf",
        ".exe", ".ipa", ".isu", ".jar", ".jnlp", ".kexe", ".lnk",
        ".msi", ".msix", ".mst", ".pkg", ".ps1", ".psm1", ".pyz",
        ".rpm", ".run", ".scexe", ".scr", ".sh", ".sys", ".uif",
        ".vbs", ".vxd", ".wsf", ".xapk", ".xip", ".xpi", ".zxp"
    ],
    "Compactados": [
        ".7z", ".ace", ".apkx", ".arc", ".arj", ".bz", ".bz2", ".cab",
        ".car", ".cpio", ".cpgz", ".gz", ".hqx",
        ".img", ".iso", ".lha", ".lrz", ".lz", ".lz4",
        ".lzma", ".lzo", ".pak", ".par", ".par2", ".rar",
        ".sit", ".sitx", ".tar", ".taz", ".tbz", ".tbz2",
        ".tgz", ".tlz", ".txz", ".uc2", ".war", ".xar", ".xz",
        ".zip", ".zipx", ".zst"
    ],
    "Codigos": [
        ".ahk", ".asm", ".asp", ".aspx", ".bash", ".bas",
        ".c", ".cc", ".cfg", ".clj", ".cmake", ".coffee", ".cpp",
        ".cs", ".csh", ".css", ".cson", ".dart", ".env", ".fs", ".fsi",
        ".fsscript", ".fsx", ".go", ".gradle", ".h", ".hpp", ".hs",
        ".html", ".htm", ".ini", ".ipynb", ".java", ".jl", ".js",
        ".json", ".jsp", ".jsx", ".kt", ".kts", ".less", ".lisp",
        ".lua", ".m", ".php", ".pl", ".py", ".pyw",
        ".r", ".rb", ".rs", ".sass", ".scala", ".scss",
        ".sql", ".swift", ".toml", ".ts", ".tsx", ".vb", ".vue",
        ".xml", ".yaml", ".yml"
    ]
}

class JanelaEditor(ctk.CTkToplevel):
    def __init__(self, parent, categoria_nome, dados_atuais, callback_salvar):
        super().__init__(parent)
        self.title(f"Editar: {categoria_nome}")
        self.geometry("650x600")
        self.categoria_nome = categoria_nome
        self.dados = dados_atuais
        self.callback_salvar = callback_salvar
        
        self.vars_extensoes = {} 

        self.grab_set()
        self.focus_force()

        ctk.CTkLabel(self, text=f"Configurando: {categoria_nome}", font=("Roboto", 20, "bold")).pack(pady=(20, 10))
        ctk.CTkLabel(self, text="Selecione quais extensões serão organizadas nesta categoria:", text_color="gray").pack(pady=(0, 10))

        frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_botoes.pack(fill="x", padx=25, pady=5)
        
        btn_todos = ctk.CTkButton(frame_botoes, text="✅ Marcar Todos", width=120, fg_color="#444", command=self.marcar_todos)
        btn_todos.pack(side="left", padx=(0, 10))
        
        btn_nenhum = ctk.CTkButton(frame_botoes, text="⬜ Desmarcar Todos", width=120, fg_color="#444", command=self.desmarcar_todos)
        btn_nenhum.pack(side="left")

        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Extensões Disponíveis", height=250)
        self.scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.criar_checkboxes()

        ctk.CTkLabel(self, text="Mover para pasta específica (Opcional):", anchor="w", font=("Roboto", 12, "bold")).pack(padx=25, pady=(10, 5), fill="x")
        
        self.frame_path = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_path.pack(padx=20, pady=5, fill="x")
        
        path_atual = self.dados['caminho_personalizado'] if self.dados['caminho_personalizado'] else ""
        self.entry_path = ctk.CTkEntry(self.frame_path, placeholder_text="Padrão (Pasta selecionada + Categoria)")
        self.entry_path.pack(side="left", fill="x", expand=True)
        self.entry_path.insert(0, path_atual)
        
        btn_buscar = ctk.CTkButton(self.frame_path, text="📂", width=50, fg_color="#444", hover_color="#555", command=self.buscar_pasta)
        btn_buscar.pack(side="left", padx=(10, 0))

        ctk.CTkButton(self, text="SALVAR CONFIGURAÇÃO", fg_color="#2cc985", hover_color="#26ab71", height=45, font=("Roboto", 14, "bold"), command=self.salvar).pack(padx=20, pady=20, fill="x")

    def criar_checkboxes(self):
        # o que já tem salvo
        extensoes_usuario = set(self.dados['extensoes'])
        
        # lista padrão do sistema
        extensoes_padrao = set(LISTA_PADRAO.get(self.categoria_nome, []))
        
        # une as duas listas e ordena
        todas_opcoes = sorted(list(extensoes_usuario.union(extensoes_padrao)))

        coluna = 0
        linha = 0
        
        for ext in todas_opcoes:
            var = ctk.BooleanVar()
            if ext in extensoes_usuario:
                var.set(True)
            else:
                var.set(False)
            
            self.vars_extensoes[ext] = var

            chk = ctk.CTkCheckBox(self.scroll_frame, text=ext, variable=var, width=110)
            chk.grid(row=linha, column=coluna, padx=5, pady=10, sticky="w")

            coluna += 1
            if coluna >= 5: 
                coluna = 0
                linha += 1

    def marcar_todos(self):
        for var in self.vars_extensoes.values():
            var.set(True)

    def desmarcar_todos(self):
        for var in self.vars_extensoes.values():
            var.set(False)

    def buscar_pasta(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, pasta)

    def salvar(self):
        lista_final = []
        for ext, var in self.vars_extensoes.items():
            if var.get():
                lista_final.append(ext)
        
        caminho = self.entry_path.get().strip()
        if caminho == "":
            caminho = None

        novos_dados = {
            "extensoes": lista_final,
            "caminho_personalizado": caminho,
            "ativo": True
        }

        self.callback_salvar(self.categoria_nome, novos_dados)
        self.destroy()