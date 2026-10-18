---
titulo: "Pool de conexiones"
aliases: ["Pool de conexiones", "pool de conexiones", "pools de conexiones", "connection pool"]
categoria: "acceso-a-datos"
tags: ["concepto"]
---

# Pool de conexiones

<!-- auto:categoria -->
Categoría: [Acceso a datos desde una aplicación](categoria.md)
<!-- /auto:categoria -->

Un **pool de conexiones** es un conjunto de conexiones abiertas a la base de datos que la aplicación comparte y reutiliza. En lugar de abrir una conexión nueva por cada consulta, cada petición toma una conexión libre del pool y la devuelve al terminar.

## Por qué se usa

Abrir una conexión es costoso: implica establecer la red, autenticarse y preparar la sesión en el servidor. Reutilizar conexiones reduce esa latencia y evita saturar el servidor con demasiadas conexiones simultáneas.

## Parámetros típicos

* **Tamaño máximo** (`connectionLimit`): cuántas conexiones pueden abrirse a la vez.
* **Cola de espera:** qué ocurre cuando todas están ocupadas. Según la configuración, la petición espera o falla.

## Ejemplo

```javascript
const pool = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    connectionLimit: 10
});
```

## Ver también

* [Controlador de base de datos](controlador-de-base-de-datos.md): la biblioteca que crea las conexiones del pool.
* [Variable de entorno](../fundamentos/variable-de-entorno.md): de donde se leen las credenciales del pool.
