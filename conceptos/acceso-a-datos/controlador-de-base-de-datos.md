---
titulo: "Controlador de base de datos"
aliases: ["Controlador de base de datos", "controlador de base de datos", "driver", "mysql2"]
categoria: "acceso-a-datos"
tags: ["concepto"]
---

# Controlador de base de datos

<!-- auto:categoria -->
Categoría: [Acceso a datos desde una aplicación](categoria.md)
<!-- /auto:categoria -->

Un **controlador** (*driver*) de base de datos es la biblioteca que permite a una aplicación comunicarse con un motor concreto: abre la conexión, envía las consultas y recibe los resultados. Por ejemplo, `mysql2` es el controlador que usa Node.js para hablar con [MySQL](../motores/mysql.md).

## Responsabilidades

* Establecer la conexión con el servidor usando host, puerto y credenciales.
* Enviar las sentencias SQL y, si se usan, sus parámetros.
* Convertir los resultados en estructuras del lenguaje, como arreglos de objetos.
* Gestionar los errores de conexión y de consulta.

## Ejemplo con mysql2

```javascript
import mysql from 'mysql2/promise';

const conexion = await mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'tu_contraseña',
    database: 'ejercicios_clase'
});

const [filas] = await conexion.query('SELECT * FROM productos');
```

## Ver también

* [Pool de conexiones](pool-de-conexiones.md): la forma de reutilizar conexiones en una aplicación con varias peticiones simultáneas.
* [Variable de entorno](../fundamentos/variable-de-entorno.md): de donde suelen leerse las credenciales.
