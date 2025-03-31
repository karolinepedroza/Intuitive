from typing import List, Dict
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pathlib import Path

#
BASE_DIR = Path(__file__).resolve().parent.parent  # api_operadora
PROJECT_ROOT = BASE_DIR.parent  # Intuitive folder
ENV_PATH = BASE_DIR / '.env'
# Carrega as variáveis de ambiente
load_dotenv(ENV_PATH)

# Configuração da connection string
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Monta a connection string
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(f"Tentando conectar ao banco: {DB_HOST}:{DB_PORT}/{DB_NAME}")

# Criação do engine com opções de conexão
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ...resto do código permanece igual...

def obter_cadastros_operadoras() -> List[Dict[str, str]]:
    """
    Consulta o banco de dados MySQL existente para obter os cadastros das operadoras.
    """
    print("Conectando ao banco de dados MySQL...")
    db = SessionLocal()
    try:
        query = text("""
            SELECT 
                registro_ans,
                cnpj,
                razao_social,
                nome_fantasia,
                modalidade,
                logradouro,
                numero,
                complemento,
                bairro,
                cidade,
                uf,
                cep,
                ddd,
                telefone,
                endereco_eletronico,
                representante,
                cargo_Representante,
                regiao_de_comercializacao,
                data_registro_ans
            FROM cadastro_operadora
        """)
        
        result = db.execute(query)
        rows = result.fetchall()
        
        operadoras = []
        for row in rows:
            operadora = {
                "registro_ans": row[0],
                "cnpj": row[1],
                "razao_social": row[2],
                "nome_fantasia": row[3],
                "modalidade": row[4],
                "logradouro": row[5],
                "numero": row[6],
                "complemento": row[7],
                "bairro": row[8],
                "cidade": row[9],
                "uf": row[10],
                "cep": row[11],
                "ddd": row[12],
                "telefone": row[13],
                "email": row[14],
                "representante": row[15],
                "cargo_representante": row[16],
                "regiao_comercializacao": row[17],
                "data_registro_ans": str(row[18]) if row[18] else None
            }
            operadoras.append(operadora)
        
        return operadoras
        
    except Exception as error:
        print(f"Erro detalhado: {str(error)}")
        raise Exception("Falha na consulta ao banco de dados.") from error
    finally:
        db.close()