Projeto de Transformação de Dados
=================================
  
Este projeto realiza a extração dos dados da tabela do web_scraping anexo1.pdf, salva em csv, altera as abreviações OD e AMB pelas descrições completas e compacta para a pasta Teste_Karoline.zip.

   Tecnologias

- Python  
 
   Pré-requisitos

Antes de começar, certifique-se de ter o Python instalado em seu sistema.

   Instalação

Clone este repositório e instale as dependências:


pip install -r requirements.txt


   Como Executar

Execute no CMD dentro da pasta do projeto:

 
python transf_dados.py
 

   Arquivos Gerados

Após a execução, os seguintes arquivos serão gerados:

-  anexo1.pdf
-  anexo2.pdf
-  Teste_Karoline.zip

Observações

- É necessária conexão com a internet para baixar os arquivos.
- Caso já exista arquivos, deverão ser deletados ou será criado uma nova cópia.

