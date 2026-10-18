---
titulo: "nvm (Node Version Manager)"
aliases: ["nvm (Node Version Manager)", "nvm", "node version manager"]
categoria: "nodejs"
tags: ["concepto"]
---

# nvm (Node Version Manager)

<!-- auto:categoria -->
Categoría: [Node.js y herramientas](categoria.md)
<!-- /auto:categoria -->

**nvm** (*Node Version Manager*) es un administrador de versiones de Node.js. Permite instalar varias versiones en el mismo equipo, cambiar entre ellas y desinstalar las que no se necesiten.

## Por qué es útil

Distintos proyectos pueden requerir versiones distintas de Node.js. nvm permite usar la versión que necesita cada proyecto sin reinstalar el sistema.

## Comandos básicos

```bash
nvm ls-remote        # muestra las versiones disponibles
nvm install --lts    # instala la versión LTS
nvm use --lts        # usa la versión LTS
nvm ls               # muestra las versiones instaladas
```

En Windows se usa nvm-windows, que es un proyecto distinto con comandos parecidos pero no idénticos.

## Archivo .nvmrc

Un proyecto puede declarar la versión de Node.js que necesita en un archivo `.nvmrc`, que contiene solo el número de versión. Al ejecutar `nvm use` dentro de esa carpeta, nvm cambia a la versión indicada. Así, todo el equipo trabaja con la misma versión sin buscar instrucciones.

## Ver también

* [Node.js](nodejs.md): la herramienta cuyas versiones administra.
* [npm](npm.md): el gestor de paquetes que viene con cada versión.
