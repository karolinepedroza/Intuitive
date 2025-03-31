Aplicativo de Busca em Vue

Este é um projeto simples feito com Vue.js que permite buscar operadoras digitando um nome em um campo de pesquisa. Ele se conecta a uma API para buscar os dados e mostrar os resultados na tela.

Estrutura do Projeto

vue-search-app  
├── src  
│   ├── App.vue                # Componente principal  
│   ├── components  
│   │   └── SearchField.vue    # Campo de busca  
│   ├── services  
│   │   └── api.js             # Arquivo para conectar com a API  
│   └── main.js                # Arquivo de entrada do Vue  
├── package.json               # Configuração do projeto  
└── README.md                  # Documentação  

Como Usar

    Baixar o projeto:

git clone <repository-url>
cd interface

Instalar as dependências:

npm install

Rodar o projeto:

    npm run serve

    Abrir no navegador:
    Vá para http://localhost:8080.

Funcionalidade

    Digite o nome de uma operadora no campo de busca.

    A aplicação enviará a busca para a API e mostrará os resultados.

Importante

A busca funciona com uma requisição POST para a API. Certifique-se de que a API esteja rodando.
