# T2-Python: Contar As, Ts, Gs, Cs

## Autor: Diego Carmona Campos
## Última actualización: 28/03/2023

### **Introducción**
Usualmente un programa puede requerir de datos externos para trabajar en función de esa entrada, por lo que es conveniente contar con herramientas que nos permitan pasarle estos datos a los programas sin tener que ingresarlos manualmente en el código. Para ello, Python cuenta con algunas funciones para recibir entradas desde el teclado. En ese trabajo se usará la función *input()* para recibir como argumento una secuencia de DNA.

**Problema:**

- Hacer un programa que cuente el total de A, C, G y T que hay en una secuencia de DNA.

- La secuencia debe pedirse al usuario cada vez que se ejecute el programa.


### **Metodología**
1. En el programa creo una variable *dna* que recibirá la cadena que contiene la secuencia.
2. Luego, para recibir la cadena del teclado uso la función input() y paso como argumento el mensaje que quiero que se imprima para solicitar la secuencia.
3. Dentro de la función *print*, utilizo *fstrings* para imprimir el output.
4. Para obtener el número de veces que se repite cada nucleótido, uso el método *count()*.

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diegocarcam/pythonI/tree/master/tareas/T2-Python).