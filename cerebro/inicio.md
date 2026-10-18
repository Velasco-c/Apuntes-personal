---
titulo: "Inicio: mapa rápido de los apuntes"
tags: ["cerebro"]
---

# Inicio: mapa rápido de los apuntes

Índice para buscar con Ctrl+F: escribe el concepto o el tema, en español o en inglés, y sigue el enlace. Se genera solo con `actualizar`; no lo edites a mano.

## Acceso rápido

| Quiero... | Ir a |
| --- | --- |
| Empezar a estudiar | [Bases de datos](../bases-de-datos/indice.md) |
| Buscar una sección de una lección | [Lecciones por secciones](lecciones.md) |
| Ver el mapa completo | [Mapa de contenidos](../MAPA.md) |
| Consultar con Gemini | [Tutorial de Gemini](../consultar-con-gemini.md) |
| Consultar sin conexión | [Tutorial de Ollama](../tutorial-ollama.md) |
| Añadir o mantener contenido | [Guía de mantenimiento](../MANTENIMIENTO.md) |

## Conceptos por categoría

### [Fundamentos](../conceptos/fundamentos/categoria.md)

> Conceptos básicos que no pertenecen a una tecnología concreta: qué son los datos, cómo se conservan y cómo se configura una aplicación.

| Concepto | Qué es |
| --- | --- |
| [Dato](../conceptos/fundamentos/dato.md) | Dato es la representación de un hecho, un valor o una medida, registrado sin interpretación. |
| [Persistencia de datos](../conceptos/fundamentos/persistencia.md) | Persistencia de datos es la capacidad de conservar información más allá de la ejecución del programa que la creó. |
| [Variable de entorno](../conceptos/fundamentos/variable-de-entorno.md) | Una variable de entorno es un valor de configuración que se define fuera del código de la aplicación, por ejemplo en el sistema operativo o en un archivo .env, y que el p… |

### [Bases de datos](../conceptos/bases-de-datos/categoria.md)

> Conceptos generales de las bases de datos, válidos para cualquier sistema gestor.

| Concepto | Qué es |
| --- | --- |
| [Base de datos](../conceptos/bases-de-datos/base-de-datos.md) | Una base de datos es una colección organizada de datos relacionados entre sí, almacenada de forma que pueda consultarse, modificarse y administrarse de manera controlada. |
| [Base de datos relacional](../conceptos/bases-de-datos/base-de-datos-relacional.md) | Una base de datos relacional organiza la información en tablas relacionadas entre sí mediante claves. |
| [Sistema gestor de bases de datos (SGBD)](../conceptos/bases-de-datos/sgbd.md) | Un sistema gestor de bases de datos (SGBD) es el software que crea, administra y da acceso a las bases de datos. |
| [Transacción](../conceptos/bases-de-datos/transaccion.md) | Una transacción es un conjunto de operaciones sobre una base de datos que se ejecutan como una sola unidad: o se completan todas, o no se aplica ninguna. |

### [Bases de datos › Modelado de datos](../conceptos/bases-de-datos/modelado/categoria.md)

> Cómo se diseña una base de datos antes de implementarla: se identifican entidades, atributos y relaciones, y después se transforman en tablas normalizadas.

| Concepto | Qué es |
| --- | --- |
| [Atributo](../conceptos/bases-de-datos/modelado/atributo.md) | Un atributo es una propiedad que describe a una entidad. |
| [Cardinalidad](../conceptos/bases-de-datos/modelado/cardinalidad.md) | La cardinalidad indica cuántas ocurrencias de una entidad pueden relacionarse con cuántas ocurrencias de otra. |
| [Entidad](../conceptos/bases-de-datos/modelado/entidad.md) | Una entidad es la representación de un objeto, persona, concepto o evento del mundo real que es relevante para el sistema y sobre el que se almacena información. |
| [Modelo entidad-relación (MER)](../conceptos/bases-de-datos/modelado/mer.md) | El modelo entidad-relación (MER) es una técnica de modelado conceptual que describe los datos de un sistema mediante entidades, atributos y relaciones, representados en u… |
| [Modelo lógico relacional](../conceptos/bases-de-datos/modelado/modelo-logico-relacional.md) | El modelo lógico relacional es la etapa de diseño en la que el MER se transforma en un conjunto de tablas, columnas, claves y restricciones. |
| [Normalización](../conceptos/bases-de-datos/modelado/normalizacion.md) | La normalización es un proceso de diseño que organiza las tablas para reducir la redundancia y evitar anomalías al insertar, actualizar o eliminar datos. |
| [Relación entre entidades](../conceptos/bases-de-datos/modelado/relacion.md) | Una relación es una asociación entre dos o más entidades que describe cómo se vinculan sus ocurrencias. |

### [Bases de datos › Estructura y claves](../conceptos/bases-de-datos/estructura/categoria.md)

> Los elementos con los que se construye una base de datos relacional ya implementada: tablas, filas, claves, índices y vistas.

| Concepto | Qué es |
| --- | --- |
| [Llave (clave)](../conceptos/bases-de-datos/estructura/llave.md) | Una llave, también llamada clave, es un atributo o conjunto de atributos que identifica o relaciona filas dentro de una base de datos. |
| [Llave foránea (FK)](../conceptos/bases-de-datos/estructura/llave-foranea.md) | Una llave foránea (FK, foreign key) es un atributo de una tabla que referencia la llave primaria de otra tabla, o de la misma. |
| [Llave primaria (PK)](../conceptos/bases-de-datos/estructura/llave-primaria.md) | Una llave primaria (PK, primary key) es el atributo o conjunto de atributos que identifica de forma única e inequívoca cada fila de una tabla. |
| [Tabla](../conceptos/bases-de-datos/estructura/tabla.md) | Una tabla es la estructura básica de una base de datos relacional. |
| [Tupla](../conceptos/bases-de-datos/estructura/tupla.md) | Una tupla, también llamada fila o registro, es una ocurrencia única de una entidad dentro de una tabla. |
| [Vista](../conceptos/bases-de-datos/estructura/vista.md) | Una vista es una consulta guardada con un nombre, que se usa como si fuera una tabla. |
| [Índice de base de datos](../conceptos/bases-de-datos/estructura/indice-bd.md) | Un índice de base de datos es una estructura auxiliar que permite localizar filas por el valor de una o más columnas sin recorrer toda la tabla. |

### [SQL](../conceptos/sql/categoria.md)

> El lenguaje SQL y las construcciones que se usan para consultar, modificar y programar datos.

| Concepto | Qué es |
| --- | --- |
| [CRUD](../conceptos/sql/crud.md) | CRUD es el acrónimo de Create, Read, Update, Delete: las cuatro operaciones básicas que se realizan sobre cualquier dato almacenado. |
| [CTE](../conceptos/sql/cte.md) | Una CTE (Common Table Expression, expresión de tabla común) es una consulta temporal con nombre, definida con WITH al inicio de una sentencia. |
| [Evento programado](../conceptos/sql/evento-programado.md) | Un evento programado es una tarea que el servidor de base de datos ejecuta según un calendario, por ejemplo cada noche, o una sola vez en un momento determinado. |
| [Función de ventana](../conceptos/sql/funcion-de-ventana.md) | Una función de ventana calcula un valor para cada fila usando un conjunto de filas relacionadas con ella, definido con la cláusula OVER. |
| [JOIN](../conceptos/sql/join.md) | Un JOIN es una operación SQL que combina filas de dos o más tablas según una condición. |
| [Procedimiento almacenado](../conceptos/sql/procedimiento-almacenado.md) | Un procedimiento almacenado es un bloque de sentencias SQL guardado en el servidor de base de datos, que se invoca por su nombre y puede recibir parámetros. |
| [SQL](../conceptos/sql/sql.md) | SQL (Structured Query Language) es el lenguaje estándar para definir, consultar y manipular datos en bases de datos relacionales. |
| [Trigger](../conceptos/sql/trigger.md) | Un trigger (disparador) es un bloque de código que se ejecuta automáticamente cuando ocurre un INSERT, un UPDATE o un DELETE sobre una tabla. |

### [Motores de base de datos](../conceptos/motores/categoria.md)

> Sistemas gestores de bases de datos concretos.

| Concepto | Qué es |
| --- | --- |
| [MySQL](../conceptos/motores/mysql.md) | MySQL es un sistema gestor de bases de datos relacionales de código abierto, muy usado en aplicaciones web. |
| [PostgreSQL](../conceptos/motores/postgresql.md) | PostgreSQL es un sistema gestor de bases de datos relacionales de código abierto. |

### [Acceso a datos desde una aplicación](../conceptos/acceso-a-datos/categoria.md)

> Cómo una aplicación se conecta a una base de datos y ejecuta consultas de forma eficiente y segura.

| Concepto | Qué es |
| --- | --- |
| [Controlador de base de datos](../conceptos/acceso-a-datos/controlador-de-base-de-datos.md) | Un controlador (driver) de base de datos es la biblioteca que permite a una aplicación comunicarse con un motor concreto: abre la conexión, envía las consultas y recibe l… |
| [Inyección SQL](../conceptos/acceso-a-datos/inyeccion-sql.md) | La inyección SQL es una vulnerabilidad que ocurre cuando datos proporcionados por el usuario se concatenan directamente en una consulta SQL, de modo que pueden alterar su… |
| [Pool de conexiones](../conceptos/acceso-a-datos/pool-de-conexiones.md) | Un pool de conexiones es un conjunto de conexiones abiertas a la base de datos que la aplicación comparte y reutiliza. |
| [Prepared statement](../conceptos/acceso-a-datos/prepared-statement.md) | Una sentencia preparada (prepared statement) es una consulta SQL cuya estructura se envía al motor por separado de sus valores. |

### [Programación orientada a objetos](../conceptos/programacion/categoria.md)

> Conceptos de programación orientada a objetos.

| Concepto | Qué es |
| --- | --- |
| [Herencia](../conceptos/programacion/herencia.md) | La herencia es un mecanismo por el que una clase recibe los atributos y métodos de otra, llamada clase padre o superclase, y puede extenderlos o modificarlos. |
| [Polimorfismo](../conceptos/programacion/polimorfismo.md) | El polimorfismo es la capacidad de tratar objetos de distinto tipo mediante una misma interfaz, de modo que cada uno responde a su manera a la misma operación. |
| [Programación orientada a objetos](../conceptos/programacion/poo.md) | La programación orientada a objetos (POO) es un paradigma que organiza el código en objetos. |

### [Ingeniería de software](../conceptos/ingenieria/categoria.md)

> Principios, patrones y prácticas para organizar el código: cómo se diseñan los componentes, cómo se transportan y validan los datos, cómo se manejan los errores y cómo se prueba el software.

| Concepto | Qué es |
| --- | --- |
| [DTO (Data Transfer Object)](../conceptos/ingenieria/dto.md) | Un DTO (Data Transfer Object, objeto de transferencia de datos) es un patrón de diseño que define un objeto simple para transportar datos entre capas o componentes de una… |
| [Escalabilidad](../conceptos/ingenieria/escalabilidad.md) | La escalabilidad es la capacidad de un sistema para atender más carga, como más usuarios, más peticiones o más datos, sin perder rendimiento de forma inaceptable. |
| [Manejo centralizado de errores](../conceptos/ingenieria/manejo-centralizado-de-errores.md) | El manejo centralizado de errores es un patrón en el que todos los errores de la aplicación se entregan a un único manejador, que decide la respuesta que se envía. |
| [Patrón de diseño](../conceptos/ingenieria/patron-de-diseno.md) | Un patrón de diseño es una solución probada y reutilizable para un problema recurrente de diseño de software. |
| [Principios SOLID](../conceptos/ingenieria/solid.md) | SOLID es un conjunto de cinco principios de diseño orientado a objetos que buscan código fácil de mantener, extender y probar. |
| [Sanitización de datos](../conceptos/ingenieria/sanitizacion-de-datos.md) | La sanitización de datos es el proceso que limpia o transforma los datos de entrada para dejarlos en una forma uniforme y segura. |
| [Testing automatizado](../conceptos/ingenieria/testing.md) | El testing automatizado consiste en verificar el comportamiento del software mediante pruebas que se ejecutan de forma automática y repetible. |
| [Validación de datos](../conceptos/ingenieria/validacion-de-datos.md) | La validación de datos es el proceso que comprueba que los datos recibidos cumplen las reglas esperadas antes de procesarlos o almacenarlos. |

### [Node.js y herramientas](../conceptos/nodejs/categoria.md)

> Node.js, su entorno de ejecución, el gestor de paquetes y las herramientas que se usan durante el desarrollo.

| Concepto | Qué es |
| --- | --- |
| [dotenv](../conceptos/nodejs/dotenv.md) | dotenv es una biblioteca de Node.js que carga las variables definidas en un archivo .env dentro de process.env cuando arranca la aplicación. |
| [Node.js](../conceptos/nodejs/nodejs.md) | Node.js es un entorno de ejecución de código abierto y multiplataforma que permite ejecutar JavaScript fuera del navegador. |
| [nodemon](../conceptos/nodejs/nodemon.md) | nodemon es una herramienta de desarrollo que observa los archivos de un proyecto Node.js y reinicia el servidor automáticamente cuando detecta cambios. |
| [npm (Node Package Manager)](../conceptos/nodejs/npm.md) | npm (Node Package Manager) es el gestor de paquetes de Node.js. |
| [nvm (Node Version Manager)](../conceptos/nodejs/nvm.md) | nvm (Node Version Manager) es un administrador de versiones de Node.js. |

### [Web y APIs](../conceptos/web/categoria.md)

> Conceptos de la web y de las APIs: protocolos, rutas, peticiones y respuestas, y los elementos de Express que los implementan.

| Concepto | Qué es |
| --- | --- |
| [API](../conceptos/web/api.md) | Una API (Application Programming Interface, interfaz de programación de aplicaciones) es un conjunto de definiciones y protocolos que permiten que componentes de software… |
| [Código de estado HTTP](../conceptos/web/codigo-de-estado-http.md) | Un código de estado HTTP es un número de tres dígitos que el servidor devuelve para indicar el resultado de una solicitud. |
| [DOM (Document Object Model)](../conceptos/web/dom.md) | El DOM (Document Object Model) es la representación en forma de árbol de un documento HTML. |
| [Encabezado HTTP](../conceptos/web/encabezado-http.md) | Un encabezado HTTP (header) es un metadato que se envía junto con una petición o una respuesta. |
| [Endpoint](../conceptos/web/endpoint.md) | Un endpoint es una combinación de un método HTTP y una ruta que el servidor atiende, por ejemplo GET /campus. |
| [Express](../conceptos/web/express.md) | Express es un marco de trabajo minimalista y flexible para Node.js que simplifica la creación de aplicaciones web y APIs. |
| [express-validator](../conceptos/web/express-validator.md) | express-validator es una biblioteca para Express que permite declarar reglas de validación y sanitización sobre los datos de una petición, y consultar sus errores. |
| [HTTP](../conceptos/web/http.md) | HTTP (Hypertext Transfer Protocol) es el protocolo de comunicación de la web. |
| [Middleware](../conceptos/web/middleware.md) | Un middleware es una función que recibe el objeto de solicitud (req), el de respuesta (res) y la función next, y forma parte de una pila que se ejecuta en secuencia cuand… |
| [Modelo cliente-servidor](../conceptos/web/modelo-cliente-servidor.md) | El modelo cliente-servidor es una arquitectura en la que un servidor provee recursos y servicios, y uno o varios clientes los solicitan y consumen mediante peticiones. |
| [Parámetro de ruta](../conceptos/web/parametro-de-ruta.md) | Un parámetro de ruta es una parte variable de una URL que el servidor captura y entrega a la aplicación. |
| [Router](../conceptos/web/router.md) | Un router es un objeto que agrupa rutas relacionadas en un módulo independiente. |

### [Formatos de datos](../conceptos/formatos/categoria.md)

> Formatos de texto para representar datos estructurados que se intercambian entre sistemas.

| Concepto | Qué es |
| --- | --- |
| [JSON](../conceptos/formatos/json.md) | JSON (JavaScript Object Notation) es un formato de texto ligero para representar datos estructurados mediante pares clave-valor y arreglos. |
| [XML](../conceptos/formatos/xml.md) | XML (Extensible Markup Language) es un lenguaje de marcas que organiza la información en etiquetas anidadas. |

### [Inteligencia artificial](../conceptos/inteligencia-artificial/categoria.md)

> Conceptos de inteligencia artificial: modelos de lenguaje, instrucciones a los modelos, redes neuronales y sistemas expertos.

| Concepto | Qué es |
| --- | --- |
| [Alucinación](../conceptos/inteligencia-artificial/alucinacion.md) | Una alucinación en un modelo de lenguaje es una respuesta que suena plausible, pero es falsa o no está respaldada por fuentes. |
| [Base de conocimiento](../conceptos/inteligencia-artificial/base-de-conocimiento.md) | Una base de conocimiento es un conjunto estructurado de hechos y reglas que un sistema experto usa para razonar. |
| [Function calling](../conceptos/inteligencia-artificial/function-calling.md) | El function calling es un mecanismo por el que un modelo de lenguaje solicita ejecutar una función definida por la aplicación, con argumentos estructurados, y después usa… |
| [Model Context Protocol (MCP)](../conceptos/inteligencia-artificial/mcp.md) | El Model Context Protocol (MCP) es un protocolo abierto que estandariza la forma en que un modelo de IA se conecta con herramientas y fuentes de datos externas. |
| [Modelo de lenguaje de gran escala (LLM)](../conceptos/inteligencia-artificial/llm.md) | Un modelo de lenguaje de gran escala (LLM, Large Language Model) es una red neuronal entrenada con grandes volúmenes de texto para predecir el siguiente fragmento de text… |
| [Motor de inferencia](../conceptos/inteligencia-artificial/motor-de-inferencia.md) | Un motor de inferencia es el componente de un sistema experto que aplica las reglas de la base de conocimiento a los hechos disponibles para deducir nuevas conclusiones. |
| [Prompt](../conceptos/inteligencia-artificial/prompt.md) | Un prompt es la instrucción o el contexto que se entrega a un modelo de lenguaje para obtener una respuesta. |
| [Red neuronal](../conceptos/inteligencia-artificial/red-neuronal.md) | Una red neuronal artificial es un modelo computacional inspirado en las neuronas biológicas. |
| [Sistema experto](../conceptos/inteligencia-artificial/sistema-experto.md) | Un sistema experto es un programa que resuelve problemas en un dominio especializado, aplicando una base de conocimiento y reglas de inferencia. |
