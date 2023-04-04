# T4-Python: de raw to FastA

## Autor: Diego Carmona Campos
## Última actualización: 29/03/2023

### **Introducción**
Usualmente un programa puede requerir de datos externos para trabajar en función de esa entrada, por lo que es conveniente contar con herramientas que nos permitan pasarle estos datos a los programas sin tener que ingresarlos manualmente en el código. Además, en biología solemos trabajar con una gran cantidad de datos, lo que nos obliga a hacer uso de archivos de texto plano para poder manejarlos. Es por ello que usaremos las herramientas para el manejo de archivos de Python para resolver problemas biológicos:

**Problema:**

Crear un archivo fasta a partir de la secuencia de DNA que está en `dna.txt`


### **Metodología**

El algoritmo para resolver el problema es:

1. Pedir el nombre del archivo con la secuencia de DNA, al usuario
2. Pedir el nombre del archivo de salida, que será formato fastA
3. Pedir el nombre o identificador de la secuencia apra colocarlo como id en el formato fastA
4. Abrir y leear el archivo de entrada, con la secuencia de DNA
5. Crear el archivo de salida 
6. Escribir la secuencia de DNA en el archivo de salida en formato fastA


Dado que la estructura de este proyecto es: 

├───data
├───doc
├───results
└───src

Se recomienda guardar el archivo de interés en la carpeta data y ejecutar el programa desde la carpeta src. De esta manera, se puede pasar la ruta como:
***"../data/'nombre del archivo'"***

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diegocarcam/pythonI/tree/master/tareas/T4-Python).
