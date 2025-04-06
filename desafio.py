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

# Relacionamento com Produto
produto = relationship("Produto", back_populates="fornecedores")

# Criando banco com as tabelas
Base.metadata.create_all(engine)


#################################################
# ADD DADOS 
#################################################

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

with Session() as session:

    fornecedor = [
        Fornecedor(id = 1, nome = 'Depósito 01'),
        Fornecedor(id = 2, nome = 'Depósito 02')
    ]

    session.add_all(fornecedor) #add_all deve ser utlizado pois é uma lista de objetos, se fosse so um, seria add()
    session.commit()

    produto = [
        Produto(id = 11, nome = 'Coca-Cola', valor = 5),
        Produto(id = 12, nome = 'Pepsi', valor = 4),
        Produto(id = 13, nome = 'Pepsi', valor = 4),
    ]

    session.add_all(produto)
    session.commit()