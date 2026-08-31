# Administración e importación de datasets en PostgreSQL
## Introducción a datasets

PostgreSQL ofrece diferentes mecanismos para importar y restaurar datos desde archivos.

Entre las alternativas utilizadas en esta clase se encuentran:

* `COPY` y `\COPY` para importar datos desde archivos.
* `pg_dump` para crear copias de seguridad.
* `psql` para restaurar copias en formato SQL.
* `pg_restore` para restaurar copias en formatos como `tar`.
* Consultas `UPDATE`, `DELETE` e `INSERT` para modificar y administrar los datos.

La opción más conveniente depende del formato de los datos, del tamaño del dataset y de si se necesita realizar una importación directa o restaurar una copia completa.

---

# Importación de datasets mediante `COPY`

El comando `COPY` permite transferir datos entre PostgreSQL y archivos.

Se utiliza principalmente para:

* **Exportar datos** desde PostgreSQL hacia un archivo mediante `COPY TO`.
* **Importar datos** desde un archivo hacia PostgreSQL mediante `COPY FROM`.

Una diferencia importante es desde dónde se ejecuta el acceso al archivo.

`COPY` trabaja desde la perspectiva del **servidor PostgreSQL**, por lo que el archivo debe ser accesible para el usuario que ejecuta el servidor.

Para trabajar con archivos ubicados en el equipo desde el cliente `psql`, se puede utilizar `\COPY`.

---

## Comandos iniciales en `psql`

Para conectarse a PostgreSQL:

```bash
psql -U postgres
```

Dentro de `psql`:

```text
\l
```

permite listar las bases de datos.

Para conectarse a `campus`:

```text
\c campus
```

Para describir una tabla:

```text
\d
```

---

# Creación de la tabla `customers`

Antes de importar el dataset se crea una tabla compatible con las columnas existentes en el archivo CSV.

```sql
CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(50)
);
```

La columna `id` utiliza `SERIAL`, por lo que PostgreSQL genera automáticamente valores mediante una secuencia.

---

# Uso de `\COPY`

`\COPY` es un comando propio del cliente `psql` que permite importar archivos desde el equipo donde se está ejecutando el cliente.

Plantilla:

```text
\COPY <tabla>
FROM '<RUTA DEL ARCHIVO>'
DELIMITER ',' CSV HEADER;
```

Por ejemplo:

```text
\COPY customers
FROM '/home/camper/postgresdata/customers.csv'
DELIMITER ',' CSV HEADER;
```

### Elementos principales

* `customers`: tabla donde se cargarán los datos.
* `FROM`: indica que los datos provienen de un archivo.
* `'/home/camper/postgresdata/customers.csv'`: ruta del archivo.
* `DELIMITER ','`: indica que las columnas están separadas por comas.
* `CSV`: indica que el archivo utiliza el formato CSV.
* `HEADER`: indica que la primera fila contiene los nombres de las columnas y debe omitirse como registro.

> [!NOTE]
> Es recomendable utilizar rutas absolutas cuando se trabaja con archivos para evitar problemas relacionados con el directorio actual.

---

## Importar un segundo dataset

Se puede utilizar el mismo procedimiento para cargar otro archivo en una tabla diferente.

```sql
CREATE TABLE customers_add(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(50)
);
```

Importación:

```text
\COPY customers_add
FROM '/home/camper/postgresdata/customers_add.csv'
DELIMITER ',' CSV HEADER;
```

---

# Copias de seguridad mediante `pg_dump`

`pg_dump` permite crear copias de seguridad de bases de datos o de objetos específicos de PostgreSQL.

Por ejemplo, para realizar una copia de la tabla `customers` en formato SQL:

```bash
pg_dump -U postgres -d campus -t customers \
> /home/camper/postgresdata/customers_bkc.sql
```

En este caso:

* `-U postgres`: usuario utilizado para conectarse.
* `-d campus`: base de datos de origen.
* `-t customers`: tabla que se desea respaldar.
* `>`: redirige la salida hacia un archivo.
* `customers_bkc.sql`: archivo de respaldo.

También se puede realizar para `customers_add`:

```bash
pg_dump -U postgres -d campus -t customers_add \
> /home/camper/postgresdata/customers_add_bkc.sql
```

---

# Restauración de una copia SQL

Primero se puede crear una base de datos destinada a recibir la restauración:

```sql
CREATE DATABASE campus_temp;
```

Después, desde la terminal del sistema, se restaura el archivo:

```bash
psql -U postgres -d campus_temp \
< /home/camper/postgresdata/customers_bkc.sql
```

El operador `<` utiliza el contenido del archivo como entrada para `psql`.

> [!IMPORTANT]
> `psql` se utiliza normalmente para ejecutar y restaurar scripts SQL. En este caso, el archivo generado por `pg_dump` contiene instrucciones SQL que permiten reconstruir la tabla y sus datos.

---

# Copias de seguridad en formato `tar`

`pg_dump` también permite generar copias en otros formatos.

Por ejemplo:

```bash
pg_dump -U postgres -d campus -t customers -F t \
> /home/camper/postgresdata/customers.tar
```

La opción:

```text
-F t
```

indica que la copia se genera en formato `tar`.

Este formato puede ser restaurado mediante `pg_restore`.

---

# Restauración mediante `pg_restore`

Para restaurar una copia en formato `tar`:

```bash
pg_restore -U postgres \
-d campus_temp \
-t customers \
/home/camper/postgresdata/customers.tar
```

En este caso:

* `-d campus_temp`: base de datos donde se restaurará la información.
* `-t customers`: limita la restauración a la tabla indicada.
* `customers.tar`: archivo de respaldo.

> [!NOTE]
> `pg_restore` se utiliza para formatos de archivo creados por `pg_dump` que no son simples scripts SQL, como `custom`, `directory` o `tar`.

---

# Diferencia entre SQL y formato `tar`

Los dos métodos utilizados permiten realizar copias de seguridad, pero funcionan de manera diferente.

| Característica | SQL        | `tar`                            |
| -------------- | ---------- | -------------------------------- |
| Creación       | `pg_dump`  | `pg_dump -F t`                   |
| Restauración   | `psql`     | `pg_restore`                     |
| Formato        | Script SQL | Archivo de respaldo estructurado |
| Ejemplo        | `.sql`     | `.tar`                           |

---

# Problema con `SERIAL` después de importar datos

Una situación importante aparece cuando una tabla utiliza `SERIAL` y posteriormente se importan registros que contienen valores explícitos para la columna `id`.

Primero se puede reconstruir la tabla:

```sql
DROP TABLE IF EXISTS customers;

CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(50)
);
```

Después se importa el dataset:

```text
\COPY customers
FROM '/home/camper/postgresdata/customers.csv'
DELIMITER ',' CSV HEADER;
```

Los registros importados pueden contener valores específicos para `id`.

Esto puede provocar que la secuencia asociada a `SERIAL` no quede sincronizada con el valor máximo existente.

Por ejemplo, si el último registro importado tiene:

```text
id = 50
```

pero la secuencia todavía considera que su siguiente valor es menor, un nuevo `INSERT` puede intentar utilizar un identificador que ya existe.

---

# Sincronizar la secuencia

Para sincronizar la secuencia con el último identificador existente:

```sql
SELECT SETVAL(
    pg_get_serial_sequence('customers', 'id'),
    (SELECT MAX(id) FROM customers)
);
```

### ¿Qué hace?

`pg_get_serial_sequence()` obtiene el nombre de la secuencia asociada a la columna `id`.

```sql
pg_get_serial_sequence('customers', 'id')
```

Después:

```sql
SELECT MAX(id) FROM customers
```

obtiene el identificador más alto actualmente almacenado.

Finalmente, `setval()` establece la secuencia utilizando ese valor.

De esta manera, los siguientes registros generados automáticamente pueden continuar a partir del último identificador utilizado.

---

# Insertar nuevos registros

Una vez sincronizada la secuencia, se pueden insertar nuevos registros:

```sql
INSERT INTO customers(first_name, last_name, email) 
VALUES
('Lana', 'Lang', 'llang@gmail.com'),
('Clark', 'Kent', 'ckent@gmail.com'),
('Jhon', 'Kent', 'jkent@gmail.com'),
('Camila', 'Cabello', 'ccabello@gmail.com');
```

Como `id` no se proporciona en el `INSERT`, PostgreSQL utiliza la secuencia asociada a la columna `SERIAL`.

---

# Evitar conflictos con `ON CONFLICT`

Si se intenta insertar un registro cuyo correo electrónico ya existe y existe una restricción `UNIQUE`, PostgreSQL puede generar un conflicto.

Una forma de ignorar el registro cuando exista un conflicto es:

```sql
INSERT INTO customers(first_name, last_name, email) 
VALUES
('Juan', 'Kent', 'jkent@gmail.com')
ON CONFLICT(email) DO NOTHING;
```

En este caso, si `email` ya está registrado, PostgreSQL no inserta el nuevo registro.

---

# Restricción `UNIQUE`

Para garantizar que los correos electrónicos no se repitan:

```sql
ALTER TABLE customers
ADD CONSTRAINT U_email UNIQUE (email);
```

La restricción garantiza que no existan dos registros con el mismo correo electrónico.

> [!IMPORTANT]
> `ON CONFLICT(email)` necesita una restricción o índice de unicidad compatible con la columna utilizada para detectar el conflicto.

---

# Consultar los datos importados

Para consultar los primeros registros según su identificador:

```sql
SELECT *
FROM customers
WHERE id < 51
ORDER BY id DESC
LIMIT 10;
```

La consulta:

* filtra los registros cuyo `id` sea menor que `51`;
* ordena los resultados de forma descendente;
* muestra únicamente los primeros 10 registros.

También se pueden consultar directamente los datos de la segunda tabla:

```sql
SELECT *
FROM customers_add;
```

---

# Actualización utilizando otra tabla

PostgreSQL permite actualizar una tabla utilizando información proveniente de otra tabla mediante `UPDATE ... FROM`.

```sql
UPDATE customers c
SET email = ca.email
FROM customers_add ca
WHERE c.id = ca.id;
```

En este caso:

* `customers` es la tabla que se modifica.
* `customers_add` proporciona los nuevos datos.
* `c.id = ca.id` relaciona ambas tablas.

Este mecanismo permite realizar actualizaciones masivas utilizando información existente en otra tabla.

---

# `UPDATE ... RETURNING`

PostgreSQL permite devolver los registros modificados mediante `RETURNING`.

```sql
UPDATE customers
SET email = 'john.micheal@gmail.com'
WHERE id = 1
RETURNING first_name, email;
```

Además de realizar la actualización, la consulta devuelve los valores solicitados del registro afectado.

Esto resulta útil cuando se necesita comprobar inmediatamente qué datos fueron modificados.

---

# Uso de `RETURNING` dentro de un bloque `DO`

También es posible almacenar el resultado de `RETURNING` dentro de una variable.

```sql
DO $$
DECLARE
    new_email VARCHAR(50);
BEGIN
    UPDATE customers
    SET email = 'john.micheal@gmail.com'
    WHERE id = 1
    RETURNING email INTO new_email;

    RAISE NOTICE 'email: %', new_email;
END $$;
```

La variable `new_email` recibe el valor devuelto por `RETURNING`.

> [!NOTE]
> En un bloque `DO`, utilizar `RAISE NOTICE` permite mostrar mensajes en el cliente `psql`. Un `SELECT` dentro de un bloque procedural no funciona como una consulta normal para devolver directamente un resultado al cliente.

---

# Base de datos de ejemplo: `Tienda`

Para continuar practicando operaciones con datos relacionados se crea una nueva base de datos:

```sql
CREATE DATABASE Tienda;
```

Después:

```text
\c Tienda
```

---

# Creación de `Productos`

```sql
CREATE TABLE Productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(120),
    precio NUMERIC(8, 2),
    stock INT
);
```

La tabla almacena:

* identificador del producto;
* nombre;
* precio;
* cantidad disponible en inventario.

---

# Creación de `Ventas`

```sql
CREATE TABLE Ventas (
    id SERIAL PRIMARY KEY,
    producto_id INT NOT NULL,
    cantidad INT,
    fecha_venta DATE
);
```

`producto_id` representa el identificador del producto relacionado con la venta.

En este ejercicio se utiliza como referencia lógica, aunque la definición original no agrega una `FOREIGN KEY`.

Una relación explícita podría definirse mediante:

```sql
ALTER TABLE Ventas
ADD CONSTRAINT fk_ventas_productos
FOREIGN KEY (producto_id)
REFERENCES Productos(id);
```

---

# Inserción de productos

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

# Inserción de ventas

Las ventas se relacionan con los productos mediante `producto_id`.

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

# Eliminación condicionada de productos

Se puede utilizar una subconsulta para identificar productos que no aparecen en ninguna venta:

```sql
DELETE FROM Productos
WHERE id NOT IN (
    SELECT producto_id
    FROM Ventas
)
AND stock = 0;
```

La condición elimina productos que:

1. no aparecen en `Ventas`;
2. tienen un `stock` igual a `0`.

> [!IMPORTANT]
> La condición `stock = 0` evita eliminar productos que todavía tengan unidades disponibles.

---

# Limpieza de datos duplicados

Los datasets reales pueden contener registros repetidos. PostgreSQL permite utilizar funciones de ventana para identificar duplicados.

Primero se crea una tabla para trabajar con datos sintéticos:

```sql
DROP TABLE IF EXISTS datos_fake;

CREATE TABLE IF NOT EXISTS datos_fake(
    id SERIAL PRIMARY KEY,
    codigo CHAR(3),
    nombre VARCHAR(30),
    apellido VARCHAR(30),
    edad INT
);
```

Después se insertan registros, incluyendo valores duplicados:

```sql
INSERT INTO datos_fake(codigo, nombre, apellido, edad) VALUES
('001', 'Patricia', 'Fernandez', 40),
('002', 'Armando', 'Benedetti', 38),
('001', 'Patricia', 'Fernandez', 40),
('003', 'Kevin', 'Garcia', 42),
('004', 'Jhon', 'Cuevas', 23),
('005', 'Luna', 'Herrera', 40),
('002', 'Armando', 'Benedetti', 38),
('001', 'Patricia', 'Fernandez', 40),
('002', 'Armando', 'Benedetti', 38),
('001', 'Patricia', 'Fernandez', 40);
```

---

# Identificar duplicados con `ROW_NUMBER()`

Para identificar registros repetidos se utiliza una función de ventana:

```sql
WITH duplicados AS (
    SELECT
        id,
        ROW_NUMBER() OVER (
            PARTITION BY codigo
            ORDER BY id
        ) AS row_num
    FROM datos_fake
)
DELETE FROM datos_fake
WHERE id IN (
    SELECT id
    FROM duplicados
    WHERE row_num > 1
);
```

### Funcionamiento

La expresión:

```sql
ROW_NUMBER() OVER (
    PARTITION BY codigo
    ORDER BY id
)
```

asigna un número consecutivo a cada registro dentro de cada grupo de `codigo`.

Por ejemplo:

```text
codigo | row_num
-------|--------
001    | 1
001    | 2
001    | 3
001    | 4
002    | 1
002    | 2
002    | 3
```

El primer registro de cada código recibe:

```text
row_num = 1
```

Los registros posteriores:

```text
row_num > 1
```

son considerados duplicados y pueden eliminarse.

> [!WARNING]
> En este ejercicio los duplicados se determinan únicamente utilizando `codigo`. Si dos personas diferentes pudieran compartir el mismo código, esta estrategia eliminaría registros válidos. La definición de un duplicado debe basarse en las columnas que realmente identifiquen un registro repetido en el dataset.

---

# Glosario

| Término                        | Descripción                                                                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Dataset**                    | Conjunto de datos utilizado para almacenar, procesar o analizar información.                                                    |
| **CSV**                        | Formato de archivo de texto donde los datos suelen organizarse en columnas separadas por un delimitador.                        |
| **`COPY`**                     | Comando de PostgreSQL utilizado para importar o exportar datos entre tablas y archivos desde la perspectiva del servidor.       |
| **`\COPY`**                    | Comando del cliente `psql` que permite importar o exportar archivos desde el equipo donde se ejecuta el cliente.                |
| **`DELIMITER`**                | Define el carácter utilizado para separar las columnas de un archivo.                                                           |
| **`HEADER`**                   | Indica que la primera fila del archivo contiene nombres de columnas y no datos.                                                 |
| **`pg_dump`**                  | Herramienta de PostgreSQL utilizada para crear copias de seguridad.                                                             |
| **`psql`**                     | Cliente de línea de comandos utilizado para conectarse y trabajar con PostgreSQL.                                               |
| **`pg_restore`**               | Herramienta utilizada para restaurar copias generadas por `pg_dump` en formatos estructurados como `tar` o `custom`.            |
| **Backup**                     | Copia de seguridad utilizada para conservar y posteriormente recuperar datos.                                                   |
| **`SERIAL`**                   | Mecanismo tradicional de PostgreSQL que utiliza una secuencia para generar valores enteros automáticamente.                     |
| **Secuencia**                  | Objeto de PostgreSQL que genera valores numéricos consecutivos, utilizado frecuentemente para identificadores.                  |
| **`SETVAL()`**                 | Función utilizada para establecer el valor actual de una secuencia.                                                             |
| **`pg_get_serial_sequence()`** | Función que obtiene la secuencia asociada a una columna definida con `SERIAL`.                                                  |
| **`ON CONFLICT`**              | Construcción de PostgreSQL utilizada para definir qué hacer cuando una operación de inserción produce un conflicto de unicidad. |
| **`UNIQUE`**                   | Restricción que evita valores duplicados en una columna o conjunto de columnas.                                                 |
| **`RETURNING`**                | Cláusula que permite devolver los registros afectados por operaciones como `INSERT`, `UPDATE` o `DELETE`.                       |
| **`UPDATE ... FROM`**          | Sintaxis de PostgreSQL que permite actualizar una tabla utilizando información proveniente de otra tabla.                       |
| **`DO`**                       | Instrucción utilizada para ejecutar un bloque de código procedural anónimo en PostgreSQL.                                       |
| **`PL/pgSQL`**                 | Lenguaje procedural utilizado por PostgreSQL para crear funciones y bloques de código.                                          |
| **`RAISE NOTICE`**             | Instrucción de PL/pgSQL utilizada para mostrar mensajes informativos.                                                           |
| **`DELETE`**                   | Instrucción SQL utilizada para eliminar registros de una tabla.                                                                 |
| **Subconsulta**                | Consulta SQL utilizada dentro de otra consulta.                                                                                 |
| **`WITH`**                     | Cláusula utilizada para definir expresiones de tabla comunes o CTE.                                                             |
| **CTE**                        | Expresión de tabla común definida mediante `WITH`, utilizada para organizar consultas complejas.                                |
| **`ROW_NUMBER()`**             | Función de ventana que asigna un número consecutivo a cada fila dentro de un conjunto.                                          |
| **`PARTITION BY`**             | Divide los registros en grupos para que una función de ventana se aplique independientemente en cada grupo.                     |
| **Función de ventana**         | Función que calcula valores sobre un conjunto de filas relacionadas sin agruparlas en una sola fila.                            |
| **Integridad de datos**        | Conjunto de mecanismos utilizados para mantener los datos correctos, consistentes y válidos.                                    |
| **Importación**                | Proceso de cargar datos externos dentro de una base de datos.                                                                   |
| **Restauración**               | Proceso de recuperar estructuras y datos a partir de una copia de seguridad.                                                    |

---

# Resumen

En esta clase se trabajó principalmente la administración e importación de datasets en PostgreSQL.

Los principales puntos estudiados fueron:

1. Comprender las alternativas disponibles para importar datasets.
2. Crear tablas compatibles con archivos CSV.
3. Importar información utilizando `\COPY`.
4. Comprender la diferencia entre `COPY` y `\COPY`.
5. Crear copias de seguridad mediante `pg_dump`.
6. Restaurar copias en formato SQL utilizando `psql`.
7. Crear copias en formato `tar`.
8. Restaurar archivos `tar` mediante `pg_restore`.
9. Identificar problemas de sincronización entre datos importados y secuencias `SERIAL`.
10. Sincronizar una secuencia utilizando `SETVAL()`.
11. Evitar registros duplicados mediante restricciones `UNIQUE`.
12. Utilizar `ON CONFLICT ... DO NOTHING`.
13. Actualizar registros utilizando información de otra tabla mediante `UPDATE ... FROM`.
14. Recuperar los datos modificados mediante `RETURNING`.
15. Utilizar bloques `DO` y variables de PL/pgSQL.
16. Crear tablas relacionadas para trabajar con productos y ventas.
17. Realizar eliminaciones condicionadas mediante subconsultas.
18. Identificar y eliminar registros duplicados utilizando `ROW_NUMBER()`.
19. Utilizar `WITH` para organizar operaciones de limpieza de datos.

La idea principal de esta clase es que trabajar con una base de datos no consiste únicamente en insertar información. También es necesario saber **importar datasets, realizar respaldos, restaurar información, mantener las secuencias, controlar duplicados y limpiar datos antes de utilizarlos**.
