'''
NAME
    porcentaje_AT_GC.py
  
VERSION
    1.1  26/04/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El proograma recibe un archivo con una secuencia de DNA y calcula
el porcentaje de AT y GC.

CATEGORY
   Sequence    

USAGE

    % python porcentaje_AT_GC.py

    El programa recibirá:

      a) El nombre del archivo con la secuencia de DNA.
      b) La ruta donde se encuentra el archivo. 
    
ARGUMENTS
    None    

SEE ALSO

'''

# Recibir del teclado la ruta al archivo
file_name = input('Ingrese el nombre del archivo con la secuencia de DNA: ')
path = input('Ingrese la ruta al archivo: ')

# Abrir el archivo
dna_file = open(path+file_name)

dna_sequence = dna_file.read().rstrip('\n')

# Calcular los porcentajes
porcentaje_GC = (dna_sequence.count("G") + dna_sequence.count("C"))*100/len(dna_sequence) 
porcentaje_AT = (dna_sequence.count("A") + dna_sequence.count("T"))*100/len(dna_sequence)

# Imprimir el output
print(f'El procentaje de GC es: {porcentaje_GC}%\n'
      f'El porcentaje de AT es: {porcentaje_AT}%\n'
      )

dna_file.close()
