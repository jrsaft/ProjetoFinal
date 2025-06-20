from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.models import Usuario, Base

class DBService:

    def __init__(self):
        # Conectar ao banco
        self.engine = create_engine('sqlite:///database.db')
        Base.metadata.create_all(self.engine)
        # Criar uma sessão
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
