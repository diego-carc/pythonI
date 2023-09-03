'''
NAME
    porcentaje_AT_GC.py
  
VERSION
    2.0  '2/09/2023


AUTHOR
    Diego "El caballo de fuego" Carmona Campos

DESCRIPTION
    El proograma recibe un archivo con una secuencia de DNA y calcula
el porcentaje de AT y GC.

CATEGORY
   Sequence
   Bioinformatics    

USAGE

    % python porcentaje_AT_GC.py -s [path to DNA sequence file]

    El programa recibirá:
        La ruta a un archivo de texto plano con la secuencia de DNA
    
ARGUMENTS
    --sequence: Ruta a un archivo de texto plano con la secuencia de DNA

SEE ALSO

'''

# Imports
import argparse

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument('-s', "--sequence",
                    help="Path al archivo con la secuencia de DNA")
args = parser.parse_args()

# Abrir el archivo
with open(args.sequence) as file:
    dna_sequence = file.read().strip('\n')

# Calcular los porcentajes
porcentaje_GC = (dna_sequence.count("G") + dna_sequence.count("C"))*100/len(dna_sequence) 
porcentaje_AT = (dna_sequence.count("A") + dna_sequence.count("T"))*100/len(dna_sequence)

# Imprimir el output
print(f'El procentaje de GC es: {porcentaje_GC}%\n'
      f'El porcentaje de AT es: {porcentaje_AT}%\n'
      )



