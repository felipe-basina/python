CREATE TABLE cidades (
	-- id INTEGER PRIMARY KEY AUTOINCREMENT,
	id INTEGER PRIMARY KEY,
	cidade TEXT UNIQUE,
	uf VARCHAR(2)
);
CREATE TABLE pessoas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	sobrenome TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	cidade_id INTEGER,
	criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (cidade_id) REFERENCES cidades(id)
);