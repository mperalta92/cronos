# Introducción a Cronos
![Cronos](https://upload.wikimedia.org/wikipedia/commons/3/39/Cronos_arm%C3%A9_de_la_faucille_%28harp%C3%A8%29_contre_son_p%C3%A8re_et_divers_m%C3%A9daillons_pierre_grav%C3%A9e_crop.jpg)
Cronos, es una deidad griega que representa el devenir del tiempo. Es un titán al cual se le atribuyen el tiempo de las cosechas y el ser padre de los dioses del olimpo.
Para manejar las tareas sistemáticas a nivel de sistema, se ha creado cronos.zyght.com. Servicio que nos permite centralizar todas las tareas programadas, y monitorear diariamente la salud de los servicios que se van creando. Este microservicio consiste en que se pueden crear de manera dinámica una tarea consistente en llamar alguna url y asignarle una periodicidad.

## Principales funciones
Este microservicio tendrá las siguientes pantallas:
1. Agregar una tarea:
    * Nombre de la tarea
    * Url de la tarea
    * Tipo de método http
    * Params y body
    * periodicidad
2. Mostrar tareas actuales (lista)
3. Editar tarea
4. Borrar tarea
5. Logs de una tarea:
	* Id de la tarea
	* Nombre de la tarea
	* Hora de ejecución
	* Tiempo de demora de la tarea
	* Código de respuesta
	* Cuerpo de respuesta

### Entidades
Tarea --> Task
Registro de la tarea --> TaskLog
Periodicidad --> periodicity
	Días del mes: [1 - 30] o [-30 - -1]
	Días de la semana: [1-7]
	Horas [0:00 - 23:59]

### ¿Cómo se asigna una periodicidad?
Asignar de a un día en el mes:
    Ej: todos los 5 de cada mes
Asignar días en la semana
	Ej: todos los lunes y jueves
Asignar hora durante el día: (unidad mínima minutos)
	Ej: a las 4 am y a las 18 hrs

La condición de validación será (Día del mes OR día de la semana) and Hora checkeando la hora actual cada minuto, en caso de que la condición sea Verdadera, entonces se ejecutará el task. Esto implica que siempre es requerida al menos una hora y al menos un día de la semana o día del mes.
