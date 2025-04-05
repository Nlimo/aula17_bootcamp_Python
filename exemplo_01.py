from sqlalchemy import create_engine

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubancodb.db', echo=True)


print('Coneção de sistema estabelecida')

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key= True)
    nome = Column(String)
    idade = Column(Integer)

# Criar uma tabela no banco de dados

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome='João', idade=28)
session.add(novo_usuario)
session.commit()

print("Usuário inserido com sucesso.")

# Consultando registros na tabela

usuario = session.query(Usuario).filter_by(nome='João').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")