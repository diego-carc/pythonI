# T6 - Manejo de secuencias

## Autor: Diego Carmona Campos
## Última actualización: 27/09/2023

### **Introducción**
El formato fastq es la salida de muchos secuenciadores de última generación. En estos archivos se muestra la secuencia con un identificador y, para cada posición de la secuencia, se cuenta con un caracter que representa su calidad según su valor en el código ASCII. Este valor puede darnos una idea de la probabilidad de tener una lectura incorrecta y por lo tanto analizar la calidad promedio de nuestras secuencias es de suma importancia al momento de hacer análisis  bioinformáticos.

**Problema:**

Crear una programa que permita leer un archivo FASTQ y obtener el número de lecturas cuyo promedio de calidad esté por debajo de un umbral dado.

### **Metodología**

El algoritmo para resolver el problema es:

1. Recibir de la línea de comandos la ruta al archivo con la secuencia fastq y el umbral para promediar la calidad.
2. Usar SeqIO para parsear el archivo fastq.
3. Iterar sobre el objeto de secuencia que se obtiene con SeqIO.
4. Para cada secuencia, obtener las calidades asociadas a cada posición del nucleótido.
5. Hacer una lista con las calidades de una secuencia y obtener el promedio.
6. Si el promedio está por debajo del umbral, se agrega a otra lista.
7. Obtener la longitud de la lista con los promedios debajo del umbral.

### Ejemplo
```
python python  .\countFastQs.py -f ..\data\sample.fastq -t 39
```
ouput:
```
19
```

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diego-carc/pythonI/tree/master/tareas/countFastQs/).
