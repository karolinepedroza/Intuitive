import mysql.connector
import os

# Configurações de conexão com o banco de dados
config = {
    'host': '127.0.0.1',       # altere se necessário
    'user': 'root',     # informe seu usuário do MySQL
    'password': '34182563',   # informe sua senha
    'database': 'estagio',     # banco de dados de destino
    'allow_local_infile': True # habilita o LOAD DATA LOCAL INFILE
}

try:
    conexao = mysql.connector.connect(**config)
    cursor = conexao.cursor()
    print("Conectado com sucesso ao banco de dados 'estagio'.")
except mysql.connector.Error as err:
    print("Erro de conexão:", err)
    exit(1)

# Lista dos arquivos SQL a serem carregados
arquivos = ["script1.sql", "script2.sql"]

# Caminho onde os arquivos estão localizados
caminho = r"c:\Intuitive\querys_mysql\\"

# Para cada arquivo, executa o comando LOAD DATA LOCAL INFILE
for arquivo in arquivos:
    caminho_completo = os.path.join(caminho, arquivo)
    # Atenção: ajuste 'sua_tabela' para o nome da tabela de destino
    comando =comando = f"""LOAD DATA LOCAL INFILE 'c:/Intuitive/banco_de_dados/2024/1T2024.csv'
        INTO TABLE contabil
        FIELDS TERMINATED BY ';'
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;"""
    try:
        cursor.execute(comando)
        conexao.commit()
        print(f"Arquivo {arquivo} carregado com sucesso.")
    except mysql.connector.Error as err:
        print(f"Erro ao carregar {arquivo}: {err}")

cursor.close()
conexao.close()
print("Processo finalizado.")