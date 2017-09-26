create table tiime (
	id integer primary key autoincrement,
	nome not null
);

create table cliente (
    id integer primary key autoincrement,
    nome_cliente text not null,
	email text not null,
	dt_nascimento date not null,
	id_time integer not null,
	dt_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (id_time) REFERENCES tiime(id)
);

create table campanha (
    id integer primary key autoincrement,
    nome_campanha text not null,
    id_time integer not null,
    dt_inicio_vigencia date,
	dt_fim_vigencia date,
	FOREIGN KEY (id_time) REFERENCES tiime(id)
);