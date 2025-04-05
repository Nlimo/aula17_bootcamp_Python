from sqlalchemy import create_engine

# Conectar ao SQLite em memória
engine = create_engine ('sqlite://meubancodb', echo = True)

print('Coneção de sistema estabelecida')