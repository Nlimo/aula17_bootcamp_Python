from sqlalchemy import create_engine

# Conectar sqlite em memória
engine = create_engine('sqlite:///meubancodbdesafio.db', echo=True)

print('Coneção de sistema estabelecida')

# Criando minhas tabelas

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Produto(Base):
    __tablename__  = 'produtos'

    id = Column(Integer, primary_key=True)
    id_fornecedor = (Column, ForeignKey('fornecedores.id'))
    nome = Column(String)
    valor = Column(Integer)

# Opcional: backref para acessar os fornecedores do produto
fornecedores = relationship("Fornecedor", back_populates="produtos")


class Fornecedor(Base):
    __tablename__  = 'fornecedores'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    id_produto = Column(Integer, ForeignKey('produtos.id'))

# Relacionamento com Produto
produto = relationship("Produto", back_populates="fornecedores")

# Criando banco com as tabelas
Base.metadata.create_all(engine)