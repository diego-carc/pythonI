# T4-Python: Contenido de AT y GC

## Autor: Diego Carmona Campos
## Última actualización: 29/03/2023

### **Introducción**
Usualmente un programa puede requerir de datos externos para trabajar en función de esa entrada, por lo que es conveniente contar con herramientas que nos permitan pasarle estos datos a los programas sin tener que ingresarlos manualmente en el código. Además, en biología solemos trabajar con una gran cantidad de datos, lo que nos obliga a hacer uso de archivos de texto plano para poder manejarlos. Es por ello que usaremos las herramientas para el manejo de archivos de Python para resolver problemas biológicos:

**Problema:**

Crear un archivo fasta a partir de la secuencia de DNA que está en `dna.txt`


### **Metodología**
1. En la variable *ruta* almaceno la ruta hacia el archivo de texto con la secuencia de DNA.
2. En la variable *nombre* almaceno el nombre para el archivo de salida en formato fasta.
3. En la variable *secuencia* almaceno el nombre que se le agregará a la secuencia en el archivo fasta.
4. Uso la variable *archivo* para abrir el archivo señalado por *ruta*.
5. Con la variable *nuevo* creo el archivo fasta que se usará. Paso como argumento la variable *nombre* para nombrar este archivo.
6. Usando el método *write*, escribo la secuencia de DNA en el archivo y le agrego el identificador.
7. Usando el método *close* cierro los archivos.
8. Al correr este código, generé el archivo *dna.fasta* que se encuentra en la carpeta *results* demeste proyecto.

Dado que la estructura de este proyecto es: 

├───data
├───doc
├───results
└───src

Se recomienda guardar el archivo de interés en la carpeta data y ejecutar el programa desde la carpeta src. De esta manera, se puede pasar la ruta como:
***"../data/'nombre del archivo'"***

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diegocarcam/pythonI).