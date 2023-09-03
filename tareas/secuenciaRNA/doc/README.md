# T1-Python: Secuencia de RNA

## Autor: Diego Carmona Campos
## Última actualización: 27/03/2023

### **Introducción**
En Python existe el tipo de dato *string*, el cual es una clase con muchos métodos que lo convierten en una herramienta poderosa para procesar cadenas con distintos fines. En esta actividad, aplicaremos algunas de esas funciones para resolver un problema biológico:

**¿Dónde empieza el codón inical AUG en la secuencia dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT' ?**

Escribe un programa que te regrese la posición del codón inicial y donde termina el codón de término

Output: un mensaje y el resultado

### **Metodología**
1. Se parsean los argumentos
    --sequence: Ruta a un archivo de texto plano con una secuencia de ADN
    --initiation: Codón de inicio
    --termination: Codón de paro
2. Se lee el archivo con la secuencia
3. Se busca el marco de lectura abierto
4. PSi no hay marco de lectura se informa y el programa termina
5. Si existe un marco de lectura se imprime en pantalla

### Ejemplo
```
python .\secuencia_RNA.py -s ..\data\dna_sequence.txt -i ATG -t TGA
```
output:
```
El marco de lectura es:
ATGGGTTACGATTTCACTCCTCTACCCGTGCAGCATGCCGGCGGGCACAAGTCCTCATCGGCTCTACCAGTGCTAAGTGCAGAACAACTACTGA
```

```
python .\secuencia_RNA.py -s ..\data\dna_sequence.txt -i AUG -t UGA
```
output:
```
La secuencia no tiene un marco de lectura abierto
```

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diego-carc/pythonI/tree/master/tareas/secuenciaRNA).