# Programacion_Estrucutrada
Tareas y Trabajos de Programacion estructurada en lenguajes C++ y JAVA


# Parcial 2 Tarea 1
Crear por medio de bucles y concatenación de datos las tablas de multiplicar del 1 al 10

Deben de utilizar el for, los programas deben de ser realizados en Java y en C++


# Parcial 2 Tarea 2
# Instrucciones para el Ejercicio: Adivinar el Número
En este ejercicio, tu tarea es escribir un programa que permita a un usuario adivinar un número secreto. El programa debe seguir estos pasos:

Establecer un Número Secreto:

El programa debe definir un número secreto. Por simplicidad, puedes asignar un valor fijo al número secreto (por ejemplo, 7).
Solicitar Intento al Usuario:

El programa debe pedir al usuario que adivine el número secreto. Esto se puede hacer mostrando un mensaje en la consola solicitando una entrada.
Evaluar la Adivinanza:

El programa debe verificar si el número introducido por el usuario coincide con el número secreto.
Si el usuario adivina incorrectamente, el programa debe indicar que la adivinanza es incorrecta y solicitar otro intento.
Repetir hasta Adivinar Correctamente:

El programa debe continuar solicitando intentos hasta que el usuario adivine el número correctamente.
Indicar Éxito:

Cuando el usuario adivine correctamente el número secreto, el programa debe mostrar un mensaje de felicitación indicando que ha adivinado correctamente.

# Ejemplo de Flujo del Programa:
* El programa define el número secreto como 7.
* El programa muestra el mensaje: "Adivina el número (entre 1 y 10): ".
* El usuario introduce un número.
* Si el número introducido por el usuario no es 7, el programa muestra el mensaje: "Intenta de nuevo: " y solicita otro número.
* El programa repite los pasos 3 y 4 hasta que el usuario introduce el número 7.
* Cuando el usuario adivina correctamente, el programa muestra el mensaje: "¡Adivinaste!".


# Parcial 3 Tarea 2

## Instrucciones del ejercicio

Crea un programa que permita al usuario administrar una lista de tareas pendientes. 

El programa debe tener las siguientes funciones:

- `agregar_tarea(tareas, tarea)`: Esta función debería recibir una lista `tareas` y una `tarea` como entrada y agregar la tarea a la lista.
- `listar_tareas(tareas)`: Esta función debería mostrar la lista de tareas numeradas.
- `completar_tarea(tareas, numero)`: Esta función debería recibir una lista `tareas` y el número de una tarea y marcar esa tarea como completada.
- `eliminar_tarea(tareas, numero)`: Esta función debería recibir una lista `tareas` y el número de una tarea y eliminar esa tarea de la lista.

El programa principal debe usar un bucle para permitir al usuario realizar las siguientes operaciones:

* Agregar una nueva tarea.
* Listar las tareas pendientes.
* Marcar una tarea como completada.
* Eliminar una tarea.
* Salir del programa.

# Parcial 3 Tarea 3

## Instrucciones del ejercicio

Con base al codigo de diccionarios dentro de este mismo repositorio realiza el siguiente ejercio:

* Solicitar al usuario un numero entero
* El programa deberá convertir o traducir ese numero entero en un numero romano
* Deberá hacer uso de funciones, diccionarios
* Deberá mostrar al usuario el número convertido en romano
* Solo permitirá números inferiores a 1001, mostrar una alerta cuando se ingrese un número mayor y solicitar uno nuevo



# Examen POO
## Instrucciones del examen
Descripción del Proyecto
La empresa tiene diferentes tipos de vehículos (autos, motocicletas, camiones) que se pueden alquilar. Cada vehículo tiene características generales (como marca, modelo, año, precio por día) y comportamientos específicos según su tipo (por ejemplo, un camión puede transportar carga, mientras que un auto puede ser de lujo o estándar).

Estructura del Proyecto
Clases principales:

Una clase base abstracta Vehiculo.
Subclases para tipos específicos de vehículos (Auto, Motocicleta, Camion).
Encapsulamiento:

Atributos privados o protegidos (por ejemplo, el estado del vehículo: disponible, alquilado).
Métodos para consultar o modificar el estado de forma controlada.
Herencia:

Las subclases heredan atributos y métodos de la clase base Vehiculo.
Polimorfismo:

Un método como calcular_precio() puede comportarse de forma diferente según el tipo de vehículo (por ejemplo, precios adicionales para autos de lujo).
