-- Remove registros
delete from campanha;
delete from cliente;
delete from tiime;

-- Registros para tabela time
insert into tiime (nome) values ("time-1"), ("time-2"), ("time-3"), ("time-4"), ("time-5");

-- Registros para tabela cliente
insert into cliente (nome_cliente, email, dt_nascimento, id_time) values 
("cliente-1", "cliente1@email.com", '1980-01-20', (select max(id) from tiime)), 
("cliente-2", "cliente2@email.com", '1980-02-20', (select min(id) from tiime)), 
("cliente-3", "cliente3@email.com", '1980-03-20', (select min(id) from tiime)), 
("cliente-4", "cliente4@email.com", '1980-04-20', (select max(id) from tiime));

-- Registros para tabela campanha
insert into campanha (nome_campanha, id_time, dt_inicio_vigencia, dt_fim_vigencia) values
("campanha-1", (select max(id) from tiime), '2017-10-01', '2017-10-03'),
("campanha-2", (select min(id) from tiime), '2017-10-01', '2017-10-02'),
("campanha-3", (select max(id) from tiime), '2016-05-01', '2016-06-03'),
("campanha-4", (select min(id) from tiime), '2017-08-01', '2017-09-02');