#  Contabil

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

_____________________
#  Tratamento_Relatorio

Este repositório contém um script em Python que realiza o download, descompacta e processa arquivos CSV.

## Funcionalidades

- Download de arquivos a partir de URLs listadas no arquivo `link.txt`.
- Extração automática de arquivos ZIP baixados.
- Organização dos arquivos CSV em pastas correspondentes aos anos 2023 e 2024.
- Processamento do arquivo `Relatorio_cadop.csv`, incluindo:
  - Leitura dos dados com tipos de colunas especificadas.
  - Remoção de linhas completamente vazias.
  - Regravação do arquivo no formato CSV, preservando a estrutura original.

## Dependências

- Python 3.x
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [wget](https://pypi.org/project/wget/)

## Como Usar

1. Certifique-se de que o arquivo `link.txt` contendo as URLs dos arquivos a serem baixados esteja presente no mesmo diretório do script.
2. Execute o script Python:
   
   ```sh
   python tratamento_Relatorio.py
