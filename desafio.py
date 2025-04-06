from sqlalchemy import create_engine

# Conctar sqlite em memória
engine = create_engine('sqlite:///meubancodbdesafio.db', echo=True)

print('Coneção de sistema estabelecida')