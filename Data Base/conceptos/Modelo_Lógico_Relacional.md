# Modelo Lógico Relacional

Etapa de diseño donde el [MER](../conceptos/MER.md) se transforma en una estructura de tablas lista para ser implementada en un [SGBD](../conceptos/SGBD.md).

## Componentes de Diseño
1. **Definición de Campos:**
   - Nombre, descripción y validaciones (**NOT NULL** , longitud, tipo de dato).
1. **Definición de Claves:**
   - [PK](../conceptos/Llave_Primaria.md): Identificador único.
   - **Claves Alternativas:** Candidatos a PK no seleccionados.
   - [FK](../conceptos/Llave_Foránea.md): Vínculo referencial entre tablas.
3. **Reglas de Comportamiento:**
   - **Integridad Referencial:** Definición de acciones ante cambios (ej. `ON DELETE CASCADE`, `ON UPDATE SET NULL`).

```sql
-- Ejemplo de integridad referencial
CREATE TABLE Usuario (
    id_usuario INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(255),
    rol VARCHAR(255)
);

CREATE TABLE TABLA_productos (
    id_producto INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(255),
    precio DECIMAL(10,2) -- Ajustado de 255 a una escala decimal real
);
```