"""
Arquivo que contém as classes que representam os modelos do banco de dados.

Classes:
 - Usuario: Classe que representa a tabela 'usuarios' no banco de dados.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base para nossos modelos
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    datadenascimento = Column(Integer)
    cpf = Column(String)
    genero = Column(String(10), nullable=False)
    telefone = Column(Integer)
    email = Column(String(40), nullable=False)
    endereco = Column(String(100), nullable=False)
    cep = Column(Integer)
    comunicacao = Column(String(10), nullable=False)

def __repr__(self):
    return f"<Usuario(nome='{self.nome}', idade={self.idade})>"

class Envios(Base):
    __tablename__= "Envio" 

    id = Column(Integer, primary_key=True)
    
    nomedoremetente = Column(String, nullable=False)
    cpfdoremetente = Column(String, nullable=False)
    enderecodoremetente = Column(String, nullable=False)
    bairrodoremetente = Column(String, nullable=False)
    cepdoremetente = Column(String, nullable=False)

    rastreio = Column(String, nullable=False)
    tipodeservico = Column(String, nullable=False)  

    nomedodestinatario = Column(String, nullable=False)
    cpfdodestinatario = Column(String, nullable=False)
    enderecododestinatario = Column(String, nullable=False)
    bairrododestinatario = Column(String, nullable=False)
    cepdodestinatario = Column(String, nullable=False)

    formadepagamento = Column(String, nullable=False)
    valor = Column(String, nullable=False)   

def __repr__(self):
    return f"<Envio(rastreio='{self.rastreio}')>"