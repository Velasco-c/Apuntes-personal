---
titulo: "Inyección SQL"
aliases: ["Inyección SQL", "inyección SQL", "inyecciones SQL", "SQL injection"]
categoria: "acceso-a-datos"
tags: ["concepto"]
---

# Inyección SQL

<!-- auto:categoria -->
Categoría: [Acceso a datos desde una aplicación](categoria.md)
<!-- /auto:categoria -->

La **inyección SQL** es una vulnerabilidad que ocurre cuando datos proporcionados por el usuario se concatenan directamente en una consulta SQL, de modo que pueden alterar su significado. Un atacante puede así leer, modificar o borrar datos que no le corresponden.

## Ejemplo del problema

```javascript
// Vulnerable: el valor de correo se pega dentro de la consulta
const sql = `SELECT * FROM usuarios WHERE correo = '${correo}'`;
```

Si `correo` vale `' OR '1'='1`, la condición siempre es verdadera y la consulta devuelve todos los usuarios.

## Cómo se evita

* Usar [sentencias preparadas](prepared-statement.md) con marcadores de posición.
* Dar a la aplicación un usuario de base de datos con solo los permisos necesarios.
* Validar los datos de entrada antes de usarlos. Ver [validación de datos](../ingenieria/validacion-de-datos.md).

## Ver también

* [Prepared statement](prepared-statement.md): la técnica que previene el problema.
* [SQL](../sql/sql.md): el lenguaje que se manipula en el ataque.
