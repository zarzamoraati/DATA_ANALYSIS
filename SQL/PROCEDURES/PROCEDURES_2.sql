drop database temp_query;


create database temp_query ;
use temp_query ;

CREATE TABLE cuentas (
    cuentaid INT not null unique auto_increment PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE transacciones (
    transaccionid INT unique not null auto_increment PRIMARY KEY,
    cuenta_origen INT,
    cuenta_destino INT,
    monto DECIMAL(10, 2),
    fecha TIMESTAMP
);



create table clientes (
clienteid int unique not null auto_increment,
nombre varchar(255),
primary Key(clienteid)
);


create table scorts(
scortid int unique not null auto_increment,
scort_name varchar(255),
contacto varchar(255),
skin varchar(55),
age int,
arancel decimal(10,2),
primary key(scortid)
);


create table cartera (
 carteraid int not null unique auto_increment,
 cuentaid int,
 clienteid int,
scortid int,
saldo decimal(10,2),
 primary key(carteraid),
 foreign key (cuentaid) references cuentas(cuentaid),
 foreign key(clienteid) references clientes(clienteid),
foreign key(scortid) references scorts(scortid) 
);




insert into cuentas(nombre) 
values ("banamex"),("banorte"),("citi");
insert into clientes (nombre)
values("Master");
insert into scorts (scort_name,contacto,skin,age,arancel)
values("Noemi","@pure_noemi","white",25,2500.00),
("Deldrima","@fun_deldrimas","white",12,1200.00),
("Esmeralda","@lui_bridget","white",31,3500.00);

select * from clientes;
select * from scorts;

select * from cuentas;
insert into cartera(
 cuentaid,
 clienteid ,
saldo)values(1,1,5000);
select * from scorts;

insert into cartera(
 cuentaid,
 scortid ,
saldo)values(3,1,1200);

insert into cartera(
 cuentaid,
 scortid ,
saldo)values(1,2,2000);

insert into cartera(
 cuentaid,
 scortid ,
saldo)values(2,3,50);


select scort_name from scorts where scortid in (select scortid from cartera where cuentaid=2);
-- call scort with id=1

delimiter //
create procedure call_scort(idchoise int)
begin
-- var declarate
declare arancel decimal(10,2);
declare saldo_cliente decimal(10,2);
declare saldo_scort decimal(10,2);
 -- iniciar transaccion
 start transaction;
 select s.arancel into arancel from scorts s where scortid=idchoise;
select saldo into saldo_cliente from cartera where clienteid=1;
select saldo into saldo_scort from cartera where scortid=idchoise;
--
update cartera 
set saldo = saldo_cliente-arancel
where clienteid=1;

update cartera
set saldo = saldo_scort + arancel 
where scortid=1;

insert into transacciones(cuenta_origen ,cuenta_destino,monto,fecha)
values(1,idchoise,arancel,now());
 -- comprobar si la transaccion es valida
 if arancel > saldo_cliente then
  rollback;-- error
else 
  commit; -- confirmar
  end if;
end //
delimiter ;
call call_scort(1);

select * from cartera;
select * from scorts s left join cartera c on s.scortid=c.scortid ;
select * from clientes c left join cartera ca  on c.clienteid=ca.clienteid;



drop procedure if exists call_scort;


select * from transacciones;

select * from cartera c left join scorts s on c.scortid=s.scortid;





