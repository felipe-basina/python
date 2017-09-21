    -- drop table if exists person;
    create table person (
    id integer primary key autoincrement,
    name text not null,
    username text not null,
    email text not null,
	creation_date datetime
);