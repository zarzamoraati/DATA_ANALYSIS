use triggerDB;

create table productos(
productoid int unique not null auto_increment,
nombre varchar(255) not null,
stock int not null,
primary key (productoid)
);
insert into productos(nombre,stock)
values ("Product A",100),("Product B",50),("Product C",75);

create table ventas(
ventaid int not null unique auto_increment,
productoid int not null,
cantidad int not null,
fecha_venta date,
primary key(ventaid),
foreign key (productoid) references productos(productoid)
);

delimiter //
create procedure update_stock(in id int , in amount int)
begin
declare current_stock int;
select stock into current_stock from productos where id=productoid;
if current_stock < amount then
	signal sqlstate "45000"
	set message_text="No hay suficiente stock para realizar la transaccion";
else 
	update productos
	set stock = current_stock - amount
	where id=productoid;
end if;
end //
delimiter ; 

delimiter //
create trigger trigger_update_stock after insert on ventas
for each row 
begin 
call update_stock(new.productoid,new.cantidad);
end //
delimiter ;

insert into ventas (ventaid,productoid,cantidad, fecha_venta)
values(102,1,99,"2023-09-13");
select  * from productos;


-- Registro de cambios: Crea un trigger que registre cada cambio (inserción, actualización o eliminación)
--  en una tabla específica en una tabla de registro de cambios.
--  Utiliza un procedimiento almacenado para manejar la lógica de registro.


-- Auditoría de usuarios: Diseña un sistema de auditoría de usuarios que registre cuándo se inicia sesión un usuario 
-- en una tabla de auditoría. Utiliza un trigger para capturar el evento de inicio de sesión y un procedimiento almacenado para realizar el registro.

-- Control de stock: Implementa un sistema de control de stock que ajuste automáticamente la cantidad de productos en stock 
-- cuando se realizan compras o ventas. Utiliza un trigger que se active al realizar inserciones en una tabla de ventas 
-- y un procedimiento almacenado para actualizar el stock.


-- Validación de datos: Crea un trigger que valide ciertos datos antes de permitir una inserción o actualización en una tabla.
-- Utiliza un procedimiento almacenado para realizar la validación y lanzar una señal de error si los datos no cumplen con ciertos criterios.

-- Generación de códigos: Diseña un sistema que genere automáticamente códigos únicos para nuevos registros en una tabla. Utiliza un procedimiento almacenado para generar el código y un trigger que se active antes de una inserción para asignar el código generado.

-- Histórico de precios: Implementa un historial de precios para productos en una tabla.
-- Utiliza un trigger que se active cuando se actualiza el precio de un producto
--  para registrar el precio anterior en una tabla de historial de precios.


-- Envío de notificaciones: Crea un sistema de notificaciones que envíe un correo electrónico o un mensaje cuando se cumplan ciertas condiciones en una tabla. Utiliza un trigger para monitorear los eventos y un procedimiento almacenado para enviar las notificaciones.

-- Control de acceso por roles: Diseña un sistema de control de acceso basado en roles (RBAC) que restrinja el acceso a ciertos recursos de la base de datos según el rol del usuario. Utiliza triggers y procedimientos almacenados para gestionar la autorización y autenticación de usuarios.


drop database temp;
create database temp;
use temp;



CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

CREATE TABLE historico_precios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT NOT NULL,
    precio_anterior DECIMAL(10, 2) NOT NULL,
    fecha_cambio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO productos (nombre, precio) VALUES
    ('Producto A', 50.00),
    ('Producto B', 30.00),
    ('Producto C', 75.00);

select * from productos;

delimiter //
create trigger updateHistory 
after update 
on productos
for each row 
begin
 -- despues del update en la tabla products queremos INSERTAR el valor original en la tabla historoial
 insert into historico_precios(producto_id,precio_anterior)
 values(old.id,old.precio);
end //
delimiter ;

delimiter //
create procedure updateCurrentPrice(in productId int,in newPrice decimal(10,2))
begin
declare product_exists int;
select count(*) into product_exists from productos where id=productId;
if product_exists > 0 then 
update productos
set precio=newPrice
where id=productId;
else
signal sqlstate "45000"
set message_text="Product no found";
end if;
end //
delimiter ;

drop procedure updateCurrentPrice;
drop trigger updateHistory;

select * from historico_precios;
select * from productos;

call updateCurrentPrice(4,100.00);
select * from historico_precios;




