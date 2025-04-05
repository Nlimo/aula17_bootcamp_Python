from sqlalchemy import create_engine

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubancodb.db', echo=True)


print('Coneção de sistema estabelecida')