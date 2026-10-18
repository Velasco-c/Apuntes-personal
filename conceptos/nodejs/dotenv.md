---
titulo: "dotenv"
aliases: ["dotenv"]
categoria: "nodejs"
tags: ["concepto"]
---

# dotenv

<!-- auto:categoria -->
Categoría: [Node.js y herramientas](categoria.md)
<!-- /auto:categoria -->

**dotenv** es una biblioteca de Node.js que carga las variables definidas en un archivo `.env` dentro de `process.env` cuando arranca la aplicación. Permite guardar la configuración del entorno en un archivo local, fuera del código.

## Uso

```text
DB_HOST=localhost
DB_PORT=3306
```

```javascript
import 'dotenv/config';

console.log(process.env.DB_HOST);
```

## Advertencias

* El archivo `.env` contiene credenciales y no debe subirse al repositorio. Debe estar en `.gitignore`.
* Los valores siempre son texto.
* La biblioteca debe cargarse antes de leer las variables. En módulos ES, cada archivo que lea `process.env` al cargarse debe importar `dotenv/config` por sí mismo.

## Precedencia

Por defecto, dotenv **no sobrescribe** una variable que ya existe en el entorno del sistema. Si `DB_HOST` está definida en la terminal antes de ejecutar la aplicación, ese valor se conserva aunque el archivo `.env` tenga otro. Esto permite cambiar la configuración desde la línea de comandos en un despliegue, sin modificar el archivo.

## Ver también

* [Variable de entorno](../fundamentos/variable-de-entorno.md): el concepto que dotenv implementa.
* [Node.js](nodejs.md): el entorno que lee `process.env`.
