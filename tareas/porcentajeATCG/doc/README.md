# T3-Python: Contenido de AT y GC

## Autor: Diego Carmona Campos
## Última actualización: 02/09/2023

### **Introducción**
Usualmente un programa puede requerir de datos externos para trabajar en función de esa entrada, por lo que es conveniente contar con herramientas que nos permitan pasarle estos datos a los programas sin tener que ingresarlos manualmente en el código. Además, en biología solemos trabajar con una gran cantidad de datos, lo que nos obliga a hacer uso de archivos de texto plano para poder manejarlos. Es por ello que usaremos las herramientas para el manejo de archivos de Python para resolver problemas biológicos:

**Problema:**
 
 ¿Cuál es el porcetaje de AT y GC en la secuencia del archivo dna.txt`
 

- Escribe un programa que te regrese el porcentaje de AT y GC
- El programa debe preguntar la ruta y el nombre del archivo de DNA de manera interactiva.


### **Metodología**
1. Se crea el argumento *sequence* con *argparse*, que recibe la ruta al archivo con la secuencia de ADN
2. Se abre el archivo y se obtiene la cadena con la secuencia de ADN
3. Por cada nucleótido (A, T, C o G) cuento el contenido con el método *count()* y se calcula el porcentaje dividiendo por la longitud de la secuencia.

### **Ejemplo**
```Bash
# Dentro de src
python .\porcentaje_AT_GC.py -s ..\data\dna_sequence.txt
```
Output:

```Bash
El procentaje de GC es: 50.168350168350166%
El porcentaje de AT es: 48.86116062586651%
```

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diego-carc/pythonI/tree/master/tareas/porcentajeATCG).