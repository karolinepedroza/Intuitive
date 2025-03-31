# Processamento de Arquivos CSV (contabil.py)

Este repositório contém um script em Python que realiza o processamento de arquivos CSV presentes no diretório `2024`.  

## Funcionalidades

- Leitura dos arquivos CSV com as colunas especificadas.
- Conversão de colunas de valores monetários, transformando de texto para float.
- Remoção de linhas que possuem todos os valores nulos.
- Regravação dos arquivos CSV com os dados processados.

## Dependências

- Python 3.x
- [Pandas](https://pandas.pydata.org/)  
- [NumPy](https://numpy.org/)

## Como Usar

1. Certifique-se de que o diretório `2024` esteja presente na mesma pasta que o script.
2. Coloque os arquivos CSV a serem processados dentro do diretório `2024`.
3. Execute o script:
   
   ```sh
   python contabil.py