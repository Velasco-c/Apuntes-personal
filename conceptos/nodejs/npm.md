---
titulo: "npm (Node Package Manager)"
aliases: ["npm (Node Package Manager)", "npm", "node package manager"]
categoria: "nodejs"
tags: ["concepto"]
---

# npm (Node Package Manager)

<!-- auto:categoria -->
Categoría: [Node.js y herramientas](categoria.md)
<!-- /auto:categoria -->

**npm** (*Node Package Manager*) es el gestor de paquetes de Node.js. Descarga, instala, actualiza y elimina bibliotecas y herramientas desde el registro en línea donde se publican los paquetes.

## Archivos principales

* `package.json`: describe el proyecto, sus scripts y sus dependencias.
* `package-lock.json`: fija las versiones exactas instaladas, para que todos instalen lo mismo.
* `node_modules/`: la carpeta donde se guardan las dependencias. No debe subirse al repositorio.

## Comandos básicos

```bash
npm init -y                      # crea package.json
npm install express              # instala una dependencia
npm install --save-dev nodemon   # instala una dependencia de desarrollo
npm uninstall express            # elimina una dependencia
npm run dev                      # ejecuta el script "dev"
```

## Versiones de las dependencias

En `package.json`, el símbolo `^` antes de una versión permite actualizaciones menores y de parche, pero no de versión mayor. Por ejemplo, `^5.3.0` acepta `5.4.0`, pero no `6.0.0`. El símbolo `~` es más restrictivo y solo permite actualizaciones de parche. El archivo `package-lock.json` fija la versión exacta que se instaló, por eso debe incluirse en el repositorio.

## Ver también

* [Node.js](nodejs.md): el entorno para el que se usa npm.
* [nodemon](nodemon.md): una dependencia de desarrollo típica.
