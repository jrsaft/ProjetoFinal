import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import datetime

class SoftwareCRM:
    def __init__(self, root): # root é o objeto da classe
        self.root = root #Janela principal 
        self.root.title("Plataforma Inteligente de Atendimento ao Cliente")
        self.root.geometry("1000x800")
        self.root.resizable(True, True) #Tornar a janela redimensionável horizontal e verticalmente.

        self.container = tk.Frame(root) #Cria um Frame dentro da janela, que é um contêiner em que você pode colocar outros widgets (botões, labels, etc.).
        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1) #row -> linhas.
        self.container.grid_columnconfigure(0, weight=1) #column -> colunas.

        self.tela_principal = tk.Frame(self.container) #Adiciona o container dentro do frame
        self.tela_perguntas_info = tk.Frame(self.container)
        self.tela_cadastro_cliente = tk.Frame(self.container)
        self.tela_infos = tk.Frame(self.container)
        self.tela_atendimento = tk.Frame(self.container)
        self.tela_logistica = tk.Frame(self.container)
        self.tela_financeiro = tk.Frame(self.container)
         

        for tela in (self.tela_principal,self.tela_perguntas_info, self.tela_cadastro_cliente, self.tela_infos, self.tela_atendimento,
                     self.tela_logistica, self.tela_financeiro): #empilhar várias "telas" umas sobre as outras no mesmo lugar. Uma delas será visivel por vez.
            tela.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(self.tela_principal)

        self.configurar_tela_principal(self.tela_principal)

    
    def mostrar_tela(self, tela):
        tela.tkraise()

    def configurar_tela_principal(self):
        frame = tk.Frame(self.tela_principal, padx=20, pady=20)#Criação do frame
        frame.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame, text="Plataforma Inteligente de atendimento ao cliente", font=(Arial, 16, "bold") )
        titulo.pack(pady=(0,30)) #(cima,baixo)

        btn_info_cliente = tk.Button(frame, text="Clientes", width=25, height=2,
                                         command=lambda: self.mostrar_tela(self.tela_infos)) #command=lambda: troca a tela atual para a tela de cadastro.
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
        frame_perguntas_info = tk.Frame(self.configurar_tela_perguntas_info, padx=30)
        frame_perguntas_info.pack(fill="both",expand=True, pady=10)

        titulo_perguntas_info = tk.Label(self.tela_perguntas_info, text="Qual ação você \n deseja realizar?", font=(Arial, 30, "bold"))
        titulo_perguntas_info.pack(pady=35)

        btn_perguntas_cadastrar = tk.Button(frame, text="Cadastrar cliente", width=30, height=4,
                                         command=lambda: self.mostrar_tela(self.tela_infos)) #command=lambda: troca a tela atual para a tela de cadastro.
        btn_perguntas_cadastrar.pack(pady=10)

        btn_perguntas_consultar = tk.Button(frame, text="Consultar informações \n do cliente", width=30, height=4
                                            command=lambda: self.mostrar_tela(self.tela_info))
        btn_perguntas_consultar.pack(pady=10)


####### CRIAR TELA DE CADASTRO DE CLIENTES E ASSOCIAR AO BOTÃO DE CADASTRO.
    def configurar_tela_cadastro_cliente(self):
        frame_cadastro_cliente = tk.Frame(self.tela_cadastro_cliente, padx=30)
        frame_cadastro_cliente.pack(pady=35)

        titulo = tk.Label(self.tela_cadastro_cliente, text="CADASTRO DE CLIENTES", font=("Arial", 22, "bold"))
        titulo.pack(pady=20)

        tdois = tk.Label(self.tela_cadastro_cliente, text="Dados de Identificação do Cliente", font=("Arial",18, "bold"))
        tdois.pack(pady=15)

        tk.Label(frame_cadastro_cliente,text="Nome:").grid(row=0, column=0, sticky="e", pady=5)
        self.cliente_nome_entry = tk.Entry(frame_cadastro_cliente, width=30)
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
        ttres.pack(pady=15)

        frame_contato_cliente = tk.Frame(self.tela_cadastro_cliente, padx=30)
        frame_contato_cliente.pack(pady=10)

        tk.Label(frame_contato_cliente, text="Telefone:").grid(row=0, column=0, sticky="e", pady=5)
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
        tquatro.pack(pady=15)

        frame_extra_cliente = tk.Frame(self.tela_cadastro_cliente, padx=30)
        frame_extra_cliente.pack(pady=10)

        # Histórico de rastreamento (entrada múltipla, separada por vírgula)
        tk.Label(frame_extra_cliente, text="Histórico de Rastreamento:").grid(row=0, column=0, sticky="e", pady=5)
        self.cliente_rastreamento_entry = tk.Entry(frame_extra_cliente, width=40)
        ####### COLOCAR O PADRÃO DE RASTREAMENTO
        self.cliente_rastreamento_entry.grid(row=0, column=1, sticky="w", pady=5)

        # Preferências de comunicação (checkboxes)
        tk.Label(frame_extra_cliente, text="Preferências de Comunicação:").grid(row=1, column=0, sticky="ne", pady=5)

        self.pref_whatsapp = tk.BooleanVar() #Váriaveis do tipo booleana
        self.pref_email = tk.BooleanVar()

        check_frame = tk.Frame(frame_extra_cliente) #Criação de um frame para o checkbutton
        check_frame.grid(row=1, column=1, sticky="w")

        tk.Checkbutton(check_frame, text="WhatsApp", variable=self.pref_whatsapp).pack(anchor="w")
        tk.Checkbutton(check_frame, text="E-mail", variable=self.pref_email).pack(anchor="w")

        # Avaliações anteriores (apenas exibição por enquanto)
        tk.Label(frame_extra_cliente, text="Avaliações Anteriores:").grid(row=2, column=0, sticky="ne", pady=5)
        ##### CONTINUIDADE COM O SOR

        # Tipo de serviços utilizados
        ###### CADASTRAR UM CAMPO PARA ARMAZENAR OS TIPOS DE ENVIO ESCOLHIDOS PELO CLIENTE (Sedex, PAC, Logística Reversa, etc.)

        # Histórico de envios e recebimentos
        ##### ARMAZENAR AS VEZES QUE O CLIENTE ENVIOU OU RECEBEU ALGO, JUNTO COM O ENDEREÇO

        # Ocorrências (extravio, atraso, devolução, etc.)
        #### ARMAZENAR DADOS DE ALGUM PROBLEMA QUE O CLIENTE TENHA PASSADO.

        # Autenticado (checkbox)
        self.cliente_autenticado_var = tk.BooleanVar(value=True)
        self.auth_checkbox = tk.Checkbutton(frame_extra_cliente, text="Cliente Autenticado", variable=self.cliente_autenticado_var)
        self.auth_checkbox.grid(row=4, columnspan=2, sticky="w", pady=5)

        # Chamados anteriores / tickets de suporte
        tk.Label(frame_extra_cliente, text="Protocolos anteriores:").grid(row=5, column=0, sticky="e", pady=5)
        #### vincular os próximos chamados para esse banco de dados, apenas informando o código.

        # Botão de salvar informações
        btn_salvar = tk.Button(self.tela_cadastro_cliente, text="Salvar Cadastro", command=self.salvar_cliente)
        btn_salvar.pack(pady=20)


    def configurar_tela_infos(self):
        frame_infos = tk.Frame(self.tela_infos, padx=20)
        frame_infos.pack(fill="both", expand=True, pady=10)

        infos_titulo = tk.Label(self.tela_infos, text="Informações dos clientes", font=(Arial, 20, "bold"))
        infos_titulo.pack(pady=20)

        scrollbar = tk.Scrollbar(infos_titulo) #Cria a barra de rolagem;
        scrollbar.pack(side="right", fill="y") #fill="y": faz com que a scrollbar preencha toda a altura vertical do lista_frame.

        self.listbox_clientes = tk.Listbox(frame_infos, width=90, height=10, font=("Arial", 10)) #Cria um widget Listbox, que é uma caixa de seleção/lista para mostrar múltiplos itens, dentro do frame_infos.
        self.listbox_clientes.pack(side="left", fill="both", expand=True)

        self.listbox_clientes.config(yscrollcommand=scrollbar.set) #conexão entre a barra de rolagem e a lista;
        scrollbar.config(command=self.listbox_clientes.yview) #O método self.listbox_proprietarios.yview é chamado para mostrar a parte correta da lista correspondente à posição da scrollbar.

        tk.Button(botoes_frame, text="Ver Detalhes", width=12,
                  command=self.ver_detalhes_proprietario).pack(side="left", padx=5)

        tk.Button(botoes_frame, text="Voltar", width=12,
                  command=lambda: self.mostrar_tela(self.tela_principal)).pack(side="left", padx=5)

