'''
NAME
    contar_nucleotidos.py
  
VERSION
    2.0  26/08/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa recibe un archivo de texto plano con una secuencia de ADN y cuenta el
contenido de cada nucleótido (A,T,C o G)

CATEGORY
   Sequence    

USAGE

    % python contar_nucleotidos.py [ruta al archivo con la secuencia]

    El programa recibirá:
      
      a) La ruta al archivo de texto plano donde se encuentra la secuencia de ADN.
    
ARGUMENTS
    sequence: Ruta al archivo de texto plano con la secuencia de DNA   

SEE ALSO

'''

# Imports
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("sequence",
                       help="Ruta al archivo de texto plano con la secuencia de DNA")
args = parser.parse_args()

# Leer archivo
with open(args.sequence) as file:
    dna_seq = file.read()
    
# Imprimir el output
print("El contenido de los nucleótidos es:")
for base in ["A", "T", "C", "G"]:
    print(f"{base}: {dna_seq.count(base)}")
