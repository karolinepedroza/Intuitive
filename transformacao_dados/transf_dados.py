import pdfplumber
import pandas as pd
import os
import csv

def criar_caminhos():
    
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_raiz = os.path.dirname(os.path.dirname(diretorio_atual))
    
    caminho_pdf = os.path.join(diretorio_raiz, "Intuitive/web_scraping", "anexo1.pdf")
    caminho_csv = os.path.join(diretorio_atual, "Rol_anexo1.csv")
    
    if not os.path.exists(caminho_pdf):
        raise FileNotFoundError(f"Arquivo PDF não encontrado em: {caminho_pdf}")
    
    return caminho_pdf, caminho_csv

def extrair_pdf_para_csv(caminho_pdf, caminho_csv):
    """Extrai tabelas do PDF e salva em CSV"""
    with pdfplumber.open(caminho_pdf) as pdf:
        with open(caminho_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            
            for pagina in pdf.pages:
                tabela = pagina.extract_table()
                if tabela:
                    writer.writerows(tabela)

def processar_dados_csv(caminho_csv):

    df = pd.read_csv(caminho_csv)
    substituicoes = {
        "OD": "Seg. Odontológica",
        "AMB": "Seg. Ambulatorial"
    }
    
    df.rename(columns=substituicoes, inplace=True)
    df.replace(substituicoes, inplace=True)
    
    return df

def salvar_csv_comprimido(df, nome_arquivo='Teste_Karoline.zip'):

    df.to_csv(
        nome_arquivo,
        compression={'method': 'zip', 'archive_name': 'Rol_anexo1ok.csv'},
        index=False
    )

def main():
    caminho_pdf, caminho_csv = criar_caminhos()
    
    extrair_pdf_para_csv(caminho_pdf, caminho_csv)
    
    df_processado = processar_dados_csv(caminho_csv)
    
    salvar_csv_comprimido(df_processado)

if __name__ == "__main__":
    main()