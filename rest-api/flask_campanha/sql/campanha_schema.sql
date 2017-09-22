create table cliente (
    id integer primary key autoincrement,
    nome_cliente text not null,
	dt_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

create table campanha (
    id integer primary key autoincrement,
    nome_campanha text not null,
    id_time integer not null,
    dt_inicio_vigencia date,
	dt_fim_vigencia date,
	cliente_id integer,
	FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);