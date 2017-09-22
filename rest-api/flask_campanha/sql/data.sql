-- Remove registros
delete from campanha;
delete from cliente;

-- Registros para tabela cliente
insert into cliente (nome_cliente) values ("cliente-1"), ("cliente-2"), ("cliente-3"), ("cliente-4");

-- Registros para tabela campanha
insert into campanha (nome_campanha, id_time, dt_inicio_vigencia, dt_fim_vigencia, cliente_id) values
("campanha-1", 1001, '2017-10-01', '2017-10-03', 1),
("campanha-2", 1001, '2017-10-01', '2017-10-02', 1);