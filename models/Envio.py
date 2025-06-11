""" Aqui serão feito os envios para os clientes e automaticamente já salva os
 dados de envio ou recebimento. git add
"""
class Envio:
    def __init__(self, nome, cpf, telefone, endereco, bairro, cep, rastreio, 
                 tipo_servico, destinatario):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.bairro = bairro
        self.cep = cep
        self.rastreio = rastreio
        self.tipo_servico = tipo_servico
        self.destinatario = destinatario
        
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def get_telefone(self):
        return self.telefone
    
    def get_endereco(self):
        return self.endereco
    
    def get_bairro(self):
        return self.bairro
    
    def get_cep(self):
        return self.cep
    
    def get_rastreio(self):
        return self.rastreio
    
    def get_tipo_servico(self):
        return self.tipo_servico
    
    def get_destinatario(self):
        return self.destinatario
    
    # def enviar(self, nome, cpf, telefone, endereco, bairro, cep, rastreio, tipo_servico, destinatario):

    #     tk.Label(frame_cadastro_cliente,text="Nome:").grid(row=0, column=0, sticky="e", pady=5)
    #     self.cliente_nome_entry = tk.Entry(frame_cadastro_cliente, width=5)
    #     self.cliente_nome_entry.grid(row=0, column=1, sticky="w", pady=5)

    # def conferir_cliente(self, nome):
    #     if self.nome 

