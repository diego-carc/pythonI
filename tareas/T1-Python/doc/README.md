# T1-Python: Secuencia de RNA

## Autor: Diego Carmona Campos
## Última actualización: 27/03/2023

### **Introducción**
En Python existe el tipo de dato *string*, el cual es una clase con muchos métodos que lo convierten en una herramienta poderosa para procesar cadenas con distintos fines. En esta actividad, aplicaremos algunas de esas funciones para resolver un problema biológico:

**¿Dónde empieza el codón inical AUG en la secuencia dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT' ?**

Escribe un programa que te regrese la posición del codón inicial y donde termina el codón de término

Output: un mensaje y el resultado

### **Metodología**
1. En el programa asigno a una variable *dna* la secuencia de interés.
2. Luego, en las variables *cod_ini* y *cod_ter* guardo los codones de inicio y término, respectivamente.
3. Dentro de la función *print*, utilizo *fstrings* para imprimir el output.
4. Para obtener la posición de los codones en la secuencia utilizo el método de cadenas *find*.
5. Para obtener la subcadena, utilizo la notación *[:]*.

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diegocarcam/pythonI).