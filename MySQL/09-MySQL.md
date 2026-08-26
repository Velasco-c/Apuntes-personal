# Optimización de Consultas, Transacciones, Particionamiento y Seguridad en MySQL

## 1. Optimización de consultas

La **optimización de consultas** es un proceso fundamental en la administración de bases de datos. Su objetivo es conseguir que las consultas se ejecuten de la manera más eficiente posible, reduciendo el tiempo de respuesta y el consumo de recursos.

En términos generales, **optimizar** significa realizar una tarea de la manera más eficiente y efectiva posible.

En el contexto de las bases de datos, optimizar una consulta significa ajustar su estructura para que el motor de base de datos pueda obtener la información solicitada utilizando la menor cantidad posible de recursos, como:

- CPU.
- Memoria.
- Operaciones de lectura y escritura.
- Tiempo de procesamiento.

> [!IMPORTANT]
> Una consulta que funciona correctamente no necesariamente está optimizada. Una consulta puede devolver el resultado esperado y, al mismo tiempo, consumir demasiados recursos o tardar demasiado cuando la cantidad de datos aumenta.

---

## 2. Ventajas de la optimización de consultas

### Mejor rendimiento

Las consultas optimizadas se ejecutan más rápidamente. Esto es especialmente importante cuando se trabaja con bases de datos grandes o sistemas que reciben muchas solicitudes simultáneas.

### Uso eficiente de recursos

Una consulta optimizada puede reducir el consumo de:

- CPU.
- Memoria.
- Operaciones de entrada y salida.
- Tiempo de procesamiento.

### Escalabilidad

Una base de datos con consultas correctamente optimizadas puede manejar un mayor volumen de datos y usuarios concurrentes sin que el rendimiento se degrade rápidamente.

---

# 3. Técnicas de optimización de consultas

Existen diferentes técnicas para mejorar el rendimiento de las consultas. Entre ellas se encuentran:

- Evitar subconsultas innecesarias.
- Utilizar índices apropiadamente.
- Utilizar `EXPLAIN` para analizar consultas.
- Reducir la cantidad de datos procesados.
- Utilizar correctamente `JOIN`.
- Utilizar caché cuando sea apropiado.
- Particionar tablas grandes cuando el caso de uso lo justifique.

---

## 4. Evitar subconsultas innecesarias

Una de las técnicas utilizadas para optimizar consultas consiste en analizar si una **subconsulta** puede reemplazarse por una operación equivalente mediante `JOIN`.

Por ejemplo, se desea encontrar todos los usuarios que realizaron al menos una compra.

### Consulta con subconsulta

```sql
SELECT nombre
FROM ventas
WHERE cliente_id IN (
    SELECT id
    FROM clientes
);
````

La subconsulta obtiene los identificadores de los clientes y posteriormente la consulta externa busca los registros correspondientes.

Una alternativa mediante `JOIN` es:

```sql
SELECT DISTINCT clientes.nombre
FROM clientes
INNER JOIN ventas
    ON clientes.id = ventas.cliente_id;
```

### Explicación

`INNER JOIN` relaciona directamente las tablas `clientes` y `ventas`.

La condición:

```sql
ON clientes.id = ventas.cliente_id
```

establece la relación entre ambas tablas.

Se utiliza `DISTINCT` porque un mismo cliente puede tener varias ventas. Sin `DISTINCT`, el nombre del cliente podría aparecer varias veces.

> [!NOTE]
> Reemplazar una subconsulta por un `JOIN` no garantiza automáticamente un mejor rendimiento en todos los casos. El optimizador de MySQL puede elegir diferentes planes de ejecución dependiendo de las tablas, índices, estadísticas y cantidad de datos.

---

# 5. Ejemplo de optimización con una base de datos de libros

El siguiente ejemplo crea una base de datos llamada `libreria`, crea una tabla de libros e inserta registros para posteriormente realizar consultas y trabajar con índices.

## 5.1 Crear la base de datos

```sql
CREATE DATABASE IF NOT EXISTS libreria;

USE libreria;
```

---

## 5.2 Crear la tabla `Libros`

```sql
CREATE TABLE IF NOT EXISTS Libros (
    ID INT AUTO_INCREMENT,
    Titulo VARCHAR(100),
    Autor VARCHAR(100),
    Anio INT,
    PRIMARY KEY (ID)
);
```

### Estructura de la tabla

| Columna  | Tipo           | Descripción              |
| -------- | -------------- | ------------------------ |
| `ID`     | `INT`          | Identificador del libro. |
| `Titulo` | `VARCHAR(100)` | Título del libro.        |
| `Autor`  | `VARCHAR(100)` | Autor del libro.         |
| `Anio`   | `INT`          | Año de publicación.      |

La columna `ID` utiliza `AUTO_INCREMENT`, por lo que MySQL genera automáticamente un nuevo identificador para cada registro.

La columna `ID` también funciona como `PRIMARY KEY`.

---

## 5.3 Insertar los registros

```sql
-- =============================================
-- INSERCIÓN DE REGISTROS EN LA TABLA Libros
-- Distribución de años: 1990 - 2026
-- =============================================

INSERT IGNORE INTO Libros (Titulo, Autor, Anio) VALUES
('El Último Imperio', 'Beatriz Ramírez', 2004),
('Infinito Reino', 'Laura Vargas', 2017),
('Secreto Tiempo', 'Miguel Gutiérrez', 1991),
('Crónicas de Mar (La Revelación)', 'Arturo Ramírez', 2018),
('El Viento de Viento (Parte I)', 'Alejandro Jiménez', 2017),
('Azul Viento', 'Valeria López', 1995),
('Camino a Imperio', 'Gonzalo Mendoza', 2006),
('Secreto Reino', 'Carmen Díaz', 1995),
('Crónicas de Fuego (La Revelación)', 'Marta Vargas', 2002),
('Luz en Alma', 'Miguel Ríos', 2008),
('Oscuro Bosque (Saga)', 'Beatriz Morales', 2013),
('Olvidado Castillo', 'Beatriz Jiménez', 1994),
('Fuego en Enigma', 'Rosa Pérez', 2019),
('Camino a Viento (La Revelación)', 'Miguel Hernández', 2010),
('Secreto Bosque (Segunda Edición)', 'Claudia Torres', 1994),
('Eterno Horizonte (Segunda Edición)', 'Ana Ruiz', 2021),
('Camino a Enigma', 'Pablo González', 2005),
('Crónicas de Pensamiento', 'Silvia Vargas', 2015),
('Sombra de Bosque (El Origen)', 'Julio Ortiz', 1995),
('Secreto Imperio', 'Alejandro Hernández', 2017),
('Fuego en Alma', 'Alba Gutiérrez', 2006),
('Crónicas de Tiempo (Parte I)', 'Beatriz Ríos', 2011),
('Invisible Fuego', 'Alba García', 2006),
('La Leyenda de Espejo', 'Javier Ruiz', 2009),
('El Último Espacio (El Origen)', 'Marta Ríos', 2000),
('Crónicas de Espacio', 'Arturo Ortiz', 2001),
('Invisible Bosque (Segunda Edición)', 'Javier Castro', 2001),
('Perdido Laberinto', 'Marina Rodríguez', 2024),
('La Leyenda de Viento', 'Laura Ruiz', 2017),
('Sombra de Espejo', 'Carmen Navarro', 2003),
('Camino a Silencio', 'Claudia Reyes', 2002),
('El Misterio de Cielo', 'Fernando Martínez', 2026),
('Perdido Universo (Parte I)', 'Julio López', 2025),
('Fuego en Fuego', 'Daniel Gutiérrez', 1996),
('El Caso de Universo', 'Claudia López', 2018),
('El Caso de Noche (Segunda Edición)', 'Arturo Jiménez', 2010),
('El Último Viento', 'Carlos Gómez', 2009),
('Rojo Universo (Saga)', 'Diego Morales', 2003),
('El Primer Mar', 'Carlos Vargas', 2002),
('Dorado Fuego', 'Fernando Gómez', 2008),
('El Misterio de Sol', 'Pablo Flores', 1997),
('Perdido Silencio', 'Silvia Martínez', 1996),
('El Caso de Sol (Saga)', 'Valeria Morales', 2014),
('Oscuro Mar', 'Diego Torres', 2007),
('El Caso de Silencio', 'Lucia Ortiz', 2002),
('El Primer Refugio', 'Carlos Martínez', 2000),
('Eterno Bosque', 'Alba Torres', 2019),
('Luz en Universo', 'Isabel Vargas', 2012),
('El Arte de Mar', 'Daniel Mendoza', 2023),
('Infinito Horizonte', 'Valeria Ramírez', 1991),
('La Leyenda de Mar (Parte I)', 'Fernando Torres', 1997),
('El Misterio de Espejo', 'Sofia Martínez', 2007),
('Crónicas de Tiempo (Segunda Edición)', 'Carmen López', 2012),
('Infinito Silencio (Parte I)', 'Ana Gómez', 1991),
('El Caso de Mar', 'Elena Ortiz', 2023),
('El Primer Código', 'Sofia Ruiz', 2011),
('Luz en Silencio', 'Silvia Jiménez', 2005),
('Dorado Crepúsculo', 'Javier Castro', 2003),
('Crónicas de Silencio', 'Patricia Martínez', 2021),
('Silencioso Mar (Saga)', 'Pablo Martínez', 2023),
('Luz en Crepúsculo (La Revelación)', 'Claudia Ramírez', 1991),
('Camino a Universo', 'Claudia Ruiz', 2018),
('La Leyenda de Horizonte (Saga)', 'Stephen Jiménez', 1999),
('Silencioso Imperio', 'Daniel Martínez', 2003),
('El Viento de Espacio', 'Stephen Morales', 1998),
('El Arte de Sol (Parte I)', 'Julio Díaz', 2020),
('Camino a Laberinto', 'Marina López', 2020),
('El Primer Laberinto', 'Carmen Ortiz', 1991),
('El Caso de Universo (La Revelación)', 'Claudia Jiménez', 1990),
('Eterno Enigma', 'Arturo Rodríguez', 2009),
('Camino a Espacio', 'Elena Rodríguez', 2011),
('Infinito Destino (El Origen)', 'Daniel Morales', 2004),
('Fuego en Espacio', 'Alba Flores', 2008),
('Crónicas de Sol', 'Stephen López', 2025),
('Olvidado Mar (Saga)', 'Mario Pérez', 2013),
('Camino a Mar (Parte I)', 'Ricardo Ramírez', 2011),
('Perdido Mar', 'Gonzalo López', 1998),
('Eterno Mar', 'Carlos Castro', 2007),
('Eterno Sol (Parte I)', 'Elena Díaz', 2011),
('Oscuro Universo', 'Ricardo Martínez', 2000),
('Fuego en Noche', 'Daniel Gómez', 2022),
('Sombra de Sol', 'Pablo Gutiérrez', 1996),
('Oscuro Viento', 'Gonzalo Ramírez', 2013),
('Dorado Espacio (Parte I)', 'Marina Ortiz', 2022),
('Dorado Espacio (Saga)', 'Elena Gómez', 1993),
('Infinito Pensamiento (Saga)', 'Javier Gutiérrez', 1990),
('El Viento de Viento (Saga)', 'Gonzalo Ramírez', 2006),
('El Arte de Bosque (Segunda Edición)', 'Julio Ortiz', 2003),
('Oscuro Laberinto', 'Ricardo Ortiz', 1996),
('El Arte de Imperio (El Origen)', 'Alejandro Rivera', 2003),
('Secreto Sol', 'Lucia Martínez', 2009),
('La Leyenda de Crepúsculo (Parte I)', 'Pablo Díaz', 2019),
('Luz en Espejo', 'Mario López', 1994),
('Eterno Mar (Segunda Edición)', 'Fernando Gutiérrez', 2019),
('Luz en Destino', 'Patricia Jiménez', 2026),
('El Último Silencio', 'Marina Jiménez', 1991),
('El Misterio de Cielo (El Origen)', 'Daniel Díaz', 2022),
('Crónicas de Espacio (Saga)', 'Fernando López', 1999),
('Dorado Horizonte', 'Gabriel Navarro', 2024),
('El Primer Universo', 'Alba López', 2011);
```

---

# 6. Índices

Un **índice** es una estructura que permite al motor de base de datos localizar determinados registros de manera más eficiente.

Si una columna se utiliza frecuentemente para buscar información, un índice puede reducir la cantidad de datos que MySQL necesita revisar.

Por ejemplo, se crea un índice sobre `autor`:

```sql
CREATE INDEX indx_autor
ON Libros(autor);
```

Posteriormente se puede realizar una búsqueda utilizando esa columna:

```sql
SELECT *
FROM Libros
WHERE autor = 'Daniel Diaz';
```

> [!IMPORTANT]
> Los índices pueden acelerar las consultas de lectura, pero también tienen un costo. Deben mantenerse cuando se insertan, actualizan o eliminan registros, por lo que no conviene crear índices indiscriminadamente.

---

# 7. Consultas con subconsultas y `JOIN`

Una consulta mediante subconsulta puede escribirse de la siguiente manera:

```sql
SELECT *
FROM categorias
WHERE id IN (
    SELECT categoria_id
    FROM productos
);
```

Una alternativa mediante `JOIN` es:

```sql
SELECT DISTINCT
    c.codigo,
    c.nombre
FROM categoria c
INNER JOIN productos p
    ON c.id = p.categoria_id;
```

La segunda consulta relaciona directamente las categorías con los productos.

---

# 8. Caché de consultas

El **caching** consiste en almacenar temporalmente resultados de consultas frecuentes para poder reutilizarlos posteriormente sin tener que procesar nuevamente toda la consulta.

Esta técnica puede ser especialmente útil en aplicaciones con:

* Gran volumen de lecturas.
* Consultas repetitivas.
* Datos que no cambian constantemente.
* Alta cantidad de solicitudes.

En arquitecturas modernas es común utilizar herramientas externas de caché como:

* Redis.
* Memcached.

> [!NOTE]
> El uso de caché requiere analizar la frecuencia de actualización de los datos. Si los datos cambian constantemente, es necesario diseñar correctamente la estrategia de invalidación o actualización de la caché.

---

# 9. Particionamiento de tablas en MySQL

El **particionamiento** es una técnica que divide una tabla grande en segmentos más pequeños llamados **particiones**.

Las particiones se organizan de acuerdo con determinados criterios, por ejemplo:

* Rangos de fechas.
* Valores de una columna.
* Rangos de valores numéricos.

La tabla continúa siendo tratada lógicamente como una única tabla, mientras que internamente sus datos se distribuyen entre las particiones.

---

## 9.1 Ventajas del particionamiento

### Gestión de grandes volúmenes de datos

Facilita la administración de tablas extremadamente grandes al dividir físicamente los datos en partes más manejables.

### Mejora potencial del rendimiento

Cuando una consulta utiliza una condición compatible con el esquema de particionamiento, MySQL puede acceder únicamente a las particiones relevantes.

### Optimización de consultas

El **partition pruning** permite que MySQL descarte particiones que no contienen datos relevantes para determinadas consultas.

Esto puede reducir significativamente la cantidad de datos que debe examinarse.

---

## 9.2 Selección del criterio de particionamiento

El criterio utilizado para particionar una tabla depende de:

* La naturaleza de los datos.
* El volumen de información.
* Las consultas más frecuentes.
* La distribución de los datos.

Por ejemplo, en un sistema de registros financieros puede ser conveniente particionar por fecha:

```text
2024
2025
2026
...
```

Esto resulta especialmente útil para consultas que trabajan con determinados períodos de tiempo.

---

# 10. Gestión de transacciones

MySQL proporciona mecanismos para trabajar con **transacciones**, permitiendo mantener un equilibrio entre rendimiento y confiabilidad en aplicaciones que realizan operaciones concurrentes de lectura y escritura.

## 10.1 ¿Qué es una transacción?

Una **transacción** es una secuencia de operaciones de base de datos que se trata como una única unidad lógica de trabajo.

Si una operación crítica falla y la transacción se revierte, los cambios realizados dentro de ella pueden deshacerse.

Las instrucciones principales para controlar una transacción son:

```sql
START TRANSACTION;
```

```sql
COMMIT;
```

```sql
ROLLBACK;
```

### `START TRANSACTION`

Inicia una transacción.

### `COMMIT`

Confirma los cambios realizados durante la transacción.

### `ROLLBACK`

Revierte los cambios realizados durante la transacción.

---

# 11. Bloqueos

Los **bloqueos (locks)** son mecanismos utilizados para controlar el acceso concurrente a los recursos de la base de datos.

Su objetivo es evitar que varias transacciones realicen operaciones incompatibles sobre los mismos datos al mismo tiempo.

Los bloqueos ayudan a mantener la **consistencia de los datos** durante operaciones concurrentes.

---

# 12. Propiedades ACID de las transacciones

Las transacciones relacionales se estudian normalmente mediante las propiedades **ACID**:

| Propiedad        | Significado                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Atomicidad**   | La transacción se considera una unidad de trabajo: sus operaciones se confirman o se revierten según el resultado de la transacción. |
| **Consistencia** | Una transacción debe llevar la base de datos de un estado válido a otro estado válido.                                               |
| **Aislamiento**  | Las transacciones concurrentes deben comportarse de acuerdo con las reglas de aislamiento configuradas.                              |
| **Durabilidad**  | Una vez confirmados los cambios mediante `COMMIT`, estos deben persistir según las garantías del sistema de almacenamiento.          |

---

# 13. Consultas preparadas con `PREPARE` y `EXECUTE`

MySQL permite preparar sentencias SQL mediante `PREPARE`.

Una sentencia preparada contiene marcadores de posición, como `?`, que posteriormente reciben valores durante su ejecución.

El proceso básico consiste en:

1. Preparar la consulta.
2. Asignar valores a variables.
3. Ejecutar la consulta.
4. Liberar la sentencia preparada.

---

## 13.1 Ejemplo

```sql
USE acme_store;

-- Preparamos la consulta para su uso
PREPARE stmt
FROM 'SELECT * FROM usuarios WHERE id = ?';

-- Asignamos un valor a la variable
SET @user_id = 2;

-- Ejecutamos la consulta preparada
EXECUTE stmt USING @user_id;

-- Liberamos la consulta preparada
DEALLOCATE PREPARE stmt;
```

### Explicación

La consulta contiene un marcador:

```sql
?
```

El valor se proporciona posteriormente mediante:

```sql
SET @user_id = 2;
```

La sentencia se ejecuta mediante:

```sql
EXECUTE stmt USING @user_id;
```

Finalmente, se libera la sentencia preparada:

```sql
DEALLOCATE PREPARE stmt;
```

---

# 14. Procedimiento para asignar categorías según el salario

Este procedimiento utiliza:

* Variables locales.
* Un `CURSOR`.
* Un `HANDLER`.
* Un `LOOP`.
* `IF`.
* `CASE`.
* `UPDATE`.

Primero se agrega la columna `categoria`:

```sql
SELECT *
FROM empleados;

ALTER TABLE empleados
ADD categoria VARCHAR(10);
```

---

## 14.1 Procedimiento almacenado

```sql
DELIMITER //

CREATE PROCEDURE asignar_categoria_salario()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE emp_id INT;
    DECLARE empleado_salario DECIMAL(8,2);

    DECLARE cursor1 CURSOR FOR
        SELECT id, salario
        FROM empleados;

    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET done = TRUE;

    OPEN cursor1;

    read_loop: LOOP

        FETCH cursor1 INTO emp_id, empleado_salario;

        IF done THEN
            LEAVE read_loop;
        END IF;

        CASE
            WHEN empleado_salario <= 3000 THEN
                UPDATE empleados
                SET categoria = 'BAJO'
                WHERE id = emp_id;

            WHEN empleado_salario > 3000
                 AND empleado_salario < 7000 THEN
                UPDATE empleados
                SET categoria = 'MEDIO'
                WHERE id = emp_id;

            ELSE
                UPDATE empleados
                SET categoria = 'ALTO'
                WHERE id = emp_id;
        END CASE;

    END LOOP;

    CLOSE cursor1;
END //

DELIMITER ;
```

Se ejecuta mediante:

```sql
CALL asignar_categoria_salario();
```

Posteriormente se pueden consultar los resultados:

```sql
SELECT *
FROM usuarios;
```

---

## 14.2 Funcionamiento del cursor

El cursor:

```sql
DECLARE cursor1 CURSOR FOR
    SELECT id, salario
    FROM empleados;
```

permite recorrer los resultados de la consulta:

```sql
SELECT id, salario
FROM empleados;
```

Cada registro se obtiene mediante:

```sql
FETCH cursor1 INTO emp_id, empleado_salario;
```

El valor de `id` se almacena en:

```sql
emp_id
```

y el salario se almacena en:

```sql
empleado_salario
```

Cuando ya no existen más registros, el `HANDLER` cambia el valor de `done`:

```sql
DECLARE CONTINUE HANDLER FOR NOT FOUND
    SET done = TRUE;
```

Entonces:

```sql
IF done THEN
    LEAVE read_loop;
END IF;
```

finaliza el ciclo.

---

# 15. Consultas preparadas sobre empleados

También se puede preparar una consulta que devuelva información específica de un empleado:

```sql
DESCRIBE empleados;

PREPARE stmt
FROM 'SELECT nombre, categoria, salario
      FROM empleados
      WHERE id = ?';

SET @user_id = 3;

EXECUTE stmt USING @user_id;

DEALLOCATE PREPARE stmt;
```

---

# 16. Ejemplo completo de particionamiento

El siguiente ejemplo crea una base de datos `Tienda` con tablas para productos y ventas.

## 16.1 Crear la base de datos

```sql
-- Elimina la base de datos si existe
DROP DATABASE IF EXISTS Tienda;

-- Crea la base de datos
CREATE DATABASE IF NOT EXISTS Tienda;

USE Tienda;
```

---

## 16.2 Crear las tablas

```sql
-- Elimina las tablas si existen
DROP TABLE IF EXISTS Ventas;
DROP TABLE IF EXISTS Productos;

-- Crea las tablas
CREATE TABLE IF NOT EXISTS Productos (
    id INT AUTO_INCREMENT,
    nombre VARCHAR(255),
    precio DECIMAL(10,2),
    stock INT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Ventas (
    id INT AUTO_INCREMENT,
    producto_id INT,
    cantidad INT,
    fecha_venta DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (producto_id) REFERENCES Productos(id)
);
```

La tabla `Ventas` mantiene una relación con `Productos` mediante:

```sql
FOREIGN KEY (producto_id)
REFERENCES Productos(id)
```

---

## 16.3 Insertar productos

```sql
INSERT INTO Productos (nombre, precio, stock) VALUES
('Laptop Dell XPS 13', 1200.00, 15),
('Mouse Inalámbrico Logitech', 25.50, 50),
('Teclado Mecánico RGB', 85.00, 30),
('Monitor Gaming 27 IPS', 320.00, 20),
('Auriculares Bluetooth Sony', 150.00, 40),
('Silla Ergonómica de Oficina', 210.00, 12),
('Disco Duro Externo 2TB', 75.00, 25),
('Webcam Full HD 1080p', 45.00, 35),
('Micrófono Condensador USB', 95.00, 18),
('Hub USB-C 7 en 1', 35.00, 45);
```

---

## 16.4 Insertar ventas

```sql
INSERT INTO Ventas (producto_id, cantidad, fecha_venta) VALUES
(1, 1, '2026-01-02'),
(2, 2, '2026-01-03'),
(5, 1, '2026-01-04'),
(8, 3, '2026-01-05'),
(3, 1, '2026-01-07'),
(4, 1, '2026-01-08'),
(7, 2, '2026-01-10'),
(10, 4, '2026-01-11'),
(2, 1, '2026-01-12'),
(6, 1, '2026-01-14'),
(9, 2, '2026-01-15'),
(5, 1, '2026-01-17'),
(3, 2, '2026-01-18'),
(1, 1, '2026-01-20'),
(8, 1, '2026-01-22'),
(2, 5, '2026-01-23'),
(10, 2, '2026-01-25'),
(7, 1, '2026-01-27'),
(4, 1, '2026-01-28'),
(5, 3, '2026-01-30'),
(2, 2, '2026-02-01'),
(6, 1, '2026-02-02'),
(9, 1, '2026-02-04'),
(3, 1, '2026-02-05'),
(8, 2, '2026-02-07'),
(10, 3, '2026-02-08'),
(1, 1, '2026-02-10'),
(5, 2, '2026-02-11'),
(7, 1, '2026-02-13'),
(2, 3, '2026-02-14'),
(4, 2, '2026-02-15'),
(8, 1, '2026-02-17'),
(6, 1, '2026-02-18'),
(9, 2, '2026-02-20'),
(10, 1, '2026-02-21'),
(3, 3, '2026-02-23'),
(5, 1, '2026-02-24'),
(7, 2, '2026-02-26'),
(2, 4, '2026-02-27'),
(1, 1, '2026-02-28'),
(8, 2, '2026-03-01'),
(10, 2, '2026-03-02'),
(4, 1, '2026-03-04'),
(2, 3, '2026-03-05'),
(5, 1, '2026-03-07'),
(9, 1, '2026-03-08'),
(6, 1, '2026-03-10'),
(3, 2, '2026-03-11'),
(7, 3, '2026-03-13'),
(1, 1, '2026-03-14'),
(8, 1, '2026-03-16'),
(10, 5, '2026-03-17'),
(2, 2, '2026-03-19'),
(5, 2, '2026-03-20'),
(4, 1, '2026-03-22'),
(9, 3, '2026-03-23'),
(7, 1, '2026-03-25'),
(3, 1, '2026-03-26'),
(6, 1, '2026-03-28'),
(10, 2, '2026-03-30');
```

---

# 17. Ranking de productos por mes

La función de ventana `RANK()` permite asignar una posición a cada producto según la cantidad vendida.

```sql
SELECT
    DATE_FORMAT(fecha_venta, '%m') AS mes,
    producto_id,
    SUM(cantidad) AS total_cantidad_vendida,
    RANK() OVER (
        PARTITION BY DATE_FORMAT(fecha_venta, '%m')
        ORDER BY SUM(cantidad) DESC
    ) AS ranking_mes
FROM Ventas
GROUP BY mes, producto_id;
```

### Explicación

`SUM(cantidad)` calcula la cantidad total vendida.

```sql
SUM(cantidad) AS total_cantidad_vendida
```

`PARTITION BY` divide los resultados de la función de ventana por mes:

```sql
PARTITION BY DATE_FORMAT(fecha_venta, '%m')
```

Después `RANK()` establece la posición de cada producto:

```sql
RANK() OVER (...)
```

Los productos se ordenan de mayor a menor cantidad vendida:

```sql
ORDER BY SUM(cantidad) DESC
```

---

## 17.1 Consultar la estructura de `Ventas`

```sql
DESC Ventas;
```

---

# 18. Particionamiento por año

El siguiente ejemplo crea una tabla de ventas particionada por el año de la fecha.

```sql
USE acme_store;

CREATE TABLE clientes1 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(60),
    email VARCHAR(60)
);
```

La tabla de ventas se define de la siguiente manera:

```sql
CREATE TABLE ventas1 (
    id_cliente INT,
    monto DECIMAL(10,2),
    fecha DATE
)
ENGINE = InnoDB
PARTITION BY RANGE (YEAR(fecha)) (
    PARTITION p2020 VALUES LESS THAN (2021),
    PARTITION p2021 VALUES LESS THAN (2022),
    PARTITION p2022 VALUES LESS THAN (2023)
);
```

---

## 18.1 Funcionamiento de las particiones

La expresión:

```sql
PARTITION BY RANGE (YEAR(fecha))
```

indica que las filas se distribuirán según el año obtenido de la columna `fecha`.

Las particiones se definen mediante límites:

```sql
PARTITION p2020 VALUES LESS THAN (2021)
```

Esta partición contiene fechas cuyo año es menor que `2021`, por lo que corresponde al año 2020 dentro del rango planteado.

De forma similar:

```sql
PARTITION p2021 VALUES LESS THAN (2022)
```

corresponde al año 2021.

Y:

```sql
PARTITION p2022 VALUES LESS THAN (2023)
```

corresponde al año 2022.

> [!IMPORTANT]
> Al utilizar `RANGE`, es necesario planificar correctamente los límites y cubrir los valores que realmente pueden aparecer en la tabla. Una definición de particiones incompleta puede impedir la inserción de filas que no pertenezcan a ninguna partición.

---

# 19. Seguridad en MySQL

La **seguridad de bases de datos** comprende las medidas utilizadas para proteger la información almacenada frente a accesos, modificaciones, eliminaciones o compromisos no autorizados.

En MySQL, la seguridad incluye aspectos como:

* Autenticación de usuarios.
* Contraseñas.
* Privilegios.
* Roles.
* Control de acceso.
* Protección de los datos.
* Protección de las conexiones.
* Prevención de ataques.
* Auditoría y administración de permisos.

Uno de los riesgos conocidos en aplicaciones que interactúan con bases de datos es la **inyección SQL**, por lo que las aplicaciones deben utilizar mecanismos adecuados para separar los datos proporcionados por el usuario de las instrucciones SQL.

---

# 20. Usuarios en MySQL

MySQL administra las cuentas mediante una combinación de:

```text
usuario@host
```

Por ejemplo:

```sql
'Velasco'@'localhost'
```

Esto identifica al usuario `Velasco` cuando se conecta desde `localhost`.

---

# 21. Usuarios administrativos y anónimos

Durante la instalación y configuración de MySQL pueden existir diferentes cuentas, dependiendo de la versión y del método de instalación.

### `root`

Es una cuenta administrativa con privilegios elevados. Su uso debe limitarse a tareas administrativas.

### Usuarios anónimos

Una cuenta anónima no tiene un nombre de usuario explícito. Si existe y no es necesaria, puede eliminarse para reducir posibles riesgos de seguridad.

---

# 22. Crear usuarios

Para eliminar un usuario antes de crearlo nuevamente:

```sql
DROP USER IF EXISTS 'Velasco'@'localhost';
```

Para crear el usuario:

```sql
CREATE USER 'Velasco'@'localhost'
IDENTIFIED BY 'Velasito2006@';
```

La parte:

```sql
'Velasco'@'localhost'
```

define el nombre de la cuenta y el host desde el cual puede autenticarse.

`IDENTIFIED BY` establece la contraseña de la cuenta.

---

# 23. Asignación de privilegios con `GRANT`

`GRANT` permite asignar privilegios a un usuario.

```sql
GRANT SELECT, INSERT, UPDATE
ON acme_store.*
TO 'Velasco'@'localhost';
```

En este caso, el usuario obtiene permisos para:

* `SELECT`.
* `INSERT`.
* `UPDATE`.

sobre los objetos de:

```text
acme_store.*
```

El `*` representa los objetos de la base de datos especificada.

---

# 24. Consultar los privilegios

Los privilegios de un usuario pueden consultarse mediante:

```sql
SHOW GRANTS FOR 'Velasco'@'localhost';
```

Esta instrucción permite comprobar qué permisos tiene asignados la cuenta.

---

# 25. Privilegios específicos sobre tablas

También es posible asignar privilegios sobre tablas concretas.

```sql
CREATE USER 'vendedor'@'localhost'
IDENTIFIED BY 'vendedor2006@';

GRANT SELECT, INSERT, UPDATE, DELETE
ON acme_store.productos
TO 'vendedor'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE
ON acme_store.categoria
TO 'vendedor'@'localhost';
```

En este caso, los permisos se limitan a las tablas especificadas.

---

# 26. Revocar privilegios

`REVOKE` permite retirar privilegios previamente concedidos.

```sql
REVOKE SELECT
ON acme_store.*
FROM 'Velasco'@'localhost';
```

Esta instrucción elimina el privilegio `SELECT` sobre los objetos de `acme_store`.

---

# 27. Límites de uso de una cuenta

MySQL permite establecer determinados límites de recursos para una cuenta.

Por ejemplo:

```sql
ALTER USER 'Velasco'@'localhost'
WITH MAX_QUERIES_PER_HOUR 100;
```

Esto establece un máximo de 100 consultas por hora para esa cuenta.

---

# 28. Privilegios sobre columnas

También pueden concederse permisos específicos sobre determinadas columnas.

```sql
GRANT SELECT (id, nombre)
ON acme_store.empleados
TO 'Velasco'@'localhost';
```

En este caso, el privilegio `SELECT` se limita a las columnas:

* `id`.
* `nombre`.

de la tabla `empleados`.

---

# 29. Creación de un usuario administrativo

Para crear una cuenta administrativa:

```sql
DROP USER IF EXISTS 'Velasco_admin'@'localhost';

CREATE USER 'Velasco_admin'@'localhost'
IDENTIFIED BY 'VelasAdmin2006@';
```

Después se pueden asignar privilegios elevados:

```sql
GRANT ALL PRIVILEGES
ON *.*
TO 'Velasco_admin'@'localhost'
WITH GRANT OPTION;
```

`ALL PRIVILEGES` concede todos los privilegios disponibles aplicables al ámbito indicado.

`*.*` representa todas las bases de datos y tablas a las que se aplica el privilegio.

`WITH GRANT OPTION` permite que el usuario pueda conceder determinados privilegios a otras cuentas, de acuerdo con los privilegios que posee.

Los privilegios pueden verificarse mediante:

```sql
SHOW GRANTS FOR 'Velasco_admin'@'localhost';
```

> [!WARNING]
> Una cuenta con privilegios globales y `WITH GRANT OPTION` tiene un nivel de acceso muy elevado. Este tipo de cuenta debe reservarse para tareas administrativas y utilizarse con precaución.

---

# 30. Resumen

La optimización y administración de una base de datos requiere comprender diferentes mecanismos que trabajan en conjunto.

Los principales conceptos estudiados son:

* **Optimización de consultas:** busca reducir el tiempo de ejecución y el consumo de recursos.
* **Subconsultas:** pueden ser apropiadas en determinados casos, aunque algunas consultas pueden expresarse mediante `JOIN`.
* **Índices:** permiten acelerar determinadas búsquedas, aunque agregan costos de mantenimiento.
* **Caché:** permite reutilizar resultados frecuentes y reducir procesamiento repetitivo.
* **Particionamiento:** divide tablas grandes en particiones administrables y puede permitir que MySQL descarte particiones irrelevantes.
* **Transacciones:** agrupan operaciones como una unidad lógica.
* **ACID:** describe propiedades fundamentales de las transacciones.
* **Bloqueos:** controlan el acceso concurrente a los recursos.
* **`PREPARE` y `EXECUTE`:** permiten trabajar con sentencias preparadas y marcadores de posición.
* **`CURSOR`:** permite recorrer resultados dentro de procedimientos almacenados.
* **`HANDLER`:** permite controlar determinadas condiciones durante la ejecución de procedimientos.
* **`GRANT`:** concede privilegios.
* **`REVOKE`:** revoca privilegios.
* **`CREATE USER`:** crea cuentas.
* **`ALTER USER`:** modifica propiedades de cuentas.
* **`SHOW GRANTS`:** permite consultar los privilegios asignados.

# Glosario

| Término                     | Descripción                                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `Query`                     | Consulta enviada al motor de base de datos para obtener o modificar información.                                                |
| `Optimización de consultas` | Proceso de mejorar la ejecución de una consulta para reducir tiempo y consumo de recursos.                                      |
| `Subconsulta`               | Consulta SQL incluida dentro de otra consulta.                                                                                  |
| `JOIN`                      | Operación utilizada para combinar registros relacionados entre tablas.                                                          |
| `INNER JOIN`                | `JOIN` que devuelve registros que tienen coincidencias en ambas tablas.                                                         |
| `DISTINCT`                  | Elimina resultados duplicados del conjunto devuelto por una consulta.                                                           |
| `Índice`                    | Estructura de datos utilizada para acelerar determinadas operaciones de búsqueda.                                               |
| `Caching`                   | Almacenamiento temporal de información para reutilizarla posteriormente.                                                        |
| `Redis`                     | Sistema de almacenamiento de datos en memoria utilizado frecuentemente como caché.                                              |
| `Memcached`                 | Sistema distribuido de almacenamiento de datos en memoria utilizado como caché.                                                 |
| `Partición`                 | Segmento en el que se divide una tabla particionada.                                                                            |
| `Partition pruning`         | Proceso mediante el cual MySQL evita consultar particiones que no pueden contener resultados relevantes.                        |
| `Transacción`               | Conjunto de operaciones tratadas como una unidad lógica de trabajo.                                                             |
| `ACID`                      | Conjunto de propiedades asociadas a la confiabilidad de las transacciones: Atomicidad, Consistencia, Aislamiento y Durabilidad. |
| `Atomicidad`                | Propiedad que trata las operaciones de una transacción como una unidad de trabajo.                                              |
| `Consistencia`              | Propiedad que mantiene la base de datos en estados válidos antes y después de una transacción.                                  |
| `Aislamiento`               | Propiedad que controla cómo interactúan las transacciones concurrentes.                                                         |
| `Durabilidad`               | Propiedad que garantiza la persistencia de los cambios confirmados.                                                             |
| `Lock`                      | Mecanismo utilizado para controlar el acceso concurrente a recursos de la base de datos.                                        |
| `PREPARE`                   | Instrucción utilizada para preparar una sentencia SQL para su posterior ejecución.                                              |
| `EXECUTE`                   | Instrucción utilizada para ejecutar una sentencia previamente preparada.                                                        |
| `DEALLOCATE PREPARE`        | Libera una sentencia SQL preparada.                                                                                             |
| `Cursor`                    | Mecanismo utilizado para recorrer los registros de un conjunto de resultados dentro de código almacenado.                       |
| `Handler`                   | Mecanismo que permite definir cómo responder ante determinadas condiciones o errores durante la ejecución de código almacenado. |
| `GRANT`                     | Instrucción utilizada para conceder privilegios a usuarios o roles.                                                             |
| `REVOKE`                    | Instrucción utilizada para retirar privilegios.                                                                                 |
| `Privilege`                 | Permiso que determina qué operaciones puede realizar una cuenta sobre determinados objetos.                                     |
| `Host`                      | Origen desde el cual una cuenta de MySQL puede autenticarse.                                                                    |
| `SQL Injection`             | Vulnerabilidad que ocurre cuando datos externos pueden alterar de forma no deseada la estructura de una consulta SQL.           |
| `WITH GRANT OPTION`         | Opción que permite a una cuenta conceder determinados privilegios a otras cuentas.                                              |

