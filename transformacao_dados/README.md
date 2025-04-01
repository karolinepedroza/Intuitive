# Projeto de Transformação de Dados

Este projeto realiza a extração de dados da tabela contida no arquivo `anexo1.pdf`, salva os dados em formato CSV, substitui abreviações específicas por suas descrições completas e, por fim, compacta os arquivos gerados na pasta `Teste_Karoline.zip`.

## Tecnologias Utilizadas

- Python

## Pré-requisitos

Antes de iniciar, certifique-se de que o Python está instalado no seu sistema.

## Instalação

Para configurar o ambiente, clone este repositório e instale as dependências necessárias executando:

```
pip install -r requirements.txt
```

## Como Executar

Dentro da pasta do projeto, utilize o seguinte comando no terminal para executar o script:

```
python transf_dados.py
```

## Arquivos Gerados

Após a execução do processo, os seguintes arquivos serão gerados:

- `anexo1.pdf`
- `anexo2.pdf`
- `Teste_Karoline.zip`

## Observações

- É necessário ter conexão com a internet para baixar os arquivos.
- Se os arquivos já existirem, será criada uma nova cópia ou será necessário excluí-los manualmente antes de uma nova execução.
