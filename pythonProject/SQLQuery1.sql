create database petshop
use petshop

create table petshop(
	Id int PRIMARY KEY IDENTITY,
	tipo_pet varchar(30),
	nome_pet varchar(30),
	idade INT
);

select * from petshop

INSERT into petshop VALUES ('Gato', 'Augusto', 3);