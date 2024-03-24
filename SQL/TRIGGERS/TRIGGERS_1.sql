create database triggerDB;
use triggerDB;
create table cuentas(
cuentaid int not null unique auto_increment,
saldo decimal(10,2),
fecha timestamp default current_timestamp on update current_timestamp,
primary key (cuentaid)
);

insert into cuentas (saldo,fecha)
values (120.00,now()),(7200.00,now()),(800000.00,now());
select * from cuentas;

create table movimientos(
movimientoid int not null unique auto_increment,
cuentaid int not null,
saldo_anterior decimal(10,2),
saldo_actual decimal(10,2),
fecha_cambio timestamp default current_timestamp,
primary key(movimientoid),
foreign key(cuentaid) references cuentas(cuentaid)
);
select * from movimientos;


delimiter //
create trigger registrar_cambios
after update 
on cuentas
for each row
begin
	insert into movimientos
    (cuentaid,saldo_anterior,saldo_actual,fecha_cambio)
    values (old.cuentaid,old.saldo,new.saldo,now());
end //
delimiter ;


select * from movimientos;
update cuentas 
set saldo = 421.10
where cuentaid=1;
select * from cuentas;

select  * from movimientos;

create table empleados(
empleadoid int not null  unique auto_increment,
nombre varchar(255),
salario decimal(10,2),
primary key(empleadoid)
);

 insert into empleados(nombre,salario)
 values("Chio",1000),("Noemi",2000),("Anahi",3000);
 
 
 select * from empleados;
 
 delimiter //
 create trigger validar_nuevo_empleado
 before insert 
 on empleados
 for each row 
 begin
    declare salario_minimo decimal(10,2);
    set salario_minimo=400.00;
    if new.salario<salario_minimo then
	signal sqlstate "45000"
    set message_text="El salario del empleado no puede ser menor 400.00 MXN";
    end if;
 end //
 delimiter ;

insert into empleados(nombre,salario)
values("John",500.00);

select * from empleados;


Registro de cambios: Crea un trigger que registre cada cambio (inserción, actualización o eliminación) en una tabla específica en una tabla de registro de cambios. Utiliza un procedimiento almacenado para manejar la lógica de registro.

Auditoría de usuarios: Diseña un sistema de auditoría de usuarios que registre cuándo se inicia sesión un usuario en una tabla de auditoría. Utiliza un trigger para capturar el evento de inicio de sesión y un procedimiento almacenado para realizar el registro.

Control de stock: Implementa un sistema de control de stock que ajuste automáticamente la cantidad de productos en stock cuando se realizan compras o ventas. Utiliza un trigger que se active al realizar inserciones en una tabla de ventas y un procedimiento almacenado para actualizar el stock.

Validación de datos: Crea un trigger que valide ciertos datos antes de permitir una inserción o actualización en una tabla. Utiliza un procedimiento almacenado para realizar la validación y lanzar una señal de error si los datos no cumplen con ciertos criterios.

Generación de códigos: Diseña un sistema que genere automáticamente códigos únicos para nuevos registros en una tabla. Utiliza un procedimiento almacenado para generar el código y un trigger que se active antes de una inserción para asignar el código generado.

Histórico de precios: Implementa un historial de precios para productos en una tabla. Utiliza un trigger que se active cuando se actualiza el precio de un producto para registrar el precio anterior en una tabla de historial de precios.

Envío de notificaciones: Crea un sistema de notificaciones que envíe un correo electrónico o un mensaje cuando se cumplan ciertas condiciones en una tabla. Utiliza un trigger para monitorear los eventos y un procedimiento almacenado para enviar las notificaciones.

Control de acceso por roles: Diseña un sistema de control de acceso basado en roles (RBAC) que restrinja el acceso a ciertos recursos de la base de datos según el rol del usuario. Utiliza triggers y procedimientos almacenados para gestionar la autorización y autenticación de usuarios.


 
 
