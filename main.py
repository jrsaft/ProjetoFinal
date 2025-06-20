import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import datetime
import random
import string
from models import bancodedados
from models.bancodedados import DBService

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
    
    def mostrar_tela(self, tela):
        tela.tkraise()

    def configurar_tela_principal(self):
        frame = tk.Frame(self.tela_principal, padx=20, pady=20)#Criação do frame
        frame.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(frame, text="Plataforma Inteligente de atendimento ao cliente", font=("Arial", 16, "bold") )
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
        print("Configurando")
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

        banco = DBService()
        btn_salvar = tk.Button(frame_extra_cliente, text="Salvar", width=12, height=1,
    command=lambda: (
        print("NOME:", self.cliente_nome_entry.get()),
        print("CPF:", self.cliente_cpf_entry.get()),
        banco.criar_usuario(
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


    # def salvar_cliente(self):


        # banco = DBService()
        # banco.criar_usuario(
        #     self.cliente_nome_entry.get(),
        #     self.cliente_data_entry.get(),
        #     self.cliente_cpf_entry.get(),
        #     self.cliente_genero_entry.get(),
        #     self.cliente_telefone_entry.get(),
        #     self.cliente_email_entry.get(),
        #     self.cliente_endereco_entry.get(),
        #     self.cliente_cep_entry.get(),
        #     comunicacao
        # )


    def configurar_tela_infos(self):
        infos_titulo = tk.Label(self.tela_infos, text="Informações dos clientes", font=("Arial", 20, "bold"))
        infos_titulo.pack(pady=10)

        tk.Label(self.tela_infos, text="Nome do cliente:").pack(ipady=5)
        self.cliente_entry = tk.Entry(self.tela_infos, width=15)
        self.cliente_entry.pack(ipady=5)

        botoes_frame = tk.Frame(self.tela_infos)
        botoes_frame.pack(pady=15)

        tk.Button(botoes_frame, text="Pesquisar", width=12, command=self.pesquisar_cliente).pack(side="left", padx=20)

        frame_infos = tk.Frame(self.tela_infos, padx=30)
        frame_infos.pack(fill="both", expand=True, pady=10)

        self.listbox_clientes = tk.Listbox(frame_infos, width=40, height=5, font=("Arial", 10)) #Cria um widget Listbox, que é uma caixa de seleção/lista para mostrar múltiplos itens, dentro do frame_infos.
        self.listbox_clientes.pack(side="left", fill="both", expand=True)

        tk.Button(botoes_frame, text="Voltar", width=12,
                  command=lambda: self.mostrar_tela(self.tela_principal)).pack(side="bottom", padx=20, pady=20)
        
    def pesquisar_cliente(self):
        nome_digitado = self.cliente_entry.get().strip().lower()
        self.listbox_clientes.selection_clear(0, tk.END)  # Limpa seleções anteriores

        for idx in range(self.listbox_clientes.size()):
            item = self.listbox_clientes.get(idx).lower()
            if nome_digitado in item:
                self.listbox_clientes.selection_set(idx)
                self.listbox_clientes.see(idx)  # Garante que o item selecionado fique visível
                return

        messagebox.showinfo("Resultado da busca", "Cliente não encontrado.")

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

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

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
        self.cliente_endereco_entry = tk.Entry(frame_destinatario, width=15)
        self.cliente_endereco_entry.grid(row=2, column=1, sticky="w", pady=5)

        tk.Label(frame_destinatario, text="Bairro:").grid(row=3, column=0, sticky="e", pady=5)
        self.cliente_bairro_entry = tk.Entry(frame_destinatario, width=15)
        self.cliente_bairro_entry.grid(row=3, column=1, sticky="w", pady=5)

        tk.Label(frame_destinatario, text="CEP:").grid(row=4, column=0, sticky="e", pady=5)
        self.cliente_cep_entry = tk.Entry(frame_destinatario, width=15)
        self.cliente_cep_entry.grid(row=4, column=1, sticky="w", pady=5)

        pagamento_titulo = tk.Label(content_frame, text="Informações do pagamento.", font=("Arial", 15, "bold"))
        pagamento_titulo.pack(pady=10)

        frame_pagamento = tk.Frame(content_frame)
        frame_pagamento.pack(pady=5)

        tk.Label(frame_pagamento, text="Forma de pagamento:").grid(row=0, column=0, sticky="e", pady=5)
        self.forma_pagamento_entry = tk.Entry(frame_pagamento, width=15)
        self.forma_pagamento_entry.grid(row=0, column=1, sticky="w", pady=5)

        botoes_frame = tk.Frame(self.tela_envio)
        botoes_frame.pack(pady=15)

        tk.Button(botoes_frame, text="Voltar", width=12,
                    command=lambda: self.mostrar_tela(self.tela_atendimento)).pack(side="bottom", padx=20, pady=20)
            
                    
    def configurar_tela_reversa(self):
    # Tela para realizar uma devolução.
        
        reversa_titulo = tk.Label(self.tela_reversa, text="Logistica reversa.", font=("Arial", 20, "bold"))
        reversa_titulo.pack(pady=10)

        frame_reversa = tk.Frame(self.tela_reversa, padx=30)
        frame_reversa.pack(pady=22)

        tk.Label(frame_reversa,text="Rastreio da devolução:").grid(row=0, column=0, sticky="e", pady=5)
        self.cliente_nome_entry = tk.Entry(frame_reversa, width=15)
        self.cliente_nome_entry.grid(row=0, column=1, sticky="w", pady=5)

        tk.Label(frame_reversa, text="CPF do cliente:").grid(row=1, column=0, sticky="e", pady=5)
        self.cliente_cpf_entry = tk.Entry(frame_reversa, width=15)
        self.cliente_cpf_entry.grid(row=1, column=1, sticky="w", pady=5)

        # tk.Label(frame_reversa, text="")

# Iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = SoftwareCRM(root)
    root.mainloop()