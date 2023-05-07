# T4-Python: de raw to FastA

## Autor: Diego Carmona Campos
## Última actualización: 06/05/2023

***

### **Introducción**
Usualmente un programa puede requerir de datos externos para trabajar en función de esa entrada, por lo que es conveniente contar con herramientas que nos permitan pasarle estos datos a los programas sin tener que ingresarlos manualmente en el código. Además, en biología solemos trabajar con una gran cantidad de datos, lo que nos obliga a hacer uso de archivos de texto plano para poder manejarlos. Por otro lado, para hacer programas robustos es necesario pensar en el manejo de errores que pueden surgir al trabjar con archivos, así como con secuencias de DNA. Es por esto que en este proyecto se implementarán programas para el manejo de secuencias biológicas aplicando el paso de argumentos, el manejo de archivos y la gestión de errores.

***

**Problema:**

Modificar los programas

a. Contar As, Ts, Gs, Cs (count_atgc.py)  
b. Contenido de ATs y GCs (at_gc_content.py)  
c. From raw to fasTA (mk-fasta-format.py)  

Que vas a integrar en los programas:

- Leer la secuencia desde un archivo aplicalo a todos los programas. Es decir la secuencia no debe estar en una variable dentro del programa.
- Se debe validar que el archivo de la secuencia exista. ¿Qué pasa si existe y viene vacío?
- La secuencia puede venir en 1 linea o en multiples lineas
- Se debe validar que la secuencia solo sean caracteres ATGC y no otros.
- Valida cualquier otro dato que consideres necesario.

***


### **Algoritmo**
1. **Contar ATCG**

**a.** Definir una función que cuente e imprima las A, T, C y G en una secuencia de DNA y divida el resultado entre la longitud de la cadena, utilizando como argumento la secuencia de DNA.

**b.** Generar un error *AmbiguousBaseError* para indicar que en la secuencia de DNA ingresada hay nucleótidos distintos a A, T, C o G.

**c.** Iniciar el parseador con los argumentos que requerirá el programa:
- path: La ruta a la ubicación del archivo con la secuencia de DNA.
- name: El nombre del archivo con la secuencia de DNA. 

**d.** Abrir el archivo con la secuencia de DNA usando *try* y crear las excepciones para los errores de tipo *IOError*, *ValueError* y *AmbiguousBaseError*.

**e.** Solo si no se produjo un error, llamar a la función *count_ATCG* para imprimir el resultado en pantalla.

***

2. **Contenido de AT**

**a.** Definir una función que calcule el contenido de AT en una secuencia de DNA, sumando las As y las Ts y dividiendo entre la longitud de la secuencia. 

**b.** Generar un error *AmbiguousBaseError* para indicar que en la secuencia de DNA ingresada hay nucleótidos distintos a A, T, C o G.

**c.** Iniciar el parseador con los argumentos que requerirá el programa:
-  path: La ruta donde se encuentra el archivo.
- name: El nombre del archivo con la secuencia de DNA.
-  -r: El número de decimales para redondear la respuesta (Opcional).

**d.** Abrir el archivo con la secuencia de DNA usando *try* y crear las excepciones para los errores de tipo *IOError*, *ValueError* y *AmbiguousBaseError*.

**e.** Solo si no se produjo algún error, llamar a la función *get_AT_content*, pasando como argumentos la secuencia de DNA y el número de decimales para la respuesta.

***

3. **From row to Fasta**

**a.** Generar un error *AmbiguousBaseError* para indicar que en la secuencia de DNA ingresada hay nucleótidos distintos a A, T, C o G.

**b.** Iniciar el parseador con los argumentos que requerirá el programa:
- path: La ruta al directorio con el archivo input
- name: El nombre del archivo con la secuencia row
- identifier: El identificador de la secuencia 
- output_file_name: El nombre para el archivo de salida
- --output_path: La ruta al directorio donde se desea guardar el archivo fasta. Def: Directorio desde donde se ejecuta el script
- --cut: El número de bases por línea para el archivo fasta. Def: 100

**c.** Abrir el archivo con la secuencia de DNA usando *try* y crear las excepciones para los errores de tipo *IOError*, *ValueError* y *AmbiguousBaseError*.

**d.** Solo si no se produjo un error, usar los argumentos para crear el archivo con el nombre, el identificador y la ubicación deseados. La secuencia se copia caracter por caracter y se separa en líneas de acuerdo al argumento *cut*.

***

### **Resultados**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diegocarcam/pythonI/tree/master/tareas/T5-Python).
