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
    cpf = Column(Integer)
    genero = Column(String(10), nullable=False)
    telefone = Column(Integer)
    email = Column(String(40), nullable=False)
    endereco = Column(String(100), nullable=False)
    cep = Column(Integer)
    comunicacao = Column(String(10), nullable=False)

def __repr__(self):
    return f"<Usuario(nome='{self.nome}', idade={self.idade})>"