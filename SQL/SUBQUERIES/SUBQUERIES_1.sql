create database subconsultas;
use subconsultas;

CREATE TABLE departamentos (
    id_departamento INT PRIMARY KEY,
    nombre_departamento VARCHAR(50)
);

CREATE TABLE empleados (
    id_empleado INT PRIMARY KEY,
    nombre_empleado VARCHAR(50),
    salario DECIMAL(10, 2),
    id_departamento INT
);

-- Departamentos
INSERT INTO departamentos (id_departamento, nombre_departamento) VALUES
(1, 'Ventas'),
(2, 'Finanzas'),
(3, 'Recursos Humanos');

-- Empleados
INSERT INTO empleados (id_empleado, nombre_empleado, salario, id_departamento) VALUES
(1, 'Juan Pérez', 5000, 1),
(2, 'María González', 6000, 2),
(3, 'Carlos Rodríguez', 5500, 1),
(4, 'Ana Martínez', 5200, 3),
(5, 'Luisa García', 4800, 1);

select * from departamentos;
select * from empleados;

-- Tareas para Subconsultas:

-- Obtener el nombre de los empleados que ganan más que el salario promedio de su departamento.
-- Encontrar los departamentos que tienen más de 2 empleados.
 -- Encontrar los nombres de los empleados que trabajan en el departamento con el nombre "Ventas".
-- 1
select nombre_empleado from empleados where salario > (select avg(salario) from empleados);
-- 2
select nombre_departamento from departamentos where id_departamento in 
(select id_departamento from empleados group by id_departamento having count(id_departamento)>2);
-- 3
select nombre_empleado from empleados where id_departamento 
in(select id_departamento from departamentos where nombre_departamento like "ven%");



-- Esquema 2: Pedidos y Productos

CREATE TABLE productos (
    id_producto INT PRIMARY KEY,
    nombre_producto VARCHAR(50),
    precio DECIMAL(10, 2)
);

CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY,
    fecha_pedido DATE,
    id_producto INT
);

-- Productos
INSERT INTO productos (id_producto, nombre_producto, precio) VALUES
(1, 'Laptop', 800),
(2, 'Teléfono', 400),
(3, 'Tablet', 300),
(4, 'Impresora', 200);

-- Pedidos
INSERT INTO pedidos (id_pedido, fecha_pedido, id_producto) VALUES
(1, '2023-08-01', 1),
(2, '2023-08-02', 2),
(3, '2023-08-02', 1),
(4, '2023-08-03', 3),
(5, '2023-08-03', 2);


-- Tareas para Subconsultas Relacionadas:

-- Obtener los nombres de los productos que se han pedido más de una vez.
select nombre_producto from productos p where (select count(id_producto) from pedidos pe where pe.id_producto=p.id_producto)>1;
-- Encontrar las fechas en las que se realizaron pedidos de productos 
-- con un precio superior al promedio de precios de todos los productos.
select fecha_pedido from pedidos where id_producto 
in(select id_producto from productos where precio > (select avg(precio) from productos));
-- Encontrar los nombres de los productos que se han pedido en el mismo día que el producto con ID 3.
select nombre_producto from productos where id_producto in
(select id_producto from pedidos where id_producto != 3 and fecha_pedido 
in (select fecha_pedido from pedidos where id_producto=3))



-- Esquema 3: Estudiantes y Notas


CREATE TABLE estudiantes (
    id_estudiante INT PRIMARY KEY,
    nombre_estudiante VARCHAR(50)
);

CREATE TABLE notas (
    id_nota INT PRIMARY KEY,
    id_estudiante INT,
    materia VARCHAR(50),
    calificacion DECIMAL(5, 2)
);

-- Estudiantes
INSERT INTO estudiantes (id_estudiante, nombre_estudiante) VALUES
(1, 'Ana'),
(2, 'Juan'),
(3, 'María'),
(4, 'Carlos'),
(5, 'Luisa');

-- Notas
INSERT INTO notas (id_nota, id_estudiante, materia, calificacion) VALUES
(1, 1, 'Matemáticas', 9.5),
(2, 1, 'Historia', 7.8),
(3, 2, 'Matemáticas', 8.2),
(4, 2, 'Historia', 6.5),
(5, 3, 'Matemáticas', 7.0),
(6, 3, 'Historia', 8.7),
(7, 4, 'Matemáticas', 9.0),
(8, 4, 'Historia', 9.8),
(9, 5, 'Matemáticas', 8.5),
(10, 5, 'Historia', 7.2);



-- Tareas para Subconsultas y Subconsultas Relacionadas:

-- Obtener los nombres de los estudiantes que tienen una calificación mayor a 9 en al menos una materia.
	select nombre_estudiante from estudiantes where id_estudiante in
    (select id_estudiante from notas where calificacion>9);
-- Encontrar las materias en las que los estudiantes obtuvieron una calificación promedio mayor a 8.
	select distinct materia from notas where materia in (select materia from notas group by materia having avg(calificacion)>8);
-- Obtener los nombres de los estudiantes que tienen una calificación mayor a 9 
-- en una materia que también tiene un estudiante llamado "Ana".

SELECT DISTINCT e.nombre_estudiante
FROM estudiantes e
WHERE e.nombre_estudiante != 'Ana' AND e.id_estudiante IN (
    SELECT DISTINCT n1.id_estudiante
    FROM notas n1
    WHERE n1.calificacion > 9 AND n1.materia IN (
        SELECT DISTINCT n2.materia
        FROM notas n2
        WHERE n2.id_estudiante = 1
    )
);

    -- Obtener los nombres de los estudiantes que tienen una calificación mayor 
	-- a una materia que también tiene un estudiante llamado "Ana".
    
