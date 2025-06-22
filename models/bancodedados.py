from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.models import Usuario, Base, Envios
import sqlite3

class DBService:

    def __init__(self, banco):
        if banco == 'usuarios':
            self.engine = create_engine('sqlite:///database.db')
        elif banco == 'envios':
            self.engine = create_engine('sqlite:///database.envio.db')
        else:
            raise ValueError("Tipo de banco inválido")

        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def criar_usuario(self, nome: str, datadenascimento: str, cpf: str, genero: str, telefone: str, email: str,
                      endereco: str, cep: str, comunicacao: str) -> Usuario:
        # Criar novo usuário
        novo_usuario = Usuario(nome=nome, datadenascimento = datadenascimento, cpf = cpf, genero = genero, 
                               telefone = telefone, email = email, endereco = endereco, 
                               cep = cep, comunicacao = comunicacao)
        # Adicionar à sessão
        self.session.add(novo_usuario)
        # Salvar no banco
        self.session.commit()
        return novo_usuario


    def buscar_todos_usuarios(self) -> list[Usuario]:
        try:
            usuarios = self.session.query(Usuario).all()
        except Exception as e:
            print(e)
            usuarios = []
        return usuarios

    def buscar_usuarios_por_nome(self, nome) -> list[Usuario]:
        try:
            usuarios = self.session.query(Usuario).filter_by(nome=nome).all()
        except Exception as e: #o "e" é para definir qual foi o erro e mostrar ele no print.
            print(e)
            usuarios = []
        return usuarios

    def criar_envio(self, nomedoremetente: str, cpfdoremetente: str, enderecodoremetente: str, bairrodoremetente: str,  
                    cepdoremetente: str, rastreio: str, tipodeservico: str, nomedodestinatario: str,
                    cpfdodestinatario:str, enderecododestinatario: str, bairrododestinatario: str,
                    cepdodestinatario: str, formadepagamento: str, valor: str) -> Usuario:
        # Criar novo usuário
        novo_envio = Envios(nomedoremetente=nomedoremetente, cpfdoremetente = cpfdoremetente, enderecodoremetente = enderecodoremetente, 
                               bairrodoremetente = bairrodoremetente, cepdoremetente = cepdoremetente, rastreio = rastreio,
                               tipodeservico = tipodeservico, nomedodestinatario = nomedodestinatario, cpfdodestinatario= cpfdodestinatario,
                               enderecododestinatario = enderecododestinatario, bairrododestinatario = bairrododestinatario, cepdodestinatario = cepdodestinatario,
                               formadepagamento = formadepagamento, valor = valor)
        # Adicionar à sessão
        self.session.add(novo_envio)
        # Salvar no banco
        self.session.commit()
        return novo_envio

    def buscar_todos_envios(self) -> list[Envios]:
        try:
            envios = self.session.query(Envios).all()
        except Exception as e:
            print(e)
            envios = []
        return envios

    def buscar_envios_por_rastreio(self, rastreio) -> list[Envios]:
        try:
            envios = self.session.query(Envios).filter_by(rastreio=rastreio).all()
        except Exception as e: #o "e" é para definir qual foi o erro e mostrar ele no print.
            print(e)
            envios = []
        return envios
