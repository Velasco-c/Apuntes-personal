---
titulo: "Transacción"
aliases: ["Transacción", "transacción", "transacciones", "transaction", "ACID"]
categoria: "bases-de-datos"
tags: ["concepto"]
---

# Transacción

<!-- auto:categoria -->
Categoría: [Bases de datos](categoria.md)
<!-- /auto:categoria -->

Una **transacción** es un conjunto de operaciones sobre una base de datos que se ejecutan como una sola unidad: o se completan todas, o no se aplica ninguna. Por ejemplo, transferir dinero implica restar en una cuenta y sumar en otra. Si solo una de las dos operaciones se aplica, los datos quedan incorrectos.

## Propiedades ACID

* **Atomicidad:** todas las operaciones de la transacción se aplican, o ninguna. Si ocurre un error a mitad del proceso, se revierte todo.
* **Consistencia:** la transacción deja la base de datos en un estado válido según sus reglas y restricciones.
* **Aislamiento:** las transacciones concurrentes no ven los cambios intermedios de las demás.
* **Durabilidad:** una vez confirmada, la transacción sobrevive a fallos del sistema.

## Comandos básicos

```sql
START TRANSACTION;
UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
```

`COMMIT` confirma los cambios. `ROLLBACK` los revierte si algo falla. En MySQL, las transacciones requieren el motor InnoDB.

## Ver también

* [SQL](../sql/sql.md): el lenguaje en el que se escriben las transacciones.
* [MySQL](../motores/mysql.md): un motor que implementa transacciones con InnoDB.
