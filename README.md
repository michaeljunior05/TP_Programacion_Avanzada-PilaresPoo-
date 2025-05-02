# TP_Programacion_Avanzada-PilaresPoo-

 
## Pregunta teórica: 
¿Cuáles son los 4 pilares de la programación orientada a objetos y qué aporta cada uno? 
## Respuesta:
Los 4 pilares fundamentales de la #POO son:

*Encapsulamiento:* Consiste en ocultar los datos internos de un objeto (sin necesidad saber como funciona internamente) y exponerlo solo a través de métodos públicos. Promoviendo la seguridad de los datos, porque evita las modificaciones directas no controladas.También facilita la modularidad y mantenimiento del código, pues los cambios internos de un objeto no afectan necesariamente a otras partes del sistema.

*Abstracción:* se enfoca en mostrar solo la información relevante de un objeto, ocultando los detalles complejos de su implementación.

*Herencia:* Este pilar permite que una clase (la subclase o clase hija) adquiera las propiedades y los comportamientos de otra clase (la superclase o clase padre). Es como heredar rasgos familiares: la subclase ya tiene ciertas características predefinidas de su "padre".

*Polimorfismo:* Literalmente significa "muchas formas". En POO, se refiere a la capacidad de un objeto de tomar muchas formas diferentes. Esto se logra a través de la herencia y la implementación de interfaces, donde diferentes clases pueden responder al mismo mensaje (llamada a un método) de maneras distintas.


1. ¿Cuál es la diferencia entre encapsulamiento y abstracción?

2. ¿Qué pilar permite a las subclases sobrescribir métodos?
## Respuesta:

<<<<<<< HEAD
## Respuesta:

1. El encapsulamiento protege protege los datos dentro de una clase restringiendo su acceso directo, asegurandose que solo metodos especificos puedan modificarlos, mientras que la abstraccion oculta detalles de implementación y expone solo lo esencial para el usuario.

2. 

=======
1. El encapsulamiento protege protege los datos dentro de una clase restringiendo su acceso directo, asegurandose que solo metodos especificos puedan modificarlos, mientras que la abstraccion oculta detalles de implementación y expone solo lo esencial para el usuario.

2. El pilar que permite a las subclases sobrescribir métodos es la herencia. Esta les permite adquirir los métodos y atributos de una clase padre, pero también les da la capacidad de sobrescribir los métodos heredados para modificar su comportamiento.


## Ejercicio:  

Define una jerarquía simple para vehículos con al menos una clase base y dos clases hijas. 
Cada clase hija debe tener un método propio sobrescrito que imprima información 
diferente. Crea una función que reciba un vehículo y llame a ese método. 


## Reflexion Individual
¿Qué pilar sentís que dominás mejor? ¿Cuál te cuesta más aplicar en la práctica? 
## Reflexiones:
 _*Celina Pereyra*_ :
 De los cuatro pilares de la POO, siento que el encapsulamiento es el que mejor comprendo (pero nose si lo logro aplicar bien). Entiendo la idea de agrupar los datos (atributos) y los métodos que operan sobre esos datos dentro de una clase, y controlar el acceso a esos datos mediante modificadores de acceso (como private, protected, public).
 El que me cuesta más es herencia. Entiendo la idea de la reutilización de código y cómo se pueden crear jerarquías de clases, pero dudo sobre cuál es la mejor manera de estructurar esas jerarquías. 
 _*Viviana Enriquez*_:
  Encapsulamiento podrían ser el que mejor comprendo.
  Durante la practica Herencia sería el que más me cuesta aplicar, por la forma en la cuál debo discernir y manipular la información. Tambien, me pasa con Abstración, en atributo y  detalles.

 _*Junior Flores*_:
 Entiendo todos pero si tuviera que quedarme con uno seria abstraccion ya que el modelar un objeto del mundo real es relativamente facil, y saber que atributos van o no es pensar segun lo que necesites.
 Y el que me cuesta aplicar mas el polimorfismo y la herencia ya que es un poco dificil entender como hacer que funcionen el mismo metodo para diferentes subclases.
## Desafio Adicional
Agregá encapsulamiento con atributos privados y métodos get y set. 
