from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração de conexão
usuario = 'matheus_db'
senha = '251272'
host = 'localhost'  # ou o IP do servidor MySQL
banco = 'data_lake'

# URL de conexão
engine = create_engine(f'mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}')

# Base para o ORM
Base = declarative_base()

# Configuração da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_connection():
    """
    Cria uma conexão direta com o banco de dados para operações em lote.

    Retorna:
        connection: Objeto de conexão ao banco de dados.
    """
    return engine.raw_connection()
