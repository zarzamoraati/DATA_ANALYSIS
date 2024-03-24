create database transacciones;
use transacciones;

CREATE TABLE cuentas (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    saldo DECIMAL(10, 2)
);

CREATE TABLE transacciones (
    id INT PRIMARY KEY,
    cuenta_origen INT,
    cuenta_destino INT,
    monto DECIMAL(10, 2),
    fecha TIMESTAMP
);

INSERT INTO cuentas (id, nombre, saldo) VALUES
(1, 'Cuenta A', 1000.00),
(2, 'Cuenta B', 500.00);

drop table cuentas;

DELIMITER //

CREATE PROCEDURE realizar_transferencia()
BEGIN
    DECLARE saldo_origen DECIMAL(10, 2);
    DECLARE saldo_destino DECIMAL(10, 2);
    DECLARE monto_transferir DECIMAL(10, 2);
    
    START TRANSACTION;

    -- Obtener los saldos actuales de las cuentas
    SELECT saldo INTO saldo_origen FROM cuentas WHERE id = 1;
    SELECT saldo INTO saldo_destino FROM cuentas WHERE id = 2;

    -- Realizar la transferencia
    SET monto_transferir = 300.00;
    UPDATE cuentas SET saldo = saldo - monto_transferir WHERE id = 1;
    UPDATE cuentas SET saldo = saldo + monto_transferir WHERE id = 2;

    -- Registrar la transacción
    INSERT INTO transacciones (id,cuenta_origen, cuenta_destino, monto, fecha)
    VALUES (1,1, 2, monto_transferir, NOW());

    -- Comprobar si hay suficiente saldo en la cuenta origen
    IF saldo_origen >= monto_transferir THEN
        COMMIT; -- Confirmar la transacción
    ELSE
        ROLLBACK; -- Revertir la transacción
    END IF;
END //

DELIMITER ;

-- Llamar al procedimiento almacenado para ejecutar la transferencia
CALL realizar_transferencia();

select * from cuentas;
select * from transacciones;

drop procedure if exists realizar_transferencia;

-- Transferencia de fondos:
-- Crea una tabla de cuentas bancarias y permite a los usuarios realizar transferencias entre cuentas.
-- Asegúrate de que la transferencia sea una transacción atómica para evitar problemas de inconsistencia.

-- Reservas de asientos:
-- Implementa un sistema de reservas para un teatro o una aerolínea. 
-- Los usuarios deben poder seleccionar asientos y confirmar la reserva.
--  Utiliza transacciones para asegurarte de que los asientos no se reserven dos veces al mismo tiempo.
CREATE TABLE asientos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero_asiento INT,
    fila CHAR(1),
    ocupado BOOLEAN DEFAULT FALSE
);

-- Crear la tabla de reservas
CREATE TABLE reservas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    -- usuario_id INT, -- Aquí puedes vincularlo a una tabla de usuarios si es necesario
    asiento_id INT,
	selection_fila char(1),
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (asiento_id) REFERENCES asientos(id)
);
drop table reservas;

drop database temp;
create database temp;
use temp;

-- Insertar algunos datos de ejemplo en la tabla de asientos
INSERT INTO asientos (numero_asiento, fila, ocupado) VALUES
    (1, 'A', FALSE),
    (2, 'A', FALSE),
    (3, 'A', FALSE),
    (1, 'B', FALSE),
    (2, 'B', FALSE),
    (3, 'B', FALSE);
select * from asientos;
drop table if exists asientos;
drop table if exists reservas;


 -- si un usuario realiza una reserva modifica el estado de la tabla (create procedure,trigger)
 -- si un usuario inetenta revervar el mismo asiento en la misma fila , cancelar transaccion 
 delimiter //
 create trigger crear_reserva 
 after update 
 on asientos
 for each row 
 begin
 insert into reservas(asiento_id,selection_fila) 
 values(old.id,old.fila);
 end //
 delimiter ;
 
 delimiter //
 create procedure realizar_reservacion( in fila char(1), in asiento int)
 begin 
	declare v_asientoid int;
	declare v_ocupado boolean;
	start transaction;
	
    select a.id , a.ocupado into v_asientoid,v_ocupado from asientos a
    where a.numero_asiento = asiento and a.fila=fila;
	update asientos 
    set ocupado=true
    where id=v_asientoid;
     
if v_asientoid is null or v_ocupado = true then
	rollback;
else 
	commit;
end if;
end //	
delimiter ;

drop procedure realizar_reservacion;


select * from asientos;
select * from reservas;
call realizar_reservacion("A",1);
call realizar_reservacion("A",1);
call realizar_reservacion("A",1);

select * from asientos;
select * from reservas;

 
 
Inventario y ventas:
Gestiona el inventario de una tienda en línea. Cuando un cliente realiza una compra, asegúrate de que el producto se deduzca del inventario solo si la transacción de compra se completa correctamente.

Actualización de puntos de fidelidad:
Crea un programa de puntos de fidelidad para una tienda. Los clientes ganan puntos con cada compra y pueden canjearlos por descuentos. Utiliza una transacción para garantizar que los puntos se actualicen correctamente cuando se realiza una compra.

Gestión de pedidos:
Implementa un sistema de gestión de pedidos para un restaurante. Los clientes pueden realizar pedidos en línea, y las transacciones garantizan que los pedidos se registren correctamente y que los ingredientes se descuenten del inventario en el momento adecuado.


