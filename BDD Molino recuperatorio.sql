CREATE TABLE Operario (
    dni INT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT
);


CREATE TABLE Material (
    id_material INT PRIMARY KEY,
    tipo VARCHAR(50),
    cantidad INT
);

USE molinoindustrial;

INSERT INTO Operario (dni, nombre, edad) VALUES
(1001, 'Juan García', 35),
(1002, 'María Rodríguez', 28),
(1003, 'Pedro López', 42),
(1004, 'Ana Martínez', 30),
(1005, 'Luis Gómez', 25),
(1006, 'Enzo Gonzalez',24 ),
(1200, 'Javier Batistela', 31),
(1122, 'Gabriel Bulacio', 29),
(1009, 'Juan Pablo Gomez', 20),
(1010, 'Lionel Messi', 37);

INSERT INTO Material (id_material, tipo, cantidad) VALUES
(101, 'Trigo', 1000),
(102, 'Maíz', 500),
(103, 'Cebada', 100),
(104, 'Avena', 900),
(105, 'Centeno', 100),
(106, 'Lenteja', 900),
(107, 'Azucar', 2000),
(108, 'Comino', 800),
(109, 'Cilantro', 1500),
(110, 'Pimienta', 900);

SELECT * FROM Operario;

SELECT tipo, cantidad FROM Material;

SELECT nombre, edad FROM Operario WHERE edad > 30;

SELECT * FROM Material WHERE tipo LIKE 'C%';

SELECT * FROM Material ORDER BY cantidad DESC LIMIT 3;