---
titulo: "Modelo cliente-servidor"
aliases: ["Modelo cliente-servidor", "modelo cliente-servidor", "arquitectura cliente-servidor", "client-server"]
categoria: "web"
tags: ["concepto"]
---

# Modelo cliente-servidor

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

El **modelo cliente-servidor** es una arquitectura en la que un servidor provee recursos y servicios, y uno o varios clientes los solicitan y consumen mediante peticiones. En la web, el cliente suele ser un navegador o una aplicación móvil, y el servidor una aplicación que responde con HTTP.

## Roles

* **Servidor:** escucha las peticiones, procesa la lógica y devuelve las respuestas. Puede atender a muchos clientes a la vez.
* **Cliente:** inicia la comunicación y presenta el resultado al usuario.

## Flujo típico

```text
Cliente  --GET /productos-->  Servidor
Cliente  <--200 + JSON----   Servidor
```

## Diferencia con peer-to-peer

En una red **peer-to-peer**, cada nodo puede actuar como cliente y como servidor, sin un proveedor central. En el modelo cliente-servidor, los roles están separados: el servidor centraliza los recursos y los clientes los solicitan. La web funciona principalmente con este modelo, aunque algunas aplicaciones combinan ambos enfoques.

## Ver también

* [HTTP](http.md): el protocolo que transporta cada solicitud y respuesta.
* [API](api.md): la interfaz que el servidor ofrece a sus clientes.
