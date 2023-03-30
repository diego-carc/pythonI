'''
T3-Python: Porcentaje de AT y GC

Autor: Diego Carmona Campos

Última Actualización: 29/03/2023

Descripción:
El programa calcula el porcentaje de GC y AT en la secuencia de DNA
de un archivo, al cual se accede por medio de la ruta proporcionada 
como input.
'''

# Recibo del teclado la ruta al archivo
nombre = input('Ingrese el nombre del archivo con la secuencia de DNA: ')
ruta = input('Ingrese la ruta al archivo: ')

# Abro el archivo
dna = open(ruta+nombre).read().rstrip('\n')

# Calculo los porcentajes usando métodos de string
porcentaje_GC = (dna.count("G") + dna.count("C"))*100/len(dna) 
porcentaje_AT = (dna.count("A") + dna.count("T"))*100/len(dna)

# Imprimo el output
print(f'El procentaje de GC es: {porcentaje_GC}%\n'
      f'El porcentaje de AT es: {porcentaje_AT}%\n'
      )