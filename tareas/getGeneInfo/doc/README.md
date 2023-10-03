# Get Gene sequences from GenBank

## Autor: Diego Carmona Campos
## Última actualización: 02/10/2023

### **Introducción**
El formato GenBank fue uno de los primeros intentos por organizar toda la información 
biológica disponible para un organismo en un archivo estandarizado. Si en su diseño no
se consideraron muchos aspectos programáticos, este formato está estructurado de tal 
forma que puede ser parseado y convertido en un objeto. Esto resalta la importancia de
generar herramientas para poder extraer grandes cantidades de información de archivos
con muchos datos.

**Problema:**

Crear una programa que permita leer un archivo GenBank y obtener la secuencia, el transcrito y 
la cadena de aminoácidos asociados a uno o más genes.

### **Metodología**

El algoritmo para resolver el problema es:

1. Recibir de la línea de comandos la ruta al archivo GenBank o el ID
2. Se itera sobre los records en el objeto GB 
3. Por cada record se busca si el nombre del gen coincide con alguno de los que buscamos
4. Si coincide, recuperamos la posición genómica
5. Usando las coordenadas, hacemos un slice de la secuencia del GenBank
6. Obtener el transcrito y la proteína usando los métodos transcribe() y translate() 

### Ejemplo
Caso 1: Se usa busca un solo gen
```
python .\getGeneInfo.py -f ..\data\virus.gb -g L

```
ouput:
```
# Gene L
>Seq
ATGGATGAGTACTCTG...AAGATGATCTGTACTA
>Transcription
AUGGAUGAGUACUCUG...AAGAUGAUCUGUACUA
>Translation
MDEYSEEKWGDSDEES...MTITTDNIQSSDWTD*
```

Caso 2: Se buscan varios genes
```
python .\getGeneInfo.py -f ..\data\virus.gb -g L M N P
```
ouput:
```
# Gene L
>Seq
ATGGATGAGTACTCTG...
>Transcription
AUGGAUGAGUACUCUG...
>Translation
MDEYSEEKWGDSDEES...
# Gene M
>Seq
ATGAAGAGCTTAAAGA...
>Transcription
AUGAAGAGCUUAAAGA...
>Translation
MKSLKRLIKSNKKKGD...
# Gene N
>Seq
ATGACTTCTGTAGTAA...
>Transcription
AUGACUUCUGUAGUAA...
>Translation
MTSVVKRIATGSSVLA...
# Gene P
>Seq
ATGTCTCGACTCAACC...
>Transcription
AUGUCUCGACUCAACC...
>Translation
MSRLNQILKDYPLLEA...
```

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diego-carc/pythonI/tree/master/tareas/getGeneInfo).
