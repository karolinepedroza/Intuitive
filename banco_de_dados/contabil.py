import os
import pandas as pd 
import numpy as np  

download_dir = "2024"

tipos_colunas_contabil = {
    'REGISTRO_ANS': 'str',
    'DATA': 'str',
    'CD_CONTA_CONTABIL': 'str',
    'DESCRICAO': 'str',
    'VL_SALDO_INICIAL': 'str', 
    'VL_SALDO_FINAL': 'str'     
}

required_columns = tipos_colunas_contabil.keys()


for arquivo in os.listdir(download_dir):
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(download_dir, arquivo)
        
        df = pd.read_csv(caminho_arquivo,
                        sep=";",
                        encoding="utf-8",
                        dtype=tipos_colunas_contabil,
                        keep_default_na=False)
        
        df = df.dropna(how='all')
        
        for col in ['VL_SALDO_INICIAL', 'VL_SALDO_FINAL']:    
            df[col] = df[col].str.replace('.', '').str.replace(',', '.').astype(float)
        
        df.to_csv(caminho_arquivo,
                sep=";",
                index=False,
                quoting=1)
                    
        print(f"Arquivo {arquivo} processado com sucesso")




            
        