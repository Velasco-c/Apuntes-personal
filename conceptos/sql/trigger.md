---
titulo: "Trigger"
aliases: ["Trigger", "trigger", "triggers", "disparador"]
categoria: "sql"
tags: ["concepto"]
---

# Trigger

<!-- auto:categoria -->
Categoría: [SQL](categoria.md)
<!-- /auto:categoria -->

Un **trigger** (disparador) es un bloque de código que se ejecuta automáticamente cuando ocurre un `INSERT`, un `UPDATE` o un `DELETE` sobre una tabla. Puede ejecutarse antes (`BEFORE`) o después (`AFTER`) de la operación.

## Usos típicos

* Registrar los cambios en una tabla de auditoría.
* Validar o corregir datos antes de guardarlos.
* Mantener datos derivados actualizados, por ejemplo un total.

## Ejemplo en MySQL

```sql
CREATE TRIGGER registrar_cambio_precio
AFTER UPDATE ON productos
FOR EACH ROW
INSERT INTO auditoria_precios (producto_id, precio_anterior, precio_nuevo)
VALUES (OLD.id, OLD.precio, NEW.precio);
```

`OLD` y `NEW` representan los valores de la fila antes y después del cambio.

## Precauciones

Un trigger ejecuta su código en cada fila afectada, así que una lógica pesada puede degradar todas las operaciones sobre la tabla. Los triggers pueden encadenarse, y un cambio en uno puede activar otro, lo que dificulta depurar el comportamiento. Por eso se reservan para reglas que deben cumplirse siempre, y no para lógica de negocio que cambia con frecuencia.

## Ver también

* [Procedimiento almacenado](procedimiento-almacenado.md): se ejecuta cuando alguien lo invoca.
* [Evento programado](evento-programado.md): se ejecuta según el tiempo, no según cambios en los datos.
