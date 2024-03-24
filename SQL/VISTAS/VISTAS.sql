
drop database temp;
create database temp;
use temp;


CREATE TABLE Pelicula (
    mID INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    anio INT,
    director VARCHAR(255)
);

-- Instancias de películas
INSERT INTO Pelicula (titulo, anio, director) VALUES
    ('Pelicula 1', 2020, 'Director 1'),
    ('Pelicula 2', 2019, 'Director 2'),
    ('Pelicula 3', 2021, 'Director 1');
    
    
CREATE TABLE Revisor (
    rID INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL
);

-- Instancias de revisores
INSERT INTO Revisor (nombre) VALUES
    ('Revisor 1'),
    ('Revisor 2'),
    ('Revisor 3');

CREATE TABLE Calificacion (
    rID INT,
    mID INT,
    estrellas INT CHECK (estrellas BETWEEN 1 AND 5),
    fecha_calificacion DATE,
    FOREIGN KEY (rID) REFERENCES Revisor (rID),
    FOREIGN KEY (mID) REFERENCES Pelicula (mID)
);

-- Instancias de calificaciones
INSERT INTO Calificacion (rID, mID, estrellas, fecha_calificacion) VALUES
    (1, 1, 4, '2022-01-15'),
    (2, 1, 3, '2022-02-20'),
    (3, 2, 5, '2022-03-10'),
    (1, 3, 4, '2022-04-05');


-- 1.  Cree una vista llamada TNS que contenga tripletas título-nombre-estrellas, 
-- donde la película (título) fue revisada por un revisor (nombre) y recibió la calificación (estrellas). 
-- Luego, haciendo referencia solo a la vista TNS y la tabla Pelicula ,
--  escriba una consulta  que devuelva el último año de cualquier película revisada por el revisor 1.
--  Puede suponer que los nombres de las películas son únicos.

create view TNS as
select p.titulo,r.nombre,c.estrellas from 
pelicula p inner join calificacion c on 
p.mID=c.mID 
inner join revisor r on
c.rID = r.rID;

select * from TNS;

select max(p.anio) as ultimo_anio 
from pelicula p inner join tns v 
on p.titulo = v.titulo
where v.nombre like "%revisor 1%";


-- 2.  Vista de referencia TNSA partir del Ejercicio 1 y ninguna otra tabla, 
-- cree una vista RatingStats que contenga cada título de película que tenga al menos una calificación,
--  la cantidad de calificaciones que recibió y su calificación promedio. Luego,
--  haciendo referencia a la vista RatingStats y no a otras tablas, 
-- escriba una consulta SQL para encontrar el título de la película con la calificación 
-- promedio más alta con al menos tres calificaciones.


create view RatingStates as
select p.titulo,count(c.estrellas) review_num,avg(c.estrellas) as avg_rating
from pelicula p inner join calificacion c on c.mid=p.mid
where c.estrellas is not null 
group by c.mid;
drop view ratingstates;

SELECT titulo, max(avg_rating) 
FROM RatingStates 
WHERE review_num > 1
GROUP BY titulo
HAVING max(avg_rating) = (SELECT max(avg_rating) 
                          FROM RatingStates 
                          WHERE review_num > 1);



-- 3.  Cree una vista Favoritos que contenga pares rID-mID, donde el crítico con rID le dio a la película 
-- con mID la calificación más alta que le dio a cualquier película. Luego, 
-- haciendo referencia solo a la vista Favoritos y las tablas Película y Crítico , 
-- escriba una consulta SQL para devolver tripletas crítico-crítico-película 
-- donde los dos críticos (diferentes) tienen la película como su favorita.
--  Devuelve cada par una vez, es decir, no devuelves un par y su inverso.





