create database procedure3;
use procedure3;

CREATE TABLE cuentas(
cuentaid INT UNSIGNED NOT NULL,
saldo DECIMAL(7,2) NOT NULL,
PRIMARY KEY(cuentaid)
);
INSERT INTO cuentas VALUES (1, 1000);
INSERT INTO cuentas VALUES (2, 2000);
INSERT INTO cuentas VALUES (3, 3000);

select * from cuentas;
-- Simple procedure
delimiter //
create procedure p()
begin 
select * from cuentas;
end //
delimiter ;

call p();

-- paso de parametros de entrada
delimiter //
create procedure fecha(in dia varchar(50),in fecha date)
begin
select dia as dia_del_mes,fecha as fecha_actual;
end //
delimiter ;
call fecha("viernes", "2023-09-01");

-- paso de parametros con modificacion de tabla
delimiter //
create procedure retirar_saldo(in id int ,in monto decimal(7,2))
begin
update cuentas
set saldo=saldo-monto
where id=cuentaid;
select cuentaid,saldo from cuentas where id=cuentaid;
end //
delimiter ;
call retirar_saldo(1,300.00);

--  parametros de retorno

delimiter //
create procedure check_disccount
(in monto decimal(10,2),out descuento decimal(10,2))
begin
if monto <= 100 then
set descuento=monto-monto*0.10;
elseif monto >100 then
set descuento=monto-monto*0.20;
end if;
end; //
delimiter ;
call check_disccount(100,@a);
select @a as precio_con_descuento;


SELECT * from cuentas;

delimiter //
create procedure bonificacion(in id int,out bono decimal (10,2))
begin
declare saldo_cuenta decimal(10,2);
select saldo into saldo_cuenta from cuentas where cuentaid=id;
if saldo_cuenta>1000.00 then 
set bono=saldo_cuenta*0.10; -- aplicar bonificacion de 10%
elseif saldo_cuenta<1000.00 then
set bono=0; -- sin bonificacion
end if;
end //
delimiter ;
call bonificacion(3,@c);
select @c as monto_de_bonificacion; -- monto de bonificacion para la cuenta tres
drop procedure bonificacion;


