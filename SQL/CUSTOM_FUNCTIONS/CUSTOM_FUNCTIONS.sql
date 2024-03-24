create database userFunctions1;
use userFunctions1;
SET GLOBAL log_bin_trust_function_creators = 1;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2)
);

INSERT INTO Customers (CustomerID, CustomerName) VALUES
(1, 'Cliente A'),
(2, 'Cliente B');

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(101, 1, '2023-01-10', 500.00),
(102, 1, '2023-01-15', 300.00),
(103, 2, '2023-02-20', 750.00);

delimiter //
create function getTotalByClient(idClient int)
returns decimal(10,2)
begin
	declare total decimal(10,2);
    select sum(totalamount) into total from orders where idClient=customerid;
    return total;
end //
delimiter ;
drop function if exists getTotalByClient;

select getTotalByClient(1);


drop database if exists temp; 
create database temp; 
use temp ;

-- Crea una función escalar llamada CalcularTotalVentasPorCliente que tome un CustomerID 
-- como entrada y devuelva el total de ventas para ese cliente.

delimiter //
create function getTotal(customerId int)
returns decimal(10,2)
begin 
    declare total decimal(10,2);
    select sum(o.totalamount) into total from Orders o
    join Customers c on o.customerid = c.customerid
    where c.customerid = customerId;
    return total;
end //
delimiter ;
select getTotal(1) ;

-- Ejercicio 2: Obtener el Nombre Completo de un Empleado

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255)
);
INSERT INTO Employees (EmployeeID, FirstName, LastName) VALUES
(1, 'John', 'Doe'),
(2, 'Jane', 'Smith'),
(3, 'Alice', 'Johnson');


select * from employees;

delimiter // 
create function getFullName(id int)
returns varchar(255)
begin
	declare full_name varchar(255);
	select concat_ws(" ",firstname,lastname) into full_name from employees where employeeid=id;
	if full_name is null then 
    signal sqlstate "45000"
    set message_text = "empleado id not foun";
	else 
    return full_name;
	end if;
end //
delimiter ;
drop function getFullName;

select getFullName(3) ;


-- Crea una función escalar llamada ObtenerNombreCompletoEmpleado que tome un EmployeeID 
-- como entrada y devuelva el nombre completo del empleado en el formato "Nombre Apellido".

delimiter //
create function getFullName(empleadoid varchar(255))
returns varchar(255)
begin
    declare full_name varchar(255);
    select CONCAT_WS(' ', firstname, lastname) into full_name from employees where employeeid=empleadoid;
    return full_name;
end
delimiter ;

select getFullName(2);

delimiter //
create function get_name_full(empleadoid varchar(255))
returns varchar(255)
begin
    declare full_name varchar(255);
    select concat(firstname," ",lastname) into full_name from employees where employeeid=empleadoid;
    return full_name;
end //
delimiter ;
select get_name_full(3);

-- Ejercicio 3: Calcular el Precio Total de Productos en un Pedido


CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2)
);

CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY,
    ProductID INT,
    Quantity INT
);


INSERT INTO Products (ProductID, ProductName, Price) VALUES
(1, 'Producto A', 10.00),
(2, 'Producto B', 15.00),
(3, 'Producto C', 5.00);

INSERT INTO OrderItems (OrderItemID, ProductID, Quantity) VALUES
(101, 1, 3),
(102, 2, 2),
(103, 3, 4);

INSERT INTO OrderItems (OrderItemID, ProductID, Quantity) VALUES (104,1,2);

-- Crea una función escalar llamada CalcularPrecioTotalPedido 
-- que tome un OrderItemID como entrada y devuelva el precio total de los productos en ese pedido.

delimiter //
create function salesTotal(id int)
returns decimal(10,2)
begin
declare acum_total decimal(10,2);
select	sum(o.quantity * p.price) into acum_total from orderitems o 
join products p on o.productid=p.productid
where o.productid=id;
return acum_total;
end //
delimiter ;

-- 50 
select salesTotal(1);


-- INTERMEDIO Ejercicio 1: Obtener la Edad Promedio
-- Supongamos que tienes una tabla llamada usuarios con columnas nombre y fecha_nacimiento
 -- (en formato de fecha). El ejercicio consiste en crear una función escalar llamada 
 -- calcularEdadPromedio que calcule la edad promedio de todos los usuarios en la tabla usuarios. 
 -- Luego, utiliza esta función en una consulta para obtener la edad promedio.


CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    fecha_nacimiento DATE 
);

-- Instancias de datos
INSERT INTO usuarios (nombre, fecha_nacimiento) VALUES
    ('Usuario 1', '1990-01-15'),
    ('Usuario 2', '1985-05-20'),
    ('Usuario 3', '1992-08-10');

select * from usuarios;

delimiter //
create function get_current_age( year_born date)
returns int
begin 
declare current_age int ;
set current_age=timestampdiff(year,year_born, now());
return current_age;
end //
delimiter ;

select nombre , get_current_age(fecha_nacimiento) as current_age from usuarios;

select avg(get_current_age(fecha_nacimiento)) as avg_age from usuarios;
    



delimiter //
create function getAvgAge(born_date date)
returns decimal(5,2)
begin
	declare current_age decimal(5,2);
	set current_age=timestampdiff(year,born_date,now());
    return current_age;
end //
delimiter ;
drop function getAvgAge;

select getAvgAge();

DELIMITER //

CREATE FUNCTION CalcularEdad(fecha_nacimiento DATE) RETURNS INT
BEGIN
  DECLARE edad INT;
  SET edad = TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE());
  RETURN edad;
END //

DELIMITER ;
SELECT avg(CalcularEdad(fecha_nacimiento)) AS edad
FROM usuarios;


-- Ejercicio 2: Formatear Nombres Completos

-- Tienes una tabla llamada empleados con columnas nombre y apellido. 
-- El objetivo es crear una función escalar llamada formatearNombreCompleto que tome 
-- el nombre y apellido como entrada y devuelva el nombre completo en formato "Apellido, Nombre".
-- Luego, aplica esta función en una consulta para obtener el nombre completo formateado de todos los empleados.
-- Esquema de la tabla 'empleados'


CREATE TABLE empleados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

-- Instancias de datos
INSERT INTO empleados (nombre, apellido) VALUES
    ('John', 'Doe'),
    ('Jane', 'Smith'),
    ('Alice', 'Johnson');
select * from empleados;

delimiter //
create function getFullName2(f_name varchar(50),surname varchar(50))
returns varchar(255)
	begin
    	declare full_name varchar(255);
		set full_name = concat_ws(" ",f_name,surname);
        return full_name;
    end //
delimiter ;
select nombre,apellido,getFullName2(nombre,apellido) as full_name from empleados;


-- INTERMEDIO Ejercicio 3: Calcular Precio Total del Carrito de Compras
-- Esquema de la tabla 'productos'
CREATE TABLE car_products (
    producto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_producto VARCHAR(100),
    precio DECIMAL(10, 2)
);

-- Esquema de la tabla 'carrito_compras'
CREATE TABLE carrito_compras (
    carrito_id INT PRIMARY KEY AUTO_INCREMENT,
    producto_id INT,
    cantidad INT
);

-- Instancias de datos
INSERT INTO car_products (nombre_producto, precio) VALUES
    ('Producto A', 10.00),
    ('Producto B', 15.00),
    ('Producto C', 5.00);

INSERT INTO carrito_compras (producto_id, cantidad) VALUES
    (1, 3),
    (2, 2),
    (3, 4);

delimiter //    
create function getTotals()
returns decimal(10,2)
begin
declare total_value decimal(10,2);
select sum(cp.precio*cc.cantidad) into total_value 
from carrito_compras cc left join car_products cp on 
cc.producto_id = cp.producto_id ;
return total_value ;
end //
delimiter ;

create database temp;
use temp;
select * from car_products;
select * from carrito_compras;


select getTotals();




    
    -- Supongamos que tienes dos tablas: productos con columnas 
-- producto_id y precio, y carrito_compras con columnas producto_id y cantidad.
 -- El ejercicio consiste en crear una función escalar llamada calcularPrecioTotal 
 -- que tome un producto_id como entrada y devuelva el precio total de ese producto 
 -- en el carrito de compras (precio * cantidad). Luego, aplica esta función en una consulta para 
--  obtener el precio total de todos los productos en el carrito de compras.

create view get_amount as 
select	c.producto_id , c.cantidad , p.precio from carrito_compras c join car_products p on
 p.producto_id=c.producto_id;
 
 select * from get_amount;

delimiter //
create function get_total_price(productId int)
returns decimal(10,2)
begin
	declare total_value decimal(10,2);
	select (precio * cantidad ) into total_value from get_amount where producto_id=productId;
    return total_value;
end // 
delimiter ;
drop function get_total_price;

select carrito_id,cantidad,get_total_price(producto_id) as total_value from carrito_compras;


-- obtener las edades de cada usuario y el promedio total 

CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    fecha_nacimiento DATE 
);

-- Instancias de datos
INSERT INTO usuarios (nombre, fecha_nacimiento) VALUES
    ('Usuario 1', '1990-01-15'),
    ('Usuario 2', '1985-05-20'),
    ('Usuario 3', '1992-08-10');

select * from usuarios;

delimiter //
create function get_current_age( year_born date)
returns int
begin 
declare current_age int ;
set current_age=timestampdiff(year,year_born, now());
return current_age;
end //
delimiter ;

select nombre , get_current_age(fecha_nacimiento) as current_age from usuarios;

select avg(get_current_age(fecha_nacimiento)) as avg_age from usuarios;
    


-- obtener el acumulado total de un carrito de compras

-- Instancias de datos
INSERT INTO car_products (nombre_producto, precio) VALUES
    ('Producto A', 10.00),
    ('Producto B', 15.00),
    ('Producto C', 5.00);

INSERT INTO carrito_compras (producto_id, cantidad) VALUES
    (1, 3),
    (2, 2),
    (3, 4);

delimiter //    
create function getTotals()
returns decimal(10,2)
begin
declare total_value decimal(10,2);
select sum(cp.precio*cc.cantidad) into total_value 
from carrito_compras cc left join car_products cp on 
cc.producto_id = cp.producto_id ;
return total_value ;
end //
delimiter ;

create database temp;
use temp;
select * from car_products;
select * from carrito_compras;


select getTotals();

c

