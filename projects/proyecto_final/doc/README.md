# Proyecto Final - Python: Contar A, T, C y G

## Autor: Diego Carmona Campos
## Última actualización: 24/05/2023

### **Introducción**

En genómica, la materia prima para los análisis bioinformáticos son las secuencias de DNA. Una de las características más importantes y sencillas de una secuencia es su contenido de nucleótidos (A, T, C y G), por lo que podemos implementar una forma programática para contar el nucleótidos a partir de secuencias que se encuentran en archivos.

Este programa recibe un archivo con la secuencia de DNA de interés en formato txt y cuenta los nucleótidos que contiene.

### **Algoritmo**
El algoritmo para resolver el problema es:

1. Recibir como argumento la ruta al archivo.
2. Recibir  como argumento el nombre del archivo.
3. Verificar que el archivo no esté vacío.
4. Guardar la secuencia de DNA en un solo *string*, eliminando saltos de
5. Verificar que la secuencia no contenga bases ambigüas.
6. Llamar a la función *define_who_wins()* para imprimir el resultado.
7. Imprimir el resultado


### Instalación

Solo se requiere tener python instalado, recomendamos la version más reciente.

### Casos de uso

**1. Se usa la opción -h para obtener una descripción del programa"**

En línea de comando se corre el programa
```
py contar_nucleotidos.py -h

```

En pantalla se imprimirá:
```
usage: contar_nucleotidos.py [-h] path file_name

El programa cuenta los nucleótidos (As, Ts, Cs y Gs) de una secuencia de DNA proveniente de un archivo.

positional arguments:
  path        La ruta con la ubicación del archivo con la secuencia de DNA.
  file_name   El nombre del archivo con la secuencia de DNA

options:
  -h, --help  show this help message and exit
```

**2. El usuario olvida algún argumento**

En línea de comando se corre el programa
```
py contar_nucleotidos.py .\data 

```

En pantalla se imprimirá:
```
usage: contar_nucleotidos.py [-h] path file_name
contar_nucleotidos.py: error: the following arguments are required: file_name
```

**3. El usuario ingresa una ruta que no existe**

En línea de comando se corre el programa
```
py contar_nucleotidos.py .\falso_directorio\ falso_archivo.txt

```

En pantalla se imprimirá:
```
La ruta o el archivo ingresado no existe
```

**4. El archivo que ingresa el usuario está vacío**

En línea de comando se corre el programa
```
py contar_nucleotidos.py .\data\ empty.txt

```

En pantalla se imprimirá:
```
El archivo está vacío
```

**5. El archivo contiene bases ambigüas**

En línea de comando se corre el programa
```
py contar_nucleotidos.py .\data\ amb_base.txt

```

En pantalla se imprimirá:
```
El archivo contiene bases ambigüas
```

**6. La ruta y el archivo están correctos**

En línea de comando se corre el programa
```
py contar_nucleotidos.py .\data\ dna.txt

```

En pantalla se imprimirá:
```
La secuencia tiene 214 As
La secuencia tiene 214 Ts
La secuencia tiene 192 Cs
La secuencia tiene 218 Gs
```