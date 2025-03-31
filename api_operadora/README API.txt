 README - API  

Esta é a API que retorna a lista de operadoras cadastradas.  

--------------------------------
IMPORTANTE: Crie o arquivo .env e substitua para conectar ao banco.
DB_USER=
DB_PASSWORD= 
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME= 
----------------------------------

URL Base  

A API roda no seguinte endereço:  

http://localhost:8000

Endpoint  

Lista de Cadastros de Operadoras

- URL: /lista_cadastros_operadoras
- Método: GET
- Autenticação: Não necessária  

Resposta de Sucesso

- Código: 200 OK 
- Descrição: Retorna a lista completa de operadoras cadastradas.  

Instalação  

Para rodar a API, instale as dependências:  
bash
pip install fastapi uvicorn sqlalchemy mysql-connector-python python-dotenv


Depois, execute o servidor:  
bash
uvicorn main:app --reload


Agora a API estará rodando em http://localhost:8000.