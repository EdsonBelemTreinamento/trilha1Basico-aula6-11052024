python -m venv venv

## Próxima etapa ativar o venv
cd  venv
cd Scripts
activate
cd .. 
cd ..

pip install pymysql
pip install flask
### Mysql
## 



entrar no mysql, primeiro criar o banco de dados

e acessar o banco de dados

create database bancodata;
use bancodata;
create table users(id varchar(255) primary key,
 name varchar (50),
 email varchar (250) unique,
 password varchar (250),
 status varchar (50)
);
desc users;
insert into users values ('100','luciana','luciana@gmail.com','123456', 'inativo');
select * from users;
select * from users where id='100';
select * from users where name='luciana';
## delete from users; não existe ...
## drop table users;
### Seguir o Padrão da Programação
## EDA (status) == 'ativo', 'logado', 'logoff', 'inativo'







