# T4-Python: de raw to FastA

## Autor: Diego Carmona Campos
## Última actualización: 29/03/2023

### **Introducción**
Usualmente un programa puede requerir de datos externos para trabajar en función de esa entrada, por lo que es conveniente contar con herramientas que nos permitan pasarle estos datos a los programas sin tener que ingresarlos manualmente en el código. Además, en biología solemos trabajar con una gran cantidad de datos, lo que nos obliga a hacer uso de archivos de texto plano para poder manejarlos. Es por ello que usaremos las herramientas para el manejo de archivos de Python para resolver problemas biológicos:

**Problema:**

Crear un archivo fasta a partir de la secuencia de DNA que está en `dna.txt`


### **Metodología**

El algoritmo para resolver el problema es:

1. Recibir los argumentos del programa:
    --sequence: Ruta al archivo de texto plano con la secuencia de DNA
    --identifier: Identificador para asignar a la secuencia en formato fasta
    --output: Nombre del archivo de salida en formato fasta
    --cut: Número de nucleótidos para cortar la secuencia en formato fasta
2. Leer el contenido del archivo indicado por el argumento *sequence*
3. Crear el archivo con el nombre del argumento *output*
4. Agregar el *identifier* a la secuencia en formato fasta
5. Formatear la secuencia en formato fasta

### Ejemplo
```
python .\from_raw_to_fasta.py -s ..\data\dna_sequence.txt -i Example_sequence -o ..\results\dna_sequence -c 75
```
ouput:
El archivo de salida se encuentra en la carpeta *results*

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diegocarcam/pythonI/tree/master/tareas/T4-Python).
