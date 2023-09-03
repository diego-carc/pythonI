# T2-Python: Contar As, Ts, Gs, Cs

## Autor: Diego Carmona Campos
## Última actualización: 26/08/2023

### **Introducción**
Usualmente un programa puede requerir de datos externos para trabajar en función de esa entrada, por lo que es conveniente contar con herramientas que nos permitan pasarle estos datos a los programas sin tener que ingresarlos manualmente en el código. Para ello, Python cuenta con algunas funciones para recibir entradas desde el teclado. En ese trabajo se usará la función *input()* para recibir como argumento una secuencia de DNA.

**Problema:**

- Hacer un programa que cuente el total de A, C, G y T que hay en una secuencia de DNA.

- La secuencia debe pedirse al usuario cada vez que se ejecute el programa.


### **Metodología**
1. Se crea el argumento *sequence* con *argparse*, que recibe la ruta al archivo con la secuencia de ADN
2. Se abre el archivo y se obtiene la cadena con la secuencia de ADN
3. Por cada nucleótido (A, T, C o G) cuento el contenido con el método *count()*

### Ejemplo
```
# Estando dentro de la carpeta *src*
python .\contar_nucleotidos.py ../data/dna_sequence.txt
```
output:
```
A: 1264
T: 1203
C: 1265
G: 1268
```

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diegocarcam/pythonI/tree/master/tareas/T2-Python).