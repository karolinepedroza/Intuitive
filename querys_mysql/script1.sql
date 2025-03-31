
-- CRIAR E CARREGAR BANCO 

create database estagio;
use estagio;

create table cadastro_operadora (
    registro_ans varchar (20) ,
    cnpj varchar (255) ,
    razao_social varchar(255) ,
	nome_fantasia varchar (255) ,
    modalidade varchar (255),
    logradouro varchar (255),
    numero varchar (255),
    complemento varchar (255),
    bairro varchar (255) ,
    cidade varchar (255),
    uf varchar (255),
    cep varchar (255),
    ddd varchar(255),
    telefone varchar (255),
    fax varchar (255) ,
    endereco_eletronico varchar(255),
    representante varchar (255),
    cargo_Representante varchar(255),
    regiao_de_comercializacao varchar (255),
    data_registro_ans date not null
);


-- RODAR PRIMEIRO VERIFICAÇÃO A SEGUIR PARA AUTORIZAR CARGA COM ARQUIVO LOCAL

SHOW VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile=1;

-- CARGA ARQUIVO CSV REGISTRO OPERADORAS
 
LOAD DATA LOCAL INFILE 'C:/banco_de_dados/Relatorio_cadop.csv'
INTO TABLE cadastro_operadora
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

 
