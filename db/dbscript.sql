drop table if exists users;
create table users (
    id serial primary key,
    email varchar(120) unique not null,
    password_hash varchar(155) not null
);
insert into users (email, password_hash) values ('admin@admin.com', 12345);
drop table if exists token_blacklist;
create table token_blacklist (
    id serial primary key,
    jti varchar(120)
);