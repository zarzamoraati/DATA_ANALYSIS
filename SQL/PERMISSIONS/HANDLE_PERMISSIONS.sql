create database gestion_permisos;
use gestion_permisos;

create table random_table(
permisoid int unique not null auto_increment,
nombre varchar(255) not null ,
contacto varchar(255) not null,
primary key(permisoid) 
);


insert into random_table(nombre,contacto)
values("john","@johndoe"),("nasted","@blinded"),("somik","@sonia");

-- 1)CREAR USUSARIO 
create user 'deldrima'@'localhost' identified by '112233';
-- 2) ASIGNA PERMISOS
grant select on gestion_permisos.* to 'deldrima'@'localhost';
-- 3) Verificar permisos del usario 
show grants for 'deldrima'@'localhost';
-- 4) Actualiza cambios en tablas
flush privileges;
-- 5) Revocar priviliegios
revoke select on gestion_permisos.* from 'deldrima'@'localhost';
show grants for 'deldrima'@'localhost';

-- Agregar paso de permisos

grant select on gestion_permisos.* to 'deldrima'@'localhots' with grant option;
show grants for 'deldrima'@'localhost';
