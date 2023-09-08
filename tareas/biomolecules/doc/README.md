# Biomolecules

## Autor: Diego Carmona Campos
## Última actualización: 08/09/2023

### **Introducción**
La Programación Orientada a Objetos (POO) es un paradigma de programación que nos permite embeber datos y funciones bajo una misma estructura. Esta forma de pensar la programación nos permite resolver problemas pensándolos como un conjunto de objetos y sus interacciones. Existen varias características de la POO que nos ayudan a organizar nuestro código, como la herencia, el polimorfirsmo y el *overriding*. 


### **Metodología**
1. Se crea la clase ***biomoleculas*** la cual será la clase parental desde la cual se crearán todas las demás. En esta clase se inicializan atributos que todas las biomoléculas comparten como un nombre, un booleano que indica si la molécula es un polímero, el nombre de las subunidades de la molécula y un booleano que indica si la molécula es hidrofóbica. Además, se agregaron los métodos de ***sintetizar*** y ***degradar*** para llamar a las enzimas que se encargan de formar y destruir cada una de estas moléculas.
2. Se crean clases para cada una de los tipos de biomoléculas: ***proteínas, lípidos, ácidos nucleicos y carbohidratos.*** Estas clases heredan los métodos y atributos de la clase ***biomoléculas***.
3. Para cada una de las clases de biomoléculas se hcieron polimorfismos en los métodos ***sintetizar*** y ***degradar***, de tal manera que se especifica el tipo de enzima encargada de cada una de estas funciones.
4. Se hace una simulación del proceso de síntesis y degradado de 4 biomoléculas, y se imprime en pantalla el resultado.

### Ejemplo
```
python .\src\biomolecules.py
```
output:
```
Inicia la síntesis de biomoléculas...
LLamando glicosil transferasas...
Se sintetizó Glucógeno
{'nombre': 'Glucógeno', 'polimero': True, 'subunidad': 'Glucosa', 'hidrofilica': True}


Llamando enzimas...
Se sintetizó Colesterol
{'nombre': 'Colesterol', 'polimero': False, 'subunidad': 'Ácidos grasos', 'hidrofilica': False}


LLamando ADN polimerasas...
Se sintetizó ADN
{'nombre': 'ADN', 'polimero': True, 'subunidad': 'Nucleótidos', 'hidrofilica': True}


LLamando ribosomas...
Se sintetizó ATP_sintasa
{'nombre': 'ATP_sintasa', 'polimero': True, 'subunidad': 'Aminoácidos', 'hidrofilica': False}


Las biomoléculas se van a degradar...
LLamando sacaridasas
Se degradó Glucógeno


LLamando lipasas...
Se degradó Colesterol


LLamando exonucleasas...
Se degradó ADN


LLamando proteasas
Se degradó ATP_sintasa
```

### **Resultados y conclusiones**
Los resultados pueden encontrarse en [mi repositorio de github](https://github.com/diego-carc/pythonI/tree/master/tareas/).