create database subquerys;
use subquerys;

CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    Nombre VARCHAR(50)
);

CREATE TABLE Ordenes (
    OrdenID INT PRIMARY KEY,
    ClienteID INT,
    Total DECIMAL(10, 2),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

-- Instancias
INSERT INTO Clientes VALUES (1, 'Ana');
INSERT INTO Clientes VALUES (2, 'Juan');
INSERT INTO Clientes VALUES (3, 'Deldrima');
INSERT INTO Clientes VALUES (4, 'Chio');
INSERT INTO Clientes VALUES (5, 'Polo');

INSERT INTO Ordenes VALUES (101, 1, 150.00);
INSERT INTO Ordenes VALUES (102, 1, 200.00);
INSERT INTO Ordenes VALUES (103, 2, 100.00);
INSERT INTO Ordenes VALUES (104, 3, 900.00);
INSERT INTO Ordenes VALUES (105, 3, 1200.00);
INSERT INTO Ordenes VALUES (106, 3, 70000.00);


select * from clientes;
select * from ordenes;

 alter table ordenes
 add column fecha date;
select * from ordenes;
update ordenes
set fecha ='2023-08-15'
where ordenid=101;
update ordenes
set fecha='2021-08-15'
where ordenid=102;
update ordenes
set fecha='2022-02-15'
where ordenid=103;
update ordenes
set fecha='2023-08-22'
where ordenid=104;
update ordenes
set fecha='2023-05-15'
where ordenid=105;
update ordenes
set fecha='2023-07-15'
where ordenid=106;



CREATE TABLE Articulos (
    ArticuloID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Precio DECIMAL(10, 2)
);

CREATE TABLE Ventas (
    VentaID INT PRIMARY KEY,
    ArticuloID INT,
    Cantidad INT,
    FOREIGN KEY (ArticuloID) REFERENCES Articulos(ArticuloID)
);

-- Instancias
INSERT INTO Articulos VALUES (1, 'Camiseta', 20.00);
INSERT INTO Articulos VALUES (2, 'Pantalón', 40.00);
INSERT INTO Articulos VALUES (3, 'Reloj', 2400.00);
INSERT INTO Articulos VALUES (4, 'Zapatos', 800.00);

INSERT INTO Ventas VALUES (101, 1, 3);
INSERT INTO Ventas VALUES (102, 2, 2);
INSERT INTO Ventas VALUES (103, 1, 2);

CREATE TABLE Estudiantes (
    EstudianteID INT PRIMARY KEY,
    Nombre VARCHAR(50)
);

CREATE TABLE Asignaturas (
    AsignaturaID INT PRIMARY KEY,
    Nombre VARCHAR(50)
);

CREATE TABLE Matriculas (
    MatriculaID INT PRIMARY KEY,
    EstudianteID INT,
    AsignaturaID INT,
    FOREIGN KEY (EstudianteID) REFERENCES Estudiantes(EstudianteID),
    FOREIGN KEY (AsignaturaID) REFERENCES Asignaturas(AsignaturaID)
);

-- Instancias
INSERT INTO Estudiantes VALUES (1, 'María');
INSERT INTO Estudiantes VALUES (2, 'Pedro');
INSERT INTO Estudiantes VALUES (3, 'Chio');
INSERT INTO Estudiantes VALUES (4, 'Nidia');
INSERT INTO Estudiantes VALUES (5, 'Noemi');
INSERT INTO Estudiantes VALUES (6, 'Fernalga');

INSERT INTO Asignaturas VALUES (101, 'Matemáticas');
INSERT INTO Asignaturas VALUES (102, 'Historia');
INSERT INTO Asignaturas VALUES (103, 'Biologia');
INSERT INTO Asignaturas VALUES (104, 'Fisica');
INSERT INTO Matriculas VALUES (201, 1, 101);
INSERT INTO Matriculas VALUES (202, 1, 102);
INSERT INTO Matriculas VALUES (203, 2, 101);
INSERT INTO Matriculas VALUES (204, 4, 103);
INSERT INTO Matriculas VALUES (205, 4, 102);
INSERT INTO Matriculas VALUES (207, 6, 101);
INSERT INTO Matriculas VALUES (208, 6, 102);
INSERT INTO Matriculas VALUES (209, 6, 103);
INSERT INTO Matriculas VALUES (210, 6, 104);
delete from matriculas where matriculaid=206;
select * from matriculas;
describe clientes;
describe ordenes;


describe estudiantes;
describe asignaturas;
describe matriculas;

describe ventas;
describe articulos;


-- Clientes y Órdenes - Total Mínimo:
-- Encuentra los nombres de los clientes que tienen al menos una orden con un total mínimo de $200.s
select nombre from clientes where clienteid in (select clienteid from ordenes where total > 200);
select * from ordenes order by total desc;

-- Artículos y Ventas - Venta Máxima:
-- Encuentra el nombre y el precio del artículo que ha tenido la venta más alta.
    select nombre from articulos where articuloid in 
    (select articuloid from ventas where precio*cantidad = 
    (select max(precio*cantidad) from ventas))

-- Estudiantes y Asignaturas - Matrículas Comunes:

-- Encuentra los nombres de las asignaturas que tienen matriculados 
-- los mismos estudiantes que la asignatura de Historia.

select * from asignaturas;
select * from matriculas;
select nombre from asignaturas where asignaturaid in (select asignaturaid from matriculas where estudianteid 
in (select estudianteid from matriculas where asignaturaid=102) and asignaturaid!=102);

-- Clientes y Órdenes - Órdenes Múltiples:
-- Encuentra los nombres de los clientes que tienen más de una orden
describe clientes;
describe ordenes;
select nombre from clientes c where (select count(clienteid) from ordenes o where c.clienteid=o.clienteid)>1;

-- Artículos y Ventas - Ventas Duplicadas:
-- Encuentra los nombres de los artículos que han sido vendidos más de una vez.
describe articulos;
describe ventas;
select nombre from articulos a where (select count(articuloid) from ventas v where a.articuloid=v.articuloid)>1;

-- Estudiantes y Asignaturas - Asignaturas Exclusivas:
-- Encuentra los nombres de las asignaturas en los que esta matriculado la estudiante  María.
describe estudiantes;
describe asignaturas;
describe matriculas;
select nombre from asignaturas where asignaturaid
in (select asignaturaid from matriculas where estudianteid in (select estudianteid from estudiantes where nombre like "mari%"));
select e.nombre,a.nombre from estudiantes e join asignaturas a join matriculas m 
on e.estudianteid=m.estudianteid and a.asignaturaid=m.asignaturaid
where e.nombre like "maria%";

SELECT *
FROM Estudiantes e
JOIN Matriculas m ON e.EstudianteID = m.EstudianteID
JOIN Asignaturas a ON a.AsignaturaID = m.AsignaturaID;

-- Clientes y Órdenes - Órdenes en un Rango:
-- Encuentra los nombres de los clientes que han realizado órdenes con un total entre $100 y $300
describe clientes;
describe ordenes;

select nombre from clientes where clienteid in (select clienteid from ordenes where total between 100 and 300 );
-- Artículos y Ventas - Artículos No Vendidos:
-- Encuentra los nombres de los artículos que no han sido vendidos.
describe articulos;
describe ventas;
select * from articulos;
select * from ventas;

select nombre from articulos a where a.articuloid not in (select v.articuloid from ventas v where a.articuloid=v.articuloid);

-- Estudiantes y Asignaturas - Matrículas en Todas las Asignaturas:
-- Encuentra los nombres de los estudiantes que están matriculados en todas las asignaturas

select nombre from estudiantes e
join matriculas m on e.estudianteid=m.estudianteid
group by e.estudianteid
having count(e.estudianteid) =
(select count(nombre) from asignaturas);

SELECT e.Nombre
FROM Estudiantes e
WHERE NOT EXISTS (
    -- Encuentra un estudiante que NO esté matriculado en TODAS las asignaturas
    -- Devuelve NADA a la nueva tabla para cada coincidencia.
    -- Si NO LO ENCUENTRA, significa que el estudiante DEBE ESTAR MATRICULADO EN TODAS LAS ASIGNATURAS
    
    SELECT 1 -- SELECCIONA LOS 1 DEVUELTO POR LA SUBCONSULTA QUE REPRESENTAN LOS REGISTROS DE LOS ESTUDIANTES MATRICULADOS EN TODAS LAS MATERIAS
    -- toma nota de como los 1 no se filtran de la SUBCONSULTA
    FROM Asignaturas a
    WHERE NOT EXISTS (
        -- Encuentra una asignatura para la cual el estudiante NO esté matriculado
        -- y DEVUELVE NADA.
        -- Si NO EXISTE UNA ASIGNATURA para la cual el estudiante ACTUAL NO ESTÉ MATRICULADO,
        -- eso SIGNIFICA QUE EL ESTUDIANTE ESTÁ MATRICULADO EN TODAS LAS ASIGNATURAS
        -- y se DEVUELVE 1.
        
        -- Subconsulta anidada
        SELECT 1
        FROM Matriculas m
        WHERE m.EstudianteID = e.EstudianteID AND m.AsignaturaID = a.AsignaturaID
    )
);

-- Clientes y Órdenes - Clientes Nuevos:
-- Encuentra los nombres de los clientes que realizaron su primera orden en el último mes.	
select nombre from clientes c where clienteid in 
(select o.clienteid from ordenes o where date(o.fecha)=
(select min(fecha) from ordenes where clienteid=o.clienteid) and o.fecha < date_sub(now(),interval 1 month));


-- Ejercicios de Subconsultas Relacionadas:

-- Clientes y Órdenes - Total Promedio:
-- Encuentra los nombres de los clientes y el promedio de los totales de sus órdenes.
	describe clientes;
    describe ordenes;
    select nombre, (select avg(o.total) from ordenes o where o.clienteid=c.clienteid ) 
    as total_avg from clientes c;
    
-- Artículos y Ventas - Total Ventas por Artículo:
-- Encuentra el nombre de los artículos y el total de ventas de cada uno.
	describe articulos;
    describe ventas;
    select nombre, (select sum(v.cantidad*a.precio) from ventas v where a.articuloid = v.articuloid)
    as total_sales from articulos a;
    
-- Estudiantes y Asignaturas - Estudiantes sin Matrícula:
	
-- Encuentra los nombres de los estudiantes que no están matriculados en ninguna asignatura.
	describe estudiantes;
    describe asignaturas ;
    describe matriculas;
    select nombre from estudiantes e where estudianteid not in
    (select estudianteid from matriculas m where e.estudianteid=m.estudianteid);
    
-- Clientes y Órdenes - Órdenes por Cliente:
-- Encuentra los nombres de los clientes y la cantidad de órdenes que han realizado.
describe clientes;
describe ordenes;
select c.nombre, (select count(o.clienteid) from ordenes o where c.clienteid=o.clienteid ) as total_pedidos from clientes c;

-- Artículos y Ventas - Artículos por Cantidad Vendida:
-- Encuentra el nombre de los artículos y la cantidad total vendida de cada uno.
describe articulos;
describe ventas;
select a.nombre, (select count(v.articuloid) from ventas v where v.articuloid=a.articuloid)  as total_sale from articulos a;

-- Estudiantes y Asignaturas - Estudiantes en Asignaturas de Mayor Número:
-- Encuentra los nombres de los estudiantes que están matriculados en las asignaturas que tienen el mayor número de matrículas.
select distinct e.nombre from estudiantes e join matriculas m on e.estudianteid=m.estudianteid where m.asignaturaid in
(select asignaturaid from matriculas group by asignaturaid  having count(*)=
(select max(total) from (select count(asignaturaid) as total from matriculas group by asignaturaid) as conteo)) ;

-- Clientes y Órdenes - Órdenes Superiores al Promedio:
-- Encuentra los nombres de los clientes y las órdenes cuyos totales son superiores al promedio 
-- de los totales de todas las órdenes.
describe clientes;
describe ordenes;

select c.nombre, o.ordenid,o.total from clientes c join ordenes o on c.clienteid=o.clienteid
where o.total > (select avg(total) from ordenes);

-- Artículos y Ventas - Ventas por Rango de Precio:
-- Encuentra el nombre de los artículos y el total de ventas de cada uno en un rango de precio específico.

describe ventas;
describe articulos;
select a.nombre,sum(a.precio*v.cantidad) as  total from articulos a join ventas v on a.articuloid=v.articuloid
group by a.articuloid having total between 90 and 400; 

-- Estudiantes y Asignaturas - Asignaturas en las que Está Matriculado Más de un Estudiante:
-- Encuentra los nombres de las asignaturas que tienen matriculados más de un estudiante.
describe asignaturas;
select * from matriculas;

select a.nombre from asignaturas a where (select count(m.asignaturaid) from matriculas m where m.asignaturaid=a.asignaturaid) > 1
 ;
