---
titulo: "XML"
aliases: ["XML"]
categoria: "formatos"
tags: ["concepto"]
---

# XML

<!-- auto:categoria -->
Categoría: [Formatos de datos](categoria.md)
<!-- /auto:categoria -->

**XML** (*Extensible Markup Language*) es un lenguaje de marcas que organiza la información en etiquetas anidadas. Fue muy usado para intercambiar datos entre sistemas, y hoy se mantiene en servicios antiguos, documentos y configuraciones.

## Ejemplo

```xml
<producto>
  <id>1</id>
  <nombre>Teclado mecánico</nombre>
</producto>
```

## Comparación con JSON

XML es más verboso, pero admite atributos, espacios de nombres y validación mediante esquemas (XSD). JSON es más compacto y más directo de usar en JavaScript.

## Dónde aparece

XML sigue presente en servicios SOAP, en archivos de configuración de algunas herramientas, como `pom.xml` en proyectos Java, y en fuentes de noticias como RSS y Atom. Conocer su estructura ayuda a leer esos archivos aunque no se elija para proyectos nuevos.

## Ver también

* [JSON](json.md): el formato que suele reemplazarlo en APIs web.
* [API](../web/api.md): el contexto en el que se intercambian estos datos.
