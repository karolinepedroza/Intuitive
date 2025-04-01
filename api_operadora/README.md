# README - API

Esta API fornece um endpoint para retornar a lista de operadoras cadastradas no sistema.

## Configuração do Banco de Dados

Antes de executar a API, crie um arquivo `.env` na raiz do projeto e adicione as seguintes configurações para conectar ao banco de dados:

```
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
```

## URL Base

A API roda no seguinte endereço:

```
http://localhost:8000
```

## Endpoint

### Lista de Cadastros de Operadoras

- **URL:** `/lista_cadastros_operadoras`
- **Método:** `GET`
- **Autenticação:** Não necessária

#### Resposta de Sucesso

- **Código:** `200 OK`
- **Descrição:** Retorna a lista completa de operadoras cadastradas no banco de dados.

## Instalação e Execução

### Instalação das Dependências

Para rodar a API, instale as dependências necessárias:

```
pip install fastapi uvicorn sqlalchemy mysql-connector-python python-dotenv
```

### Execução do Servidor

Após instalar as dependências, execute o servidor com o seguinte comando:

```
uvicorn main:app --reload
```

Agora a API estará disponível em `http://localhost:8000`.

Caso precise de mais detalhes sobre a estrutura do projeto ou configuração adicional, consulte a documentação do repositório principal.
