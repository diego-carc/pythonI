'''
NAME
    contar_nucleotido.py
  
VERSION
    2.0  05/05/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa cuenta los nucleótidos (A, T, C, G) de un archivo con
    una secuencia de DNA.

CATEGORY
   Sequence    

USAGE

    % python contar_nucleotidos.py path file_name

    El programa recibirá:
      
      a) La ruta al archivo

      b) El nombre del archivo
    
ARGUMENTS

    path: La ruta a la ubicación del archivo con la secuencia de DNA.

    file_name: El nombre del archivo con la secuencia de DNA. 

SEE ALSO
'''

# Imports
import argparse 
import re 

# Functions
def count_ATCG(dna_sequence):
    '''
    Cuenta los nucleótidos A, T, C y G de una secuencia de DNA.

    Args:
        dna_sequence (str): Secuencia de DNA.
    
    Returns:
        Un diccionario cuyos keys son las bases y cada value es el conteo de la base.
    '''
    bases = ['A', 'T', 'C', 'G']
    bases_count = {base : dna_sequence.count(base) for base in bases}
    return(bases_count)
    
# Main
# Definir errores
class AmbiguousBaseError(Exception):
    pass

# Iniciar el parseador 
description = 'El programa cuenta los nucleótidos (As, Ts, Cs y Gs)\nde una secuencia de DNA proveniente de un archivo.'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('path',
                    type=str,
                    help='La ruta con la ubicación del archivo con la secuencia de DNA.')
parser.add_argument('file_name',
                    type=str,
                    help='El nombre del archivo con la secuencia de DNA')

# Parsear argumentos
args = parser.parse_args()

# Abrir archivo
try:
    input_file = open(args.path + args.file_name)
    dna_sequence = input_file.read().rstrip('\n').upper()
    dna_sequence = dna_sequence.split('\n')
    dna_sequence = ''.join(dna_sequence)
    input_file.close()

    if len(dna_sequence) == 0:
        raise ValueError()
    
    if len(re.findall(r'[^ATCG]', dna_sequence)):
        raise AmbiguousBaseError()

except IOError:
    print('La ruta o el archivo ingresado no existe') 
except ValueError:
    print('El archivo está vacío')
except AmbiguousBaseError:
    print('El archivo contiene bases ambigüas.')
else:
    count = count_ATCG(dna_sequence)
    for key, value in count.items():
        print(f'La secuencia tiene {value} {key}s')

