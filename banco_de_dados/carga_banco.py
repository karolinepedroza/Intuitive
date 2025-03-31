import mysql.connector
import pandas as pd

# Conectar ao MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="34182563",
    database="estagio"
)

cursor = conn.cursor()

# Carregar o arquivo CSV com pandas
df = pd.read_csv("banco_de_dados/Relatorio_cadop.csv", sep=";", quotechar='"')

# Inserir os dados na tabela
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO cadastro_operadora (coluna1, coluna2, coluna3) VALUES (%s, %s, %s)",
        (row["coluna1"], row["coluna2"], row["coluna3"])
    )

conn.commit()
cursor.close()
conn.close()
