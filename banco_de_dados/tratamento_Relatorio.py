import wget 
import zipfile
import pandas as pd  
import numpy as np  
import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
download_dir = script_dir

# Download dos arquivos
link_path = os.path.join(script_dir, "link.txt")
with open(link_path, "r") as file:
    links = file.readlines()

# Download de todos os arquivos
for url in links:  # Mudança aqui: 'link' para 'links'
    url = url.strip()  # Remove espaços e quebras de linha
    filename = os.path.basename(url)
    file_path = os.path.join(download_dir, filename)
    
    if not os.path.exists(file_path):
        print(f"Baixando {filename}...")
        wget.download(url, file_path)
        print()

# Descompactar apenas arquivos ZIP
print("\nProcessando arquivos ZIP...")
for arquivo in os.listdir(download_dir):
    arquivo_path = os.path.join(download_dir, arquivo)
    
    # Verifica se é arquivo e se tem extensão .zip
    if os.path.isfile(arquivo_path) and arquivo.lower().endswith('.zip'):
        print(f"Descompactando {arquivo}...")
        with zipfile.ZipFile(arquivo_path, "r") as zip_ref:
            zip_ref.extractall(download_dir)
        os.remove(arquivo_path)
        print(f"Arquivo ZIP {arquivo} removido.")


dir_2023 = os.path.join(download_dir, "2023")
dir_2024 = os.path.join(download_dir, "2024")

os.makedirs(dir_2023, exist_ok=True)
os.makedirs(dir_2024, exist_ok=True)

for arquivo in os.listdir(download_dir):
    if arquivo.endswith('.csv') and arquivo != 'Relatorio_cadop.csv':
        origem = os.path.join(download_dir, arquivo)
        if '2023' in arquivo:
            destino = os.path.join(dir_2023, arquivo)
        else:
            destino = os.path.join(dir_2024, arquivo)
        shutil.move(origem, destino)
        print(f"Arquivo {arquivo} movido para a pasta correspondente.")

#---------BAIXA, DESCOMPACTA E APAGA OS .ZIP

tipos_colunas_relatorio = {
    'Registro_ANS': 'int64', 
    'CNPJ': 'str',  
    'Razao_Social': 'str',
    'Nome_Fantasia': 'str',
    'Modalidade': 'str', 
    'Logradouro': 'str', 
    'Numero': 'str', 
    'Complemento': 'str', 
    'Bairro': 'str', 
    'Cidade': 'str', 
    'UF': 'str',  
    'CEP': 'str', 
    'DDD': 'str', 
    'Telefone': 'str', 
    'Fax': 'str',  
    'Endereco_eletronico': 'str',  
    'Representante': 'str', 
    'Cargo_Representante': 'str',  
    'Regiao_de_Comercializacao': 'str', 
    'Data_Registro_ANS': 'str'  
}

required_columns = list(tipos_colunas_relatorio.keys())

relatorio_path = os.path.join(download_dir, "Relatorio_cadop.csv")
df = pd.read_csv(relatorio_path, 
                 sep=";",
                 encoding="utf-8",
                 dtype=tipos_colunas_relatorio,
                 keep_default_na=False)
 
df = df.dropna(how='all')
df.to_csv(relatorio_path, sep=";", index=False, quoting=1)