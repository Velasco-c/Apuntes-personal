---
titulo: "Evento programado"
aliases: ["Evento programado", "evento programado", "eventos programados", "event scheduler"]
categoria: "sql"
tags: ["concepto"]
---

# Evento programado

<!-- auto:categoria -->
Categoría: [SQL](categoria.md)
<!-- /auto:categoria -->

Un **evento programado** es una tarea que el servidor de base de datos ejecuta según un calendario, por ejemplo cada noche, o una sola vez en un momento determinado. En MySQL se administra con el *Event Scheduler*.

## Ejemplo en MySQL

```sql
SET GLOBAL event_scheduler = ON;

CREATE EVENT limpiar_sesiones
ON SCHEDULE EVERY 1 DAY
DO
    DELETE FROM sesiones WHERE expira_en < NOW();
```

## Diferencia con un trigger

Un trigger reacciona a un cambio en los datos. Un evento se ejecuta por tiempo, haya habido cambios o no. PostgreSQL no incluye un programador de eventos integrado; para lo mismo se usa una extensión, como `pg_cron`, o un programador externo.

## Errores comunes

Si el programador de eventos está desactivado, el evento se crea pero nunca se ejecuta. Conviene comprobarlo con `SHOW VARIABLES LIKE 'event_scheduler';`. Además, los eventos usan la zona horaria del servidor, no la del usuario, por lo que una tarea programada para las 00:00 puede ejecutarse a otra hora local si el servidor está configurado en otra zona.

## Ver también

* [Trigger](trigger.md): la alternativa cuando la tarea depende de un cambio en los datos.
* [MySQL](../motores/mysql.md): el motor donde el Event Scheduler está integrado.
