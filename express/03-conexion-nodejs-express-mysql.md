---
titulo: "Conexión de Node.js y Express con MySQL"
area: "express"
orden: 3
tags: ["express"]
---

# Conexión de Node.js y Express con MySQL

Esta lección muestra cómo conectar una aplicación de [Node.js](../conceptos/nodejs.md) con [Express](../conceptos/express.md) a una [base de datos](../conceptos/base-de-datos.md) [MySQL](../conceptos/mysql.md). Se explica la configuración de la conexión, cómo verificarla y cómo usarla desde una ruta. Para la comunicación se usa el controlador [mysql2](../conceptos/mysql2.md).

---

## 1. Objetivo

Al terminar esta lección, la aplicación podrá:

* Leer las credenciales de la base de datos desde un archivo `.env`, usando [variables de entorno](../conceptos/variable-de-entorno.md).
* Crear un [pool de conexiones](../conceptos/pool-de-conexiones.md) reutilizable.
* Verificar la conexión antes de iniciar el servidor.
* Ejecutar consultas SQL desde una ruta de Express de forma segura.

---

## 2. Requisitos

| Herramienta | Versión recomendada |
| --- | --- |
| Node.js | 18.11 o superior |
| MySQL Server | 8.0 o superior |
| Cliente visual (Workbench, DBeaver o phpMyAdmin) | Cualquiera |
| Postman, Thunder Client o curl | Cualquiera |

Para verificar las versiones instaladas:

```bash
node -v
mysql --version
```

---

## 3. Estructura del proyecto

```
ejercicios_clase/
├── config/
│   └── db.js                  ← Configuración de la conexión a MySQL
├── routes/
│   └── producto.routes.js     ← Ruta de ejemplo que usa la conexión
├── .env                       ← Credenciales (no subir a Git)
├── .gitignore
├── package.json
└── server.js                  ← Punto de entrada de la aplicación
```

La carpeta de configuración debe llamarse exactamente `config`, sin caracteres adicionales.

---

## 4. Instalación de dependencias

Desde la raíz del proyecto:

```bash
npm init -y
npm install express mysql2 dotenv
```

* `express`: crea el servidor y las rutas.
* `mysql2`: cliente de MySQL para Node.js. La versión `mysql2/promise` permite usar `async/await`.
* `dotenv`: carga las variables del archivo `.env` en `process.env`.

### Configuración del `package.json`

El proyecto usa `import` y `export`, así que debe indicar que trabaja con módulos ES. Agrega `"type": "module"`:

```json
{
  "name": "ejercicios_clase",
  "version": "1.0.0",
  "main": "server.js",
  "type": "module",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "dotenv": "^18.0.7",
    "express": "^5.3.0",
    "mysql2": "^3.24.6"
  }
}
```

Sin `"type": "module"`, aparece el error `SyntaxError: Cannot use import statement outside a module`.

---

## 5. Preparar la base de datos

Antes de conectar, la base de datos y la [tabla](../conceptos/tabla.md) deben existir. Ejecuta este script en MySQL:

```sql
CREATE DATABASE IF NOT EXISTS ejercicios_clase
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE ejercicios_clase;

CREATE TABLE IF NOT EXISTS productos (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  codigo      VARCHAR(20)   NOT NULL UNIQUE,
  nombre      VARCHAR(100)  NOT NULL,
  descripcion TEXT          NULL,
  precio      DECIMAL(10,2) NOT NULL,
  activo      TINYINT(1)    NOT NULL DEFAULT 1,
  creado_en   TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO productos (codigo, nombre, descripcion, precio) VALUES
  ('P001', 'Teclado mecánico', 'Teclado USB con retroiluminación', 350.00),
  ('P002', 'Mouse inalámbrico', 'Mouse de 2.4 GHz', 120.50);
```

Para confirmar que la tabla tiene datos:

```sql
SELECT * FROM productos;
```

---

## 6. Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
SERVER_PORT=3000

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=ejercicios_clase
```

Crea también un `.gitignore` para que las credenciales y las dependencias no se suban al repositorio:

```gitignore
node_modules/
.env
```

Las credenciales nunca deben escribirse directamente en el código.

---

## 7. Configuración de la conexión

Archivo `config/db.js`:

```javascript
import 'dotenv/config';
import mysql from 'mysql2/promise';

const pool = mysql.createPool({
    host: process.env.DB_HOST,
    port: Number(process.env.DB_PORT) || 3306,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

export default pool;
```

### ¿Qué es un pool de conexiones?

Abrir una conexión a MySQL es un proceso costoso. El [pool](../conceptos/pool-de-conexiones.md) mantiene varias conexiones abiertas y las reutiliza:

1. Llega una petición y el pool entrega una conexión libre.
2. La consulta termina y la conexión regresa al pool.
3. Si las 10 conexiones están ocupadas, la siguiente petición espera en la cola.

Se crea un solo pool al iniciar la aplicación, y todas las rutas lo comparten. No se debe llamar a `createConnection` dentro de cada ruta.

### Parámetros principales

| Parámetro | Descripción |
| --- | --- |
| `host` | Dirección del servidor MySQL. Usa `localhost` si MySQL está en tu equipo |
| `port` | Puerto de MySQL. Por defecto es `3306` |
| `user` y `password` | Credenciales del usuario de la base de datos |
| `database` | Base de datos a utilizar |
| `connectionLimit` | Máximo de conexiones simultáneas |
| `waitForConnections` | Si es `true`, las peticiones esperan una conexión libre en lugar de fallar |
| `queueLimit` | Máximo de peticiones en espera. `0` significa sin límite |

---

## 8. Verificar la conexión al iniciar: `server.js`

Archivo `server.js`:

```javascript
import express from 'express';
import 'dotenv/config';

import pool from './config/db.js';
import productosRouter from './routes/producto.routes.js';

const server = express();
const PORT = process.env.SERVER_PORT || 3000;

server.use(express.json());

server.use('/productos', productosRouter);

server.use((req, res) => {
    res.status(404).json({ error: 'Ruta no encontrada' });
});

server.use((err, req, res, next) => {
    console.error('Error interno:', err);
    res.status(500).json({ error: 'Error interno del servidor' });
});

async function iniciar() {
    try {
        const conexion = await pool.getConnection();
        console.log('Conexión a MySQL establecida');
        conexion.release();

        server.listen(PORT, () => {
            console.log(`Servidor corriendo en http://localhost:${PORT}`);
        });
    } catch (error) {
        console.error('No se pudo conectar a MySQL:', error.message);
        process.exit(1);
    }
}

iniciar();
```

### Puntos importantes

* `pool.getConnection()` pide una conexión real a MySQL. Si las credenciales son incorrectas o MySQL no está activo, el error aparece al arrancar, no cuando alguien hace una petición.
* `conexion.release()` devuelve la conexión al pool. Si se omite, la conexión queda ocupada.
* El manejador de errores necesita cuatro parámetros `(err, req, res, next)`. Express lo reconoce como manejador de errores por su firma.

---

## 9. Usar la conexión en una ruta

Archivo `routes/producto.routes.js`:

```javascript
import { Router } from 'express';
import pool from '../config/db.js';

const productosRouter = Router();

// GET /productos → obtener todos los productos
productosRouter.get('/', async (req, res, next) => {
    try {
        const [rows] = await pool.query(
            'SELECT id, codigo, nombre, descripcion, precio, activo FROM productos'
        );
        res.json(rows);
    } catch (error) {
        next(error);
    }
});

// GET /productos/:id → obtener un producto por id
productosRouter.get('/:id', async (req, res, next) => {
    try {
        const [rows] = await pool.execute(
            'SELECT id, codigo, nombre, descripcion, precio, activo FROM productos WHERE id = ?',
            [req.params.id]
        );

        if (rows.length === 0) {
            return res.status(404).json({ error: 'Producto no encontrado' });
        }

        res.json(rows[0]);
    } catch (error) {
        next(error);
    }
});

// POST /productos → crear un producto
productosRouter.post('/', async (req, res, next) => {
    try {
        const { codigo, nombre, descripcion = null, precio, activo = 1 } = req.body;

        if (!codigo || !nombre || precio === undefined) {
            return res.status(400).json({ error: 'codigo, nombre y precio son obligatorios' });
        }

        const [result] = await pool.execute(
            'INSERT INTO productos (codigo, nombre, descripcion, precio, activo) VALUES (?, ?, ?, ?, ?)',
            [codigo, nombre, descripcion, precio, activo]
        );

        res.status(201).json({ id: result.insertId, mensaje: 'Producto creado correctamente' });
    } catch (error) {
        next(error);
    }
});

export default productosRouter;
```

### Cómo leer el resultado de una consulta

Cada consulta devuelve un arreglo de dos elementos. Con `const [rows] = ...` se toma el primero:

| Operación | Qué devuelve mysql2 | Qué usar |
| --- | --- | --- |
| `SELECT` | Arreglo de filas | `rows` |
| `INSERT` | Objeto con `insertId` | `result.insertId` |
| `UPDATE` o `DELETE` | Objeto con `affectedRows` | `result.affectedRows` |

### `query` frente a `execute`

* `pool.query(sql)` ejecuta el texto tal cual. Úsalo solo cuando la consulta no recibe datos del usuario.
* `pool.execute(sql, valores)` usa [consultas preparadas](../conceptos/prepared-statement.md). Los `?` se reemplazan de forma segura. Úsalo siempre que haya datos variables.

Nunca construyas una consulta concatenando datos del usuario, porque abre la puerta a una [inyección SQL](../conceptos/inyeccion-sql.md):

```javascript
// INCORRECTO: vulnerable a inyección SQL
const [rows] = await pool.query(`SELECT * FROM productos WHERE id = ${req.params.id}`);

// CORRECTO: consulta preparada
const [rows] = await pool.execute('SELECT * FROM productos WHERE id = ?', [req.params.id]);
```

---

## 10. Pruebas

Inicia el servidor:

```bash
node server.js
```

Consola esperada:

```
Conexión a MySQL establecida
Servidor corriendo en http://localhost:3000
```

Listar productos:

```bash
curl http://localhost:3000/productos
```

Respuesta esperada (`200 OK`):

```json
[
  { "id": 1, "codigo": "P001", "nombre": "Teclado mecánico", "descripcion": "Teclado USB con retroiluminación", "precio": "350.00", "activo": 1 },
  { "id": 2, "codigo": "P002", "nombre": "Mouse inalámbrico", "descripcion": "Mouse de 2.4 GHz", "precio": "120.50", "activo": 1 }
]
```

Obtener un producto por id:

```bash
curl http://localhost:3000/productos/1
```

Crear un producto:

```bash
curl -X POST http://localhost:3000/productos \
  -H "Content-Type: application/json" \
  -d '{"codigo":"P003","nombre":"Monitor 24\"","descripcion":"Full HD","precio":1200}'
```

Respuesta esperada (`201 Created`):

```json
{ "id": 3, "mensaje": "Producto creado correctamente" }
```

Si el id no existe, la respuesta es `404 Not Found` con `{ "error": "Producto no encontrado" }`.

---

## 11. Errores comunes

### Errores del proyecto

| Síntoma | Causa | Solución |
| --- | --- | --- |
| `SyntaxError: Cannot use import statement outside a module` | Falta `"type": "module"` en `package.json` | Agregar la línea |
| `Cannot find module '.../config/db.js'` | La carpeta tiene un nombre distinto, por ejemplo `config,/` | Renombrar la carpeta a `config` |
| `ERR_MODULE_NOT_FOUND` al importar una ruta | El nombre del archivo no coincide con el import | Revisar que el import tenga el mismo nombre que el archivo |
| Un error no devuelve `500` | El manejador de errores tiene tres parámetros | Usar `(err, req, res, next)` |

### Errores de conexión a MySQL

| Mensaje | Causa probable | Solución |
| --- | --- | --- |
| `ECONNREFUSED` | MySQL no está activo, o el puerto es incorrecto | Iniciar el servicio de MySQL y revisar `DB_PORT` |
| `ER_ACCESS_DENIED_ERROR` | Usuario o contraseña incorrectos | Revisar `DB_USER` y `DB_PASSWORD` en el `.env` |
| `ER_BAD_DB_ERROR` | La base de datos no existe | Ejecutar el script de la sección 5 o revisar `DB_NAME` |
| `ER_NO_SUCH_TABLE` | La tabla no fue creada | Verificar con `SHOW TABLES;` |
| `ER_BAD_FIELD_ERROR` | Una columna de la consulta no existe | Comparar los nombres de columnas con el script de creación |
| Host o usuario `undefined` | El `.env` no se cargó | Confirmar que el archivo se llama `.env` y está en la raíz del proyecto |

### Diagnóstico rápido

Si la aplicación no conecta, prueba las mismas credenciales directamente en MySQL:

```bash
mysql -h localhost -P 3306 -u root -p ejercicios_clase
```

Si ese comando falla, el problema está en MySQL o en las credenciales, no en el código de Node.js.

---

## 12. Flujo de una petición

```
Cliente (Postman o navegador)
        │  GET /productos
        ▼
server.js (Express)
        │  monta la ruta /productos
        ▼
routes/producto.routes.js
        │  pool.query o pool.execute
        ▼
config/db.js (pool de conexiones)
        │  toma una conexión libre
        ▼
MySQL (ejercicios_clase)
        │  devuelve filas
        ▼
Cliente recibe JSON
```

---

## Notas de apoyo

> [!TIP]
> Verifica la conexión con el mismo usuario y contraseña del `.env` antes de culpar al código. Si `mysql -u ... -p` falla, el problema está en MySQL.

> [!NOTE]
> La lección [Persistencia de datos con MySQL y Node.js](../nodejs/08-persistencia-con-mysql.md) usa `createConnection`, que abre una sola conexión. Esta lección usa `createPool`, que es la opción adecuada cuando una [API](../conceptos/api.md) atiende varias peticiones a la vez.

> [!WARNING]
> No subas el archivo `.env` al repositorio. Si una contraseña se publica, cámbiala en MySQL, aunque hayas borrado el archivo después.

> [!NOTE]
> En producción, el usuario de la aplicación debería tener solo los permisos que necesita, por ejemplo `SELECT`, `INSERT`, `UPDATE` y `DELETE` sobre `ejercicios_clase`. No se recomienda usar `root`.

> [!TIP]
> Si cambias el esquema de la base de datos, revisa que las consultas de las rutas coincidan con los nombres de las columnas.

---

## Conexiones

* [Introducción a Node.js con Express.js](01-introduccion-nodejs-expressjs.md): instalación, `package.json` y `dotenv`.
* [API, estados HTTP, parámetros, middlewares y routers en Express.js](02-api-http-middlewares-routers.md): cómo organizar las rutas en [routers](../conceptos/router.md) y leer `req.body` y `req.params`.
* [Persistencia de datos con MySQL y Node.js](../nodejs/08-persistencia-con-mysql.md): la versión con una conexión individual y un [CRUD](../conceptos/crud.md) en consola.
* [SQL](../conceptos/sql.md) y [Base de datos relacional](../conceptos/base-de-datos-relacional.md): el lenguaje y el modelo que usan las consultas de esta lección.
* [JSON](../conceptos/json.md): formato de los datos que se reciben y se devuelven en la API.

---

## Resumen

* Un pool de conexiones se crea una vez y lo comparten todas las rutas.
* `mysql2/promise` permite usar `async/await` con `pool.query` y `pool.execute`.
* Las credenciales se leen desde `.env`, y ese archivo nunca se sube al repositorio.
* `pool.execute` con `?` evita la inyección SQL. Nunca concatenes datos del usuario en una consulta.
* `getConnection` al arrancar confirma que la base de datos responde antes de aceptar peticiones.

<!-- auto:pie -->
---

**Navegación:** [← Anterior: API, estados HTTP, parámetros, middlewares y routers en Express.js](02-api-http-middlewares-routers.md) · [Índice de Express](indice.md)

**Conceptos de esta lección:** [MySQL](../conceptos/mysql.md), [Base de Datos](../conceptos/base-de-datos.md), [Node.js](../conceptos/nodejs.md), [Express.js](../conceptos/express.md), [Pool de conexiones](../conceptos/pool-de-conexiones.md), [Tabla (Base de Datos)](../conceptos/tabla.md), [API (Interfaz de programación de aplicaciones)](../conceptos/api.md), [mysql2](../conceptos/mysql2.md), [Variable de entorno](../conceptos/variable-de-entorno.md), [SQL](../conceptos/sql.md), [Inyección SQL](../conceptos/inyeccion-sql.md), [Persistencia de datos](../conceptos/persistencia.md), [Router](../conceptos/router.md), [Prepared statement](../conceptos/prepared-statement.md), [HTTP](../conceptos/http.md)
<!-- /auto:pie -->
