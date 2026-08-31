# Operadores y tipos de datos en PostgreSQL

## 1. Operadores aritméticos

PostgreSQL proporciona los operadores aritméticos tradicionales y algunos operadores adicionales para realizar cálculos.

| Operador | Significado    |
| -------- | -------------- |
| `+`      | Suma           |
| `-`      | Resta          |
| `*`      | Multiplicación |
| `/`      | División       |
| `%`      | Módulo o resto |
| `^`      | Exponenciación |
| `\|/`    | Raíz cuadrada  |
| `\|\|/`  | Raíz cúbica    |
| `@`      | Valor absoluto |

También existe la función `FACTORIAL()` para calcular el factorial de un número.

### Ejemplos

```sql
SELECT 1 + 2;

-- Potencia
SELECT 25 ^ 3;

-- Factorial
SELECT FACTORIAL(3);

-- Valor absoluto
SELECT @ -25;
```

> [!NOTE]
> `FACTORIAL()` es una función de PostgreSQL. También existen operadores factoriales como `!` y `!!` en determinados contextos de PostgreSQL.

---

# 2. Operadores de cadenas y expresiones regulares

PostgreSQL incluye operadores que permiten trabajar directamente con cadenas de texto y expresiones regulares.

| Operador | Significado                                                                  |
| -------- | ---------------------------------------------------------------------------- |
| `\|\|`   | Concatenación de cadenas                                                     |
| `~`      | Coincidencia con expresión regular, distingue mayúsculas y minúsculas        |
| `~*`     | Coincidencia con expresión regular sin distinguir mayúsculas y minúsculas    |
| `!~`     | No coincidencia con expresión regular, distingue mayúsculas y minúsculas     |
| `!~*`    | No coincidencia con expresión regular sin distinguir mayúsculas y minúsculas |

La concatenación permite unir diferentes cadenas:

```sql
SELECT 'Hola' || ' - ' || 'Campers';
```

### Expresiones regulares

Las expresiones regulares permiten buscar patrones dentro de una cadena.

Son especialmente útiles para validar o identificar formatos de texto, por ejemplo:

* Correos electrónicos.
* Códigos.
* Números telefónicos.
* Contraseñas.
* Patrones específicos de texto.

Ejemplo:

```sql
SELECT 'Campuslands'
WHERE 'Campuslands' ~ '^Campus';
```

La expresión:

```text
^Campus
```

indica que la cadena debe comenzar con `Campus`.

> [!IMPORTANT]
> Una expresión regular permite comprobar que un texto cumple determinado patrón, pero una validación de contraseña segura normalmente requiere reglas adicionales, como longitud mínima, caracteres permitidos y políticas de seguridad.

---

# 3. Funciones para trabajar con texto

PostgreSQL proporciona funciones para consultar y transformar cadenas.

### Longitud

`LENGTH()` permite obtener la cantidad de caracteres de una cadena.

```sql
SELECT first_name, LENGTH(first_name)
FROM customers;
```

### Convertir a minúsculas

```sql
SELECT first_name, LOWER(first_name)
FROM customers;
```

### Convertir a mayúsculas

```sql
SELECT first_name, UPPER(first_name)
FROM customers;
```

### Eliminar caracteres de la izquierda

`LTRIM()` elimina determinados caracteres desde el comienzo de una cadena.

```sql
SELECT first_name, LTRIM(first_name, 'B')
FROM customers;

SELECT first_name, LTRIM(first_name, 'S')
FROM customers;
```

> [!NOTE]
> `LTRIM()` no elimina necesariamente una única letra. El segundo argumento indica qué caracteres deben eliminarse desde el inicio mientras coincidan.

---

# 4. SUBSTRING

`SUBSTRING()` permite obtener una parte de una cadena.

Existen diferentes formas de utilizarla.

### Sintaxis

```text
SUBSTRING(cadena, inicio, cantidad)
```

Ejemplo:

```sql
SELECT SUBSTRING('HOLA CAMPERS', 2, 5);
```

También puede utilizarse la sintaxis:

```text
SUBSTRING(cadena FROM inicio FOR cantidad)
```

Por ejemplo:

```sql
SELECT SUBSTRING('HOLA CAMPERS' FROM 2 FOR 5);
```

> [!NOTE]
> El tercer parámetro representa la **cantidad de caracteres** que se desean obtener, no la posición final.

---

# 5. Tipos de datos de red

PostgreSQL incluye tipos de datos especializados para almacenar direcciones IP y redes.

Los principales son:

* `INET`: almacena una dirección IPv4 o IPv6, pudiendo incluir una máscara de red.
* `CIDR`: representa una red o subred en formato CIDR.

Estos tipos son útiles para aplicaciones relacionadas con:

* Administración de redes.
* Seguridad informática.
* Segmentación de redes.
* Registro de direcciones IP.
* Control de acceso.

Ejemplo:

```sql
CREATE TABLE redes (
    direccion_ip INET,
    subred CIDR
);
```

---

# 6. Arrays

Los `ARRAY` permiten almacenar múltiples valores del mismo tipo dentro de una columna.

Pueden ser útiles cuando un registro necesita almacenar una colección de valores relacionados y no resulta necesario crear una tabla independiente para ellos.

Por ejemplo, una tabla de estudiantes podría almacenar varios teléfonos:

```sql
CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    telefonos VARCHAR(15)[]
);
```

Posteriormente se pueden almacenar varios valores:

```sql
INSERT INTO estudiantes (nombre, telefonos)
VALUES (
    'Carlos',
    ARRAY['5555-1111', '5555-2222']
);
```

> [!WARNING]
> Los arrays no deben utilizarse automáticamente para reemplazar relaciones entre tablas. Cuando los elementos necesitan tener propiedades propias, relacionarse con otros registros o consultarse individualmente con frecuencia, normalmente resulta más apropiado utilizar una tabla relacionada.

---

# 7. Tipos de datos compuestos

Los tipos compuestos permiten definir estructuras formadas por varios campos.

Primero se puede crear un tipo compuesto:

```sql
CREATE TYPE direccion AS (
    calle VARCHAR(100),
    ciudad VARCHAR(100),
    codigo_postal VARCHAR(10)
);
```

Posteriormente puede utilizarse como tipo de una columna:

```sql
CREATE TABLE personas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    domicilio direccion
);
```

Esto permite almacenar un conjunto de datos relacionados como una unidad.

> [!IMPORTANT]
> Un tipo compuesto no funciona como una tabla independiente. Es un tipo de dato definido por el usuario que puede utilizarse dentro de otras estructuras.

---

# 8. Tipos de datos JSON

PostgreSQL soporta los tipos `JSON` y `JSONB`.

Estos tipos permiten almacenar información estructurada en formato JSON.

Son útiles cuando los datos poseen una estructura flexible, por ejemplo:

* Configuraciones.
* Opciones dinámicas.
* Metadatos.
* Información recibida desde aplicaciones web.
* Datos cuyo esquema puede variar.

Ejemplo:

```sql
CREATE TABLE configuraciones (
    id SERIAL PRIMARY KEY,
    configuracion JSON
);
```

PostgreSQL también proporciona:

```sql
JSONB
```

`JSONB` almacena los datos en una representación binaria optimizada y proporciona funcionalidades eficientes para consultar e indexar el contenido.

> [!NOTE]
> `JSON` conserva el texto JSON original, mientras que `JSONB` almacena una representación binaria que PostgreSQL puede procesar de manera más eficiente para muchas operaciones.

---

# 9. Tipo de datos XML

PostgreSQL también proporciona el tipo `XML`, utilizado para almacenar documentos XML.

XML puede ser útil cuando se trabaja con:

* Sistemas empresariales.
* Intercambio de información entre aplicaciones.
* Sistemas que utilizan estándares XML.
* Datos con estructuras jerárquicas.

Ejemplo:

```sql
CREATE TABLE documentos (
    id SERIAL PRIMARY KEY,
    documento XML
);
```

---

# 10. Casos de cuidado con JSON y XML

Aunque `JSON`, `JSONB` y `XML` proporcionan flexibilidad, no siempre son la mejor opción para almacenar toda la información de una aplicación.

### Complejidad de las consultas

Extraer y modificar información dentro de estructuras JSON o XML puede resultar más complejo que trabajar con columnas relacionales tradicionales.

### Integridad de los datos

Cuando una estructura flexible permite diferentes formatos de información, puede ser más difícil garantizar que todos los registros mantengan la misma estructura.

### Rendimiento

El rendimiento depende de cómo se almacenen, consulten e indexen los datos.

### Diseño de la base de datos

Si una información tiene una estructura estable y se consulta frecuentemente, normalmente resulta más apropiado utilizar columnas y tablas relacionales.

> [!IMPORTANT]
> La flexibilidad de JSON o XML no significa que deban utilizarse para reemplazar el modelo relacional. Su utilidad depende del tipo de información y de las consultas que necesita realizar la aplicación.

---

# 11. Administración de usuarios y permisos

PostgreSQL permite crear usuarios y controlar las operaciones que pueden realizar sobre los objetos de la base de datos.

### Crear un usuario

```sql
CREATE USER analista
WITH PASSWORD '123456';
```

> [!WARNING]
> En entornos reales no se recomienda utilizar contraseñas simples como la mostrada en el ejemplo. El usuario y la contraseña del ejercicio se utilizan únicamente con fines educativos.

---

## 11.1 Otorgar permisos

Para permitir que un usuario consulte una tabla:

```sql
GRANT SELECT
ON customers
TO analista;
```

También se pueden otorgar varios permisos:

```sql
GRANT SELECT, INSERT, UPDATE
ON customers_add
TO analista;
```

Los permisos principales utilizados en estos ejemplos son:

* `SELECT`: consultar datos.
* `INSERT`: insertar datos.
* `UPDATE`: modificar datos.
* `DELETE`: eliminar datos.

---

## 11.2 Revocar permisos

Para retirar un permiso:

```sql
REVOKE SELECT
ON customers
FROM analista;
```

Esto elimina el permiso `SELECT` previamente otorgado sobre `customers`.

---

## 11.3 Eliminar un usuario

```sql
DROP USER analista;
```

> [!WARNING]
> Un usuario no puede eliminarse si todavía posee objetos o dependencias que impidan su eliminación. En esos casos es necesario revisar sus privilegios y objetos asociados.

---

# 12. Revisión de tablas utilizadas anteriormente

Durante esta clase se reutilizan conceptos y tablas trabajados anteriormente, especialmente:

* `customers`
* `customers_add`

Esto permite aplicar los operadores, funciones de texto, usuarios y permisos sobre datos ya existentes.

---

# Glosario

| Término               | Definición                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Operador**          | Símbolo o construcción utilizada para realizar una operación sobre uno o más valores.                                   |
| **Exponenciación**    | Operación matemática que eleva un número a una potencia.                                                                |
| **Valor absoluto**    | Valor de un número sin considerar su signo.                                                                             |
| **Factorial**         | Producto de todos los números enteros positivos desde 1 hasta un número determinado.                                    |
| **Concatenación**     | Unión de dos o más cadenas de texto en una sola cadena.                                                                 |
| **Expresión regular** | Patrón utilizado para buscar o validar coincidencias dentro de cadenas de texto.                                        |
| **ARRAY**             | Tipo de dato que permite almacenar múltiples valores del mismo tipo en una columna.                                     |
| **Tipo compuesto**    | Tipo de dato definido por el usuario que contiene varios campos.                                                        |
| **JSON**              | Formato de datos estructurado utilizado para representar información mediante pares clave-valor y estructuras anidadas. |
| **JSONB**             | Representación binaria de JSON utilizada por PostgreSQL para almacenar y procesar datos JSON de forma optimizada.       |
| **XML**               | Lenguaje de marcado utilizado para representar información estructurada y jerárquica.                                   |
| **INET**              | Tipo de PostgreSQL utilizado para almacenar direcciones IP.                                                             |
| **CIDR**              | Tipo utilizado para representar redes y subredes mediante notación CIDR.                                                |
| **Usuario**           | Rol de PostgreSQL utilizado para autenticar y controlar el acceso al sistema de base de datos.                          |
| **Permiso**           | Autorización que determina qué operaciones puede realizar un usuario sobre un objeto.                                   |
| **GRANT**             | Comando utilizado para otorgar privilegios a usuarios o roles.                                                          |
| **REVOKE**            | Comando utilizado para retirar privilegios previamente otorgados.                                                       |
| **SELECT**            | Operación utilizada para consultar información.                                                                         |
| **INSERT**            | Operación utilizada para insertar nuevos registros.                                                                     |
| **UPDATE**            | Operación utilizada para modificar registros existentes.                                                                |
| **DROP USER**         | Instrucción utilizada para eliminar un usuario o rol de PostgreSQL.                                                     |
| **SUBSTRING**         | Función utilizada para extraer una parte de una cadena de texto.                                                        |
| **LENGTH**            | Función que devuelve la longitud de una cadena.                                                                         |
| **LOWER**             | Función que convierte una cadena a minúsculas.                                                                          |
| **UPPER**             | Función que convierte una cadena a mayúsculas.                                                                          |
| **LTRIM**             | Función que elimina caracteres desde el inicio de una cadena.                                                           |

---

# Resumen

En esta clase se estudiaron diferentes características de PostgreSQL relacionadas con operadores, manipulación de texto, tipos de datos especializados y administración de usuarios.

Los principales puntos fueron:

1. Utilizar operadores aritméticos adicionales de PostgreSQL.
2. Trabajar con exponenciación, raíces, factoriales y valores absolutos.
3. Concatenar cadenas mediante `||`.
4. Utilizar expresiones regulares para buscar patrones.
5. Manipular texto mediante `LENGTH`, `LOWER`, `UPPER` y `LTRIM`.
6. Extraer partes de una cadena mediante `SUBSTRING`.
7. Trabajar con direcciones IP mediante `INET` y `CIDR`.
8. Utilizar arrays para almacenar colecciones de valores.
9. Crear tipos de datos compuestos.
10. Almacenar información estructurada mediante `JSON`, `JSONB` y `XML`.
11. Comprender los casos donde JSON o XML requieren mayor cuidado.
12. Crear usuarios mediante `CREATE USER`.
13. Otorgar permisos mediante `GRANT`.
14. Revocar permisos mediante `REVOKE`.
15. Eliminar usuarios mediante `DROP USER`.

La idea principal de esta clase es ampliar el uso de PostgreSQL más allá de las operaciones relacionales básicas, aprovechando sus operadores, funciones y tipos de datos especializados sin perder de vista el diseño adecuado de la base de datos.
