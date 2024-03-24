create database transaction2;
use transaction2;
CREATE TABLE cuentas(
cuentaid INT UNSIGNED NOT NULL,
saldo DECIMAL(7,2) NOT NULL,
PRIMARY KEY(cuentaid)
);
INSERT INTO cuentas VALUES (1, 1000);
INSERT INTO cuentas VALUES (2, 2000);
INSERT INTO cuentas VALUES (3, 3000);
select * from cuentas;

drop table cuentas;
-- Agregar una bonificaion a las cuentas si su saldo es superior a 1000

delimiter //
create procedure add_bonification(in id int,in bonificacion decimal(10,2))
begin 
-- declaracion de variables
declare saldo_cliente decimal(10,2);
-- execute transacccion
start transaction;
-- init var 
select saldo into saldo_cliente from cuentas where id=cuentaid;
update cuentas
set saldo=saldo_cliente+bonificacion
where id=cuentaid;

-- evaluar transacion
if saldo_cliente <= 1000.00 then
	rollback;
else 
	commit; 
end if; 
end // 
delimiter ;

call add_bonification(1,400);
select * from cuentas;
call add_bonification(2,400);
select * from cuentas;

delimiter //
create procedure call_cuentas()
begin
declare num_cuentas int;
declare i int;
select count(*) into num_cuentas from cuentas;
set i=1;
	while i <= num_cuentas do
    call add_bonification(i,400);
    set i= i+1;
	end while;
end //
delimiter ;

call call_cuentas();

select * from cuentas;
