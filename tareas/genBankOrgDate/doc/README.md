# Obtener organismo y fecha de un GenBank

## Autor: Diego Carmona Campos
## Última actualización: 27/09/2023

### **Introducción**
El formato GenBank fue uno de los primeros intentos por organizar toda la información 
biológica disponible para un organismo en un archivo estandarizado. Si en su diseño no
se consideraron muchos aspectos programáticos, este formato está estructurado de tal 
forma que puede ser parseado y convertido en un objeto. Esto resalta la importancia de
generar herramientas para poder extraer grandes cantidades de información de archivos
con muchos datos.

**Problema:**

Crear una programa que permita leer un archivo GenBank y obtener de qué organismo 
proviene, así como la fecha de subida.

### **Metodología**

El algoritmo para resolver el problema es:

1. Recibir de la línea de comandos la ruta al archivo GenBank o el ID
2. Si se recibe un archivo, se usa SeqIO para parsear su contenido.
3. Si se recibe un ID, se hace la consulta con Entrez para acceder a su
contenido.
4. Se itera sobre los records en el objeto GB y luego se itera sobre el 
diccionario annotations.items
5. Se identican la fecha y el nombre del organismo.

### Ejemplo
Caso 1: Se usa un archivo .gb
```
python .\genBankOrgDate.py -g ..\data\virus.gb  -f
```
ouput:
```
date : 13-AUG-2018
organism : Isfahan virus
```

Caso 2: Se usa un ID
```
python .\genBankOrgDate.py -g NC_020806 -e diegocar@lcg.unam.mx
```
ouput:
```
date : 13-AUG-2018
organism : Isfahan virus
```

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diego-carc/pythonI/tree/master/tareas/).
