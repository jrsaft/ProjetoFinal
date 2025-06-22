import tkinter as tk
from tkinter import ttk, messagebox,filedialog
from datetime import datetime
import random
import string
from models.bancodedados import DBService
from PIL import Image, ImageTk
import csv

class SoftwareCRM:
    def __init__(self, root): # root é o objeto da classe
        self.root = root #Janela principal 
        self.root.title("Plataforma Inteligente de Atendimento ao Cliente")
        self.root.geometry("1000x800")
        self.root.resizable(True, True) #Tornar a janela redimensionável horizontal e verticalmente.

        self.container = tk.Frame(root) #Cria um Frame dentro da janela, que é um contêiner em que você pode colocar outros widgets (botões, labels, etc.).
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1) #row -> linhas.
        self.container.grid_columnconfigure(0, weight=1) #column -> colunas.

        self.tela_principal = tk.Frame(self.container) #Adiciona o container dentro do frame
        self.tela_perguntas_info = tk.Frame(self.container)
        self.tela_cadastro_cliente = tk.Frame(self.container)
        self.tela_infos = tk.Frame(self.container)
        self.tela_atendimento = tk.Frame(self.container)
        self.tela_envio = tk.Frame(self.container)
        self.tela_reversa = tk.Frame(self.container)
        self.tela_logistica = tk.Frame(self.container)
        self.tela_financeiro = tk.Frame(self.container)
         

        for tela in (self.tela_principal,self.tela_perguntas_info, self.tela_cadastro_cliente, self.tela_infos, self.tela_atendimento,
                     self.tela_envio, self.tela_reversa, self.tela_logistica, self.tela_financeiro): #empilhar várias "telas" umas sobre as outras no mesmo lugar. Uma delas será visivel por vez.
            tela.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(self.tela_principal)

        self.configurar_tela_principal()
        self.configurar_tela_perguntas_info()
        self.configurar_tela_infos()
        self.configurar_tela_cadastro_cliente()
        self.configurar_tela_atendimento()
        self.configurar_tela_envio()
        self.gerar_codigo_rastreio()
        self.configurar_tela_reversa()
        self.configurar_tela_financeiro()
        self.configurar_tela_logistica()

        self.banco_usuarios = DBService(banco='usuarios')
        self.banco_envios = DBService(banco='envios')

    
    def mostrar_tela(self, tela):
        tela.tkraise()

    def configurar_tela_principal(self):
        frame = tk.Frame(self.tela_principal, padx=20, pady=20)#Criação do frame
        frame.place(relx=0.5, rely=0.5, anchor="center")

        imagem = Image.open("models/logo.jpg")
        imagem = imagem.resize((200, 120))  # Redimensiona conforme necessário
        imagem_tk = ImageTk.PhotoImage(imagem)

        label_imagem = tk.Label(frame, image=imagem_tk)
        label_imagem.image = imagem_tk  # MANTER a referência
        label_imagem.pack(pady=(0, 10))  # Espaço abaixo da imagem

        titulo = tk.Label(frame, text="People Control", font=("Arial", 16, "bold") )
        titulo.pack(pady=(0,30)) #(cima,baixo)

        btn_info_cliente = tk.Button(frame, text="Clientes", width=25, height=2,
                                         command=lambda: self.mostrar_tela(self.tela_perguntas_info)) #command=lambda: troca a tela atual para a tela de cadastro.
        btn_info_cliente.pack(pady=10)

        btn_atendimentos = tk.Button(frame, text="Atendimento", width=25, height=2,
                                        command=lambda: self.mostrar_tela(self.tela_atendimento))
        btn_atendimentos.pack(pady=10)

        btn_logistica = tk.Button(frame, text="Gestão de logistica", width=25, height=2,
                                               command=lambda: self.mostrar_tela(self.tela_logistica))
        btn_logistica.pack(pady=10)

        btn_finaceiro = tk.Button(frame, text="Financeiro", width=25, height=2,
                                             command=lambda: self.mostrar_tela(self.tela_financeiro))
        btn_finaceiro.pack(pady=10)

        btn_sair = tk.Button(frame, text="Sair", width=25, height=2,
                             command=self.root.quit)
        btn_sair.pack(pady=10)

    def configurar_tela_perguntas_info(self): # tela para perguntar se ele deseja cadastrar ou consultar um cliente.
        titulo_perguntas_info = tk.Label(self.tela_perguntas_info, text="Qual ação você \n deseja realizar?", font=("Arial", 30, "bold"))
        titulo_perguntas_info.pack(pady=35)

        frame_perguntas_info = tk.Frame(self.tela_perguntas_info, padx=30)
        frame_perguntas_info.pack(fill="both",expand=True, pady=10)

        btn_perguntas_cadastrar = tk.Button(frame_perguntas_info, text="Cadastrar cliente", width=30, height=4,
                                         command=lambda: self.mostrar_tela(self.tela_cadastro_cliente)) #command=lambda: troca a tela atual para a tela de cadastro.
        btn_perguntas_cadastrar.pack(pady=10)

        btn_perguntas_consultar = tk.Button(frame_perguntas_info, text="Consultar informações \n do cliente", width=30, height=4,
                                            command=lambda: self.mostrar_tela(self.tela_infos))
        btn_perguntas_consultar.pack(pady=10)

        btn_voltar = tk.Button(frame_perguntas_info, text="Voltar", width=30, height=4,
                                command=lambda: self.mostrar_tela(self.tela_principal))
        btn_voltar.pack(pady=10)

###### CRIAR TELA DE CADASTRO DE CLIENTES E ASSOCIAR AO BOTÃO DE CADASTRO.
    def configurar_tela_cadastro_cliente(self):
        titulo = tk.Label(self.tela_cadastro_cliente, text="CADASTRO DE CLIENTES", font=("Arial", 22, "bold"))
        titulo.pack(pady=20)

        tdois = tk.Label(self.tela_cadastro_cliente, text="Dados de Identificação do Cliente", font=("Arial",18, "bold"))
        tdois.pack(pady=8)

        frame_cadastro_cliente = tk.Frame(self.tela_cadastro_cliente, padx=10)
        frame_cadastro_cliente.pack(pady=10)

        tk.Label(frame_cadastro_cliente,text="Nome:").grid(row=0, column=0, sticky="e", pady=5)
        self.cliente_nome_entry = tk.Entry(frame_cadastro_cliente, width=15)
        self.cliente_nome_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(frame_cadastro_cliente, text="CPF:").grid(row=1, column=0, sticky="e", pady=5)
        self.cliente_cpf_entry = tk.Entry(frame_cadastro_cliente, width=15)
        self.cliente_cpf_entry.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(frame_cadastro_cliente, text="Data de nascimento:").grid(row=2, column=0,sticky="e",pady=5)
        self.cliente_data_entry = tk.Entry(frame_cadastro_cliente,width=15)
        self.cliente_data_entry.grid(row=2, column=1,sticky="w",pady=5)

        tk.Label(frame_cadastro_cliente, text="Gênero:").grid(row=3, column=0, sticky="e",pady=5)
        self.cliente_genero_entry = tk.Entry(frame_cadastro_cliente,width=15)
        self.cliente_genero_entry.grid(row=3, column=1, sticky="w",pady=5)

        # Seção: Informações pessoais do cliente

        ttres = tk.Label(self.tela_cadastro_cliente, text="Informações de Contato", font=("Arial",18, "bold"))
        ttres.pack(pady=8)

        frame_contato_cliente = tk.Frame(self.tela_cadastro_cliente, padx=30)
        frame_contato_cliente.pack(pady=18)

        tk.Label(frame_contato_cliente, text="Telefone:").grid(row=0, column=0, sticky="e", pady=2)
        self.cliente_telefone_entry = tk.Entry(frame_contato_cliente, width=20)
        self.cliente_telefone_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(frame_contato_cliente, text="E-mail:").grid(row=1, column=0, sticky="e", pady=5)
        self.cliente_email_entry = tk.Entry(frame_contato_cliente, width=30)
        self.cliente_email_entry.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(frame_contato_cliente, text="Endereço:").grid(row=2, column=0, sticky="e", pady=5)
        self.cliente_endereco_entry = tk.Entry(frame_contato_cliente, width=30)
        self.cliente_endereco_entry.grid(row=2, column=1, sticky="w", pady=5)

        tk.Label(frame_contato_cliente, text="CEP:").grid(row=3, column=0, sticky="e", pady=5)
        self.cliente_cep_entry = tk.Entry(frame_contato_cliente, width=10)
        self.cliente_cep_entry.grid(row=3, column=1, sticky="w", pady=5)

        # Seção: Preferências e histórico do cliente
        tquatro = tk.Label(self.tela_cadastro_cliente, text="Histórico", font=("Arial", 18, "bold"))
        tquatro.pack(pady=8)

        frame_extra_cliente = tk.Frame(self.tela_cadastro_cliente, padx=30)
        frame_extra_cliente.pack(pady=10)

        # # Histórico de rastreamento (entrada múltipla, separada por vírgula)
        # tk.Label(frame_extra_cliente, text="Histórico de Rastreamento:").grid(row=0, column=0, sticky="e", pady=5)
        # self.cliente_rastreamento_entry = tk.Entry(frame_extra_cliente, width=40)
        # validar_rastreio(cliente_)
        # self.cliente_rastreamento_entry.grid(row=0, column=1, sticky="w", pady=5)

        # Preferências de comunicação (checkboxes)
        tk.Label(frame_extra_cliente, text="Preferências de Comunicação:").grid(row=1, column=0, sticky="ne", pady=5)
 
        self.pref_whatsapp = tk.BooleanVar() #Váriaveis do tipo booleana
        self.pref_email = tk.BooleanVar()

        check_frame = tk.Frame(frame_extra_cliente) #Criação de um frame para o checkbutton
        check_frame.grid(row=1, column=1, sticky="w")

        tk.Checkbutton(check_frame, text="WhatsApp", variable=self.pref_whatsapp).pack(anchor="w")
        tk.Checkbutton(check_frame, text="E-mail", variable=self.pref_email).pack(anchor="w")

        btn_salvar = tk.Button(frame_extra_cliente, text="Salvar", width=12, height=1,
    command=lambda: (
        self.banco_usuarios.criar_usuario(
            self.cliente_nome_entry.get(),
            self.cliente_data_entry.get(),
            self.cliente_cpf_entry.get(),
            self.cliente_genero_entry.get(),
            self.cliente_telefone_entry.get(),
            self.cliente_email_entry.get(),
            self.cliente_endereco_entry.get(),
            self.cliente_cep_entry.get(),
            " e ".join(
                [x for x in ["WhatsApp" if self.pref_whatsapp.get() else "", 
                             "E-mail" if self.pref_email.get() else ""] if x]
            ) or "Nenhuma"
        )
    )
)
        btn_salvar.grid(row=4, column=1, pady=5)
        #Botão de voltar para a tela anterior;
        btn_voltar = tk.Button(frame_extra_cliente, text="Voltar", width=12, height=1,
                  command=lambda: self.mostrar_tela(self.tela_perguntas_info)).grid(row=4, column=0, pady=5)


    def configurar_tela_infos(self):
        infos_titulo = tk.Label(self.tela_infos, text="Informações dos clientes", font=("Arial", 20, "bold"))
        infos_titulo.pack(pady=10)

        tk.Label(self.tela_infos, text="Nome do cliente:").pack(ipady=5)
        self.cliente_entry = tk.Entry(self.tela_infos, width=15)
        self.cliente_entry.pack(ipady=5)

        botoes_frame = tk.Frame(self.tela_infos)
        botoes_frame.pack(pady=15)

        tk.Button(botoes_frame, text="Pesquisar", width=12,
          command=self.pesquisar_cliente).pack(side="left", padx=20)
        
        tk.Button(botoes_frame, text="Voltar", width=12,
                  command=lambda: self.mostrar_tela(self.tela_principal)).pack(side="bottom", padx=20, pady=20)

        frame_infos = tk.Frame(self.tela_infos, padx=30)
        frame_infos.pack(fill="both", expand=True, pady=10)

        self.listbox_clientes = tk.Listbox(frame_infos, width=40, height=5, font=("Arial", 10)) #Cria um widget Listbox, que é uma caixa de seleção/lista para mostrar múltiplos itens, dentro do frame_infos.
        self.listbox_clientes.pack(side="left", fill="both", expand=True)
        
    def pesquisar_cliente(self):
        nome = self.cliente_entry.get().strip()
        if not nome:
            messagebox.showinfo("Busca vazia", "Digite um nome para pesquisar.")
            return

        resultados = self.banco_usuarios.buscar_usuarios_por_nome(nome)

        self.listbox_clientes.delete(0, tk.END)
        if not resultados:
            messagebox.showinfo("Resultado da busca", "Cliente não encontrado.")
            return
        for u in resultados:
            cliente_info = (
                f"{u.nome} | \n"
                f"CPF: {u.cpf}  |  Nascimento: {u.datadenascimento} | \n"
                f"Gênero: {u.genero}  |  Telefone: {u.telefone} | \n"
                f"E-mail: {u.email} | \n"
                f"Endereço: {u.endereco} - CEP: {u.cep} | \n"
                f"Preferência: {u.comunicacao} \n"
            )
            self.listbox_clientes.insert(tk.END, cliente_info)
            

    def configurar_tela_atendimento(self):
    # Tela que mostra os três botões para Envio, Logistica Reversa e Voltar.

        titulo_perguntas_info = tk.Label(self.tela_atendimento, text="Qual ação você \n deseja realizar?", font=("Arial", 30, "bold"))
        titulo_perguntas_info.pack(pady=35)

        frame_atendimento = tk.Frame(self.tela_atendimento, padx=30)
        frame_atendimento.pack(fill="both",expand=True, pady=10)

        btn_envio = tk.Button(frame_atendimento, text="Envio", width=30, height=4,
                                         command=lambda: self.mostrar_tela(self.tela_envio)) #command=lambda: troca a tela atual para a tela de cadastro.
        btn_envio.pack(pady=10)

        btn_envio = tk.Button(frame_atendimento, text="Logistica reversa", width=30, height=4,
                                         command=lambda: self.mostrar_tela(self.tela_reversa)) #command=lambda: troca a tela atual para a tela de cadastro.
        btn_envio.pack(pady=10)

        btn_voltar = tk.Button(frame_atendimento, text="Voltar", width=30, height=4,
                  command=lambda: self.mostrar_tela(self.tela_principal))
        btn_voltar.pack(pady=10)

    def gerar_codigo_rastreio(self):
        # Método para gerar um código de rastreio aleatório a cada clique no botão.
        letras = string.ascii_uppercase
        prefixo = ''.join(random.choices(letras, k=2))
        numeros = ''.join(random.choices(string.digits, k=9))
        sufixo = ''.join(random.choices(letras, k=2))
        rastreio = prefixo + numeros + sufixo
        self.rastreio_entry.delete(0, tk.END)
        self.rastreio_entry.insert(0, rastreio)


    def configurar_tela_envio(self):
        # === SCROLL SETUP ===
        canvas = tk.Canvas(self.tela_envio)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.tela_envio, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Frame de conteúdo dentro do canvas
        content_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="n")

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        content_frame.bind("<Configure>", on_configure)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

        # Tela para relizar um envio.
        envio_titulo = tk.Label(content_frame, text="Realização de envios.", font=("Arial", 20, "bold"))
        envio_titulo.pack(pady=5)

        remetente_titulo = tk.Label(content_frame, text="Informações do remetente.", font=("Arial", 15, "bold"))
        remetente_titulo.pack(pady=18)

        frame_envio = tk.Frame(content_frame, padx=30)
        frame_envio.pack(pady=25)

        tk.Label(frame_envio,text="Nome:").grid(row=0, column=0, sticky="e", pady=5)
        self.envio_nome_entry = tk.Entry(frame_envio, width=15)
        self.envio_nome_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(frame_envio, text="CPF:").grid(row=1, column=0, sticky="e", pady=5)
        self.envio_cpf_entry = tk.Entry(frame_envio, width=15)
        self.envio_cpf_entry.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(frame_envio, text="Logradouro:").grid(row=2, column=0, sticky="e", pady=5)
        self.envio_endereco_entry = tk.Entry(frame_envio, width=15)
        self.envio_endereco_entry.grid(row=2, column=1, sticky="w", pady=5)

        tk.Label(frame_envio, text="Bairro:").grid(row=3, column=0, sticky="e", pady=5)
        self.envio_bairro_entry = tk.Entry(frame_envio, width=15)
        self.envio_bairro_entry.grid(row=3, column=1, sticky="w", pady=5)

        tk.Label(frame_envio, text="CEP:").grid(row=4, column=0, sticky="e", pady=5)
        self.envio_cep_entry = tk.Entry(frame_envio, width=15)
        self.envio_cep_entry.grid(row=4, column=1, sticky="w", pady=5)
        
        tk.Label(frame_envio, text="Rastreio:").grid(row=5, column=0, sticky="e", pady=5)
        self.rastreio_entry = tk.Entry(frame_envio, width=20)
        self.rastreio_entry.grid(row=5, column=1, pady=5)
        btn_rastreio = tk.Button(frame_envio, text="Gerar rastreio", width=10, height=1,
                                            command=lambda: self.gerar_codigo_rastreio())
        btn_rastreio.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(frame_envio, text="Tipo de serviço escolhido:").grid(row=7, column=0, sticky="ne", pady=5)

        self.tipo_servico = tk.StringVar()  # Variável comum para todos os Radiobuttons

        check_frame = tk.Frame(frame_envio)
        check_frame.grid(row=7, column=1, sticky="w")

        tk.Radiobutton(check_frame, text="Sedex", variable=self.tipo_servico, value="Sedex").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(check_frame, text="PAC", variable=self.tipo_servico, value="PAC").grid(row=0, column=1, sticky="w")
        tk.Radiobutton(check_frame, text="Carta", variable=self.tipo_servico, value="Carta").grid(row=0, column=2, sticky="w")

        destinatario_titulo = tk.Label(content_frame, text="Informações do destinatário.", font=("Arial", 15, "bold"))
        destinatario_titulo.pack(pady=18)

        frame_destinatario = tk.Frame(content_frame, padx=30)
        frame_destinatario.pack(pady=18)

        tk.Label(frame_destinatario, text="Nome:").grid(row=0, column=0, sticky="e", pady=5)
        self.destinatario_entry = tk.Entry(frame_destinatario, width=15)
        self.destinatario_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(frame_destinatario, text="CPF:").grid(row=1, column=0, sticky="e", pady=5)
        self.destinatario_cpf_entry = tk.Entry(frame_destinatario, width=15)
        self.destinatario_cpf_entry.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(frame_destinatario, text="Logradouro:").grid(row=2, column=0, sticky="e", pady=5)
        self.destinatario_endereco_entry = tk.Entry(frame_destinatario, width=15)
        self.destinatario_endereco_entry.grid(row=2, column=1, sticky="w", pady=5)

        tk.Label(frame_destinatario, text="Bairro:").grid(row=3, column=0, sticky="e", pady=5)
        self.destinatario_bairro_entry = tk.Entry(frame_destinatario, width=15)
        self.destinatario_bairro_entry.grid(row=3, column=1, sticky="w", pady=5)

        tk.Label(frame_destinatario, text="CEP:").grid(row=4, column=0, sticky="e", pady=5)
        self.destinatario_cep_entry = tk.Entry(frame_destinatario, width=15)
        self.destinatario_cep_entry.grid(row=4, column=1, sticky="w", pady=5)

        pagamento_titulo = tk.Label(content_frame, text="Informações do pagamento.", font=("Arial", 15, "bold"))
        pagamento_titulo.pack(pady=10)

        frame_pagamento = tk.Frame(content_frame)
        frame_pagamento.pack(pady=5)

        tk.Label(frame_pagamento, text="Forma de pagamento:").grid(row=0, column=0, sticky="e", pady=5)
        self.forma_pagamento_entry = tk.Entry(frame_pagamento, width=15)
        self.forma_pagamento_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(frame_pagamento, text="Valor:").grid(row=1, column=0, sticky="e", pady=5)
        self.valor_entry =tk.Entry(frame_pagamento, width=15)
        self.valor_entry.grid(row=1, column=1, pady=5)
        btn_valor = tk.Button(frame_pagamento, text="Calcular valor", width=12, height=1,
            command=self.mostrar_valor_envio)
        btn_valor.grid(row=2, column=0, columnspan=2, pady=10)

        btn_salvar_envio = tk.Button(
            frame_pagamento,
            text="Salvar", 
            width=12, 
            height=1,
    command=lambda: (
        self.banco_envios.criar_envio(
            self.envio_nome_entry.get(),
            self.envio_cpf_entry.get(),
            self.envio_endereco_entry.get(),
            self.envio_bairro_entry.get(),
            self.envio_cep_entry.get(),
            self.rastreio_entry.get(),
            self.tipo_servico.get(),
            self.destinatario_entry.get(),
            self.destinatario_cpf_entry.get(),
            self.destinatario_endereco_entry.get(),
            self.destinatario_bairro_entry.get(),
            self.destinatario_cep_entry.get(),
            self.forma_pagamento_entry.get(),
            self.valor_entry.get())))
        btn_salvar_envio.grid(row=3, column=0, pady=10)

        btn_voltar_envio = tk.Button(
            frame_pagamento,
            text="Voltar",
            width=12,
            command=lambda: self.mostrar_tela(self.tela_atendimento)
        )
        btn_voltar_envio.grid(row=3, column=1, padx=15)


    def calcular_valor_envio(self, cep_destino: str) -> float:
        # Remove traço e converte para inteiro
        try:
            cep_num = int(cep_destino.replace("-", ""))
        except ValueError:
            return "Erro"

        # Região Sudeste
        if 1000000 <= cep_num <= 19999999:
            return 20.00  # São Paulo
        elif 20000000 <= cep_num <= 28999999:
            return 22.00  # Rio de Janeiro
        elif 29000000 <= cep_num <= 29999999:
            return 22.00  # Espírito Santo
        elif 30000000 <= cep_num <= 39999999:
            return 21.00  # Minas Gerais

        # Região Sul
        elif 80000000 <= cep_num <= 87999999:
            return 23.00  # Paraná
        elif 88000000 <= cep_num <= 89999999:
            return 23.00  # Santa Catarina
        elif 90000000 <= cep_num <= 99999999:
            return 24.00  # Rio Grande do Sul

        # Região Nordeste
        elif 40000000 <= cep_num <= 48999999:
            return 26.00  # Bahia
        elif 49000000 <= cep_num <= 49999999:
            return 26.50  # Sergipe
        elif 50000000 <= cep_num <= 56999999:
            return 27.00  # Pernambuco
        elif 57000000 <= cep_num <= 57999999:
            return 27.00  # Alagoas
        elif 58000000 <= cep_num <= 58999999:
            return 27.00  # Paraíba
        elif 59000000 <= cep_num <= 59999999:
            return 27.50  # RN
        elif 60000000 <= cep_num <= 63999999:
            return 28.00  # Ceará
        elif 64000000 <= cep_num <= 64999999:
            return 28.00  # Piauí
        elif 65000000 <= cep_num <= 65999999:
            return 28.00  # Maranhão

        # Região Norte
        elif 66000000 <= cep_num <= 68899999:
            return 29.00  # Pará
        elif 68900000 <= cep_num <= 68999999:
            return 30.00  # Amapá
        elif 69000000 <= cep_num <= 69299999:
            return 30.00  # Amazonas parte 1
        elif 69300000 <= cep_num <= 69399999:
            return 30.00  # Roraima
        elif 69400000 <= cep_num <= 69899999:
            return 30.00  # Amazonas parte 2
        elif 69900000 <= cep_num <= 69999999:
            return 30.00  # Acre
        elif 76800000 <= cep_num <= 76999999:
            return 30.00  # Rondônia
        elif 77000000 <= cep_num <= 77999999:
            return 29.00  # Tocantins

        # Região Centro-Oeste
        elif 70000000 <= cep_num <= 72799999:
            return 25.00  # DF parte 1
        elif 72800000 <= cep_num <= 72999999:
            return 25.00  # GO parte 1
        elif 73000000 <= cep_num <= 73699999:
            return 25.00  # DF parte 2
        elif 73700000 <= cep_num <= 76799999:
            return 25.00  # GO parte 2
        elif 78000000 <= cep_num <= 78899999:
            return 26.00  # MT
        elif 79000000 <= cep_num <= 79999999:
            return 26.00  # MS

        # Caso não se encaixe em nenhuma faixa
        return 35.00  # Valor padrão para CEPs não reconhecidos
            
    def mostrar_valor_envio(self):
        cep = self.destinatario_cep_entry.get()
        valor = self.calcular_valor_envio(cep)
        self.valor_entry.delete(0, tk.END)

        if valor == "Erro":
            self.valor_entry.insert(0, "CEP inválido")
        else:
            self.valor_entry.insert(0, f"R$ {valor:.2f}")


    def configurar_tela_reversa(self):
    # Tela para realizar uma devolução.
        
        reversa_titulo = tk.Label(self.tela_reversa, text="Logistica reversa.", font=("Arial", 20, "bold"))
        reversa_titulo.pack(pady=10)

        frame_reversa = tk.Frame(self.tela_reversa, padx=20)
        frame_reversa.pack(fill="both", expand=True, pady=10)

        tk.Label(frame_reversa,text="Rastreio da devolução:").grid(row=0, column=0, sticky="e", pady=5)
        self.reversa_rastreio_entry = tk.Entry(frame_reversa, width=15)
        self.reversa_rastreio_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(frame_reversa, text="CPF do cliente:").grid(row=1, column=0, sticky="e", pady=5)
        self.reversa_cpf_entry = tk.Entry(frame_reversa, width=15)
        self.reversa_cpf_entry.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(frame_reversa, text="Forma de pagamento").grid(row=2, column=0, sticky="e", pady=5)
        self.reversa_pagemento_entry = tk.Entry(frame_reversa, width=25)
        self.reversa_pagemento_entry.grid(row=2, column=1, sticky="w", pady=5)

        self.listbox_reversa = tk.Listbox(frame_reversa, width=150, height=25, font=("Arial", 10))
        self.listbox_reversa.grid(row=3, column=0, columnspan=2, pady=10)

        botoes_reversa = tk.Frame(self.tela_reversa)
        botoes_reversa.pack(pady=10)

        tk.Button(botoes_reversa, text="Pesquisar", width=12,
          command=self.pesquisar_rastreio).pack(side="left", padx=20)
        
        tk.Button(botoes_reversa, text="Voltar", width=12,
                  command=lambda: self.mostrar_tela(self.tela_atendimento)).pack(side="left", padx=20)

        
    def pesquisar_rastreio(self):
        rastreio = self.reversa_rastreio_entry.get().strip()
        if not rastreio:
            messagebox.showinfo("Busca vazia", "Digite o rastreio para pesquisar.")
            return

        resultados = self.banco_envios.buscar_envios_por_rastreio(rastreio)

        self.listbox_reversa.delete(0, tk.END)
        if not resultados:
            messagebox.showinfo("Resultado da busca", "Envio não encontrado.")
            return
        for u in resultados:
            self.listbox_reversa.insert(
                tk.END,
                f"Rastreio {u.rastreio} \n "
                f"Destinatario: {u.nomedodestinatario} - CEP: {u.cepdodestinatario} - "
                f"Endereço de retorno: {u.enderecodoremetente} - CEP: {u.cepdoremetente} "
            )

    def criar_entry(self, frame, label_text, row):
        tk.Label(frame, text=label_text).grid(row=row, column=0, padx=5, pady=5, sticky="e")
        var = tk.StringVar()
        tk.Entry(frame, textvariable=var, width=40).grid(row=row, column=1, padx=5, pady=5)
        return var
    
    def configurar_tela_financeiro(self):
        financeiro_titulo = tk.Label(self.tela_financeiro, text="Tela Financeira", font=("Arial", 20, "bold"))
        financeiro_titulo.pack(pady=10)
        
        frame_financeiro = tk.Frame(self.tela_financeiro, padx=20)
        frame_financeiro.pack(fill="both", expand=True, pady=10)

        form_frame = tk.Frame(frame_financeiro)
        form_frame.pack(pady=10)

        self.cliente_var = self.criar_entry(form_frame, "Cliente:", 0)
        self.produto_var = self.criar_entry(form_frame, "Produto:", 1)
        self.valor_var = self.criar_entry(form_frame, "Valor (R$):", 2)

        tk.Label(form_frame, text="Forma de Pagamento:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.forma_pagamento_var = tk.StringVar()
        forma_pagamento_combo = ttk.Combobox(form_frame, textvariable=self.forma_pagamento_var, state="readonly",
                                             values=["Crédito", "Débito", "Pix", "Boleto"])
        forma_pagamento_combo.grid(row=3, column=1, padx=5, pady=5)
        forma_pagamento_combo.current(0)

        self.tree_financeiro = ttk.Treeview(frame_financeiro, columns=("Cliente", "Produto", "Valor", "Pagamento", "Data"), show="headings")
        for col in ("Cliente", "Produto", "Valor", "Pagamento", "Data"):
            self.tree_financeiro.heading(col, text=col)
            self.tree_financeiro.column(col, width=150)
        self.tree_financeiro.pack(pady=10, fill="x", expand=True)

        def adicionar_compra():
            cliente = self.cliente_var.get()
            produto = self.produto_var.get()
            valor = self.valor_var.get()
            forma = self.forma_pagamento_var.get()
            data = datetime.now().strftime("%d/%m/%Y")

            if cliente and produto and valor and forma:
                self.tree_financeiro.insert("", "end", values=(cliente, produto, valor, forma, data))
                self.cliente_var.set("")
                self.produto_var.set("")
                self.valor_var.set("")
                self.forma_pagamento_var.set("Crédito")
            else:
                messagebox.showwarning("Campos vazios", "Preencha todos os campos.")

        def exportar_csv():
            caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if not caminho_arquivo:
                return

            try:
                with open(caminho_arquivo, mode="w", newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Cliente", "Produto", "Valor", "Forma de Pagamento", "Data"])
                    for row in self.tree_financeiro.get_children():
                        writer.writerow(self.tree_financeiro.item(row)["values"])
                messagebox.showinfo("Exportado", f"Relatório salvo em:\n{caminho_arquivo}")
            except Exception as e:
                messagebox.showerror("Erro ao exportar", str(e))

        def remover_compra():
            item = self.tree_financeiro.selection()
            if item:
                self.tree_financeiro.delete(item)
            else:
                messagebox.showinfo("Remover", "Selecione um item para remover.")

        tk.Button(frame_financeiro, text="Registrar Compra", command=adicionar_compra).pack(pady=5)
        tk.Button(frame_financeiro, text="Remover Registro", command=remover_compra).pack(pady=5)
        tk.Button(frame_financeiro, text="Exportar Relatório (CSV)", command=exportar_csv).pack(pady=5)
        tk.Button(frame_financeiro, text="Voltar ao Menu", command=lambda: self.mostrar_tela(self.tela_principal)).pack(pady=10)

        return frame_financeiro

    def configurar_tela_logistica (self):

        logistica_titulo = tk.Label(self.tela_logistica, text="Logística - Registro de Entregas", font=("Arial", 16))
        logistica_titulo.pack(pady=10)

        frame_logistica = tk.Frame(self.tela_logistica, padx=20)
        frame_logistica.pack(fill="both", expand=True, pady=10)

        form_frame_logistica = tk.Frame(frame_logistica)
        form_frame_logistica.pack(pady=10)

        self.rua_var = self.criar_entry(form_frame_logistica, "Rua:", 0)
        self.cidade_var = self.criar_entry(form_frame_logistica, "Cidade:", 1)
        self.cep_var = self.criar_entry(form_frame_logistica, "CEP:", 2)
        self.rastreio_var = self.criar_entry(form_frame_logistica, "Código de Rastreio:", 3)

        self.tree_logistica = ttk.Treeview(frame_logistica, columns=("Rua", "Cidade", "CEP", "Rastreio"), show="headings")
        for col in ("Rua", "Cidade", "CEP", "Rastreio"):
            self.tree_logistica.heading(col, text=col)
            self.tree_logistica.column(col, width=150)
        self.tree_logistica.pack(pady=10, fill="x", expand=True)

        tk.Button(frame_logistica, text="Registrar Entrega", command=self.adicionar_entrega_logistica).pack(pady=5)
        tk.Button(frame_logistica, text="Remover Registro", command=lambda: self.remover_item(self.tree_logistica)).pack(pady=5)
        tk.Button(frame_logistica, text="Exportar Histórico (CSV)", command=self.exportar_logistica_csv).pack(pady=5)

        busca_frame = tk.Frame(frame_logistica)
        busca_frame.pack(pady=10)
        tk.Label(busca_frame, text="Buscar por Cidade ou Código:").pack(side="left", padx=5)
        self.busca_var = tk.StringVar()
        tk.Entry(busca_frame, textvariable=self.busca_var, width=30).pack(side="left", padx=5)
        tk.Button(busca_frame, text="Buscar", command=self.buscar_logistica).pack(side="left")

        tk.Button(frame_logistica, text="Voltar ao Menu", command=lambda: self.mostrar_tela(self.tela_principal)).pack(pady=10)

        return frame_logistica

    def adicionar_entrega_logistica(self):
        rua = self.rua_var.get()
        cidade = self.cidade_var.get()
        cep = self.cep_var.get()
        rastreio = self.rastreio_var.get()

        if rua and cidade and cep and rastreio:
            self.tree_logistica.insert("", "end", values=(rua, cidade, cep, rastreio))
            self.rua_var.set("")
            self.cidade_var.set("")
            self.cep_var.set("")
            self.rastreio_var.set("")
        else:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos para registrar a entrega.")

    def exportar_logistica_csv(self):
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not caminho_arquivo:
            return

        try:
            with open(caminho_arquivo, mode="w", newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Rua", "Cidade", "CEP", "Código de Rastreio"])
                for row in self.tree_logistica.get_children():
                    writer.writerow(self.tree_logistica.item(row)["values"])
            messagebox.showinfo("Exportado", f"Histórico salvo em:\n{caminho_arquivo}")
        except Exception as e:
            messagebox.showerror("Erro ao exportar", str(e))

    def buscar_logistica(self):
        termo = self.busca_var.get().lower().strip()
        if not termo:
            messagebox.showinfo("Busca vazia", "Digite um termo para buscar.")
            return

        resultados = []
        for item in self.tree_logistica.get_children():
            valores = self.tree_logistica.item(item)["values"]
            if termo in str(valores[1]).lower() or termo in str(valores[3]).lower():
                resultados.append((item, valores))

        if not resultados:
            messagebox.showinfo("Nenhum resultado", "Nenhum registro encontrado.")
            return

        for item in self.tree_logistica.get_children():
            self.tree_logistica.item(item, tags="")

        for item, _ in resultados:
            self.tree_logistica.item(item, tags=("encontrado",))

        self.tree_logistica.tag_configure("encontrado", background="lightblue")

    def remover_item(self, tree):
        item = tree.selection()
        if item:
            tree.delete(item)
        else:
            messagebox.showinfo("Remover", "Selecione um item para remover.")


# Iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = SoftwareCRM(root)
    root.mainloop()