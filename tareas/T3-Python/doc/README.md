# T3-Python: Contenido de AT y GC

## Autor: Diego Carmona Campos
## Última actualización: 28/03/2023

### **Introducción**
Usualmente un programa puede requerir de datos externos para trabajar en función de esa entrada, por lo que es conveniente contar con herramientas que nos permitan pasarle estos datos a los programas sin tener que ingresarlos manualmente en el código. Además, en biología solemos trabajar con una gran cantidad de datos, lo que nos obliga a hacer uso de archivos de texto plano para poder manejarlos. Es por ello que usaremos las herramientas para el manejo de archivos de Python para resolver problemas biológicos:

**Problema:**
 
 ¿Cuál es el porcetaje de AT y GC en la secuencia del archivo dna.txt`
 

- Escribe un programa que te regrese el porcentaje de AT y GC
- El programa debe preguntar la ruta y el nombre del archivo de DNA de manera interactiva.


### **Metodología**
1. En la variable *nombre* guardo una cadena con el nombre del archivo, el cual recibo desde el teclado con la función *input()*.
2. En la variable *ruta* guardo una cadena con la ruta hacia el archivo, el cual recibo desde el teclado con la función *input()*.
3. En la variable *dna* abro el archivo usando *open()* y pasando como argumento la unión de las cadenas *ruta* y *nombre*.
4. Con el método *read()* accedo al contenido del archivo en forma de string.
5. Con el método *rstrip()* elimino el último salto de línea en el string.
6. Uso las variables *porcentaje_GC* y *porcentaje_AT* para guardar el contenido de cada par de bases. Este contenido se calcula contando el número de repeticiones de cada base, sumando los pares, multiplicando por 100 y luego dividiendo entre la longitud de la cadena.
7. Uso la función *print* con fstrings para imprimir el output.

Dado que la estructura de este proyecto es: 

├───data
├───doc
├───results
└───src

Se recomienda guardar el archivo de interés en la carpeta data y ejecutar el programa desde la carpeta src. De esta manera, se puede pasar la ruta como:
***"../data/"***

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diegocarcam/pythonI/tree/master/tareas/T3-Python).