'''
NAME
    porcentaje_AT_GC_v2.0.py
  
VERSION
    2.0  05/05/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa calcula el contenido de AT de una secuencia de DNA proveniente de un archivo

CATEGORY
   Sequence    

USAGE

    % python porcentaje_AT_GC_v2.0.py

    El programa recibirá:

      a) La ruta donde se encuentra el archivo.

      b) El nombre del archivo con la secuencia de DNA.

      c) El número de decimales para la respuesta.
    
ARGUMENTS

path: La ruta donde se encuentra el archivo.

name: El nombre del archivo con la secuencia de DNA.

-r: El número de decimales para redondear la respuesta (Opcional).

SEE ALSO
'''

import argparse
import re

# Functions
def get_AT_content(dna_sequence, r=2):
    '''
    Calcula el contenido de AT en una secuencia de DNA

    Args:
        dna_sequence: El string con la secuencia de DNA
        r: El número de decimales para redondear la respuesta
    '''
    seguence_lenght = len(dna_sequence)
    A_content = dna_sequence.count('A')
    T_content = dna_sequence.count('T')
    return(round((A_content+T_content)/seguence_lenght, r))

# Main
# Definir errores
class AmbiguousBaseError(Exception):
    pass

# Iniciar el parseador 
description = 'El programa calcula el porcentaje de AT de secuencia de DNA proveniente de un archivo.'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('path',
                    type=str,
                    help='La ruta a la ubicación del archivo con la secuencia de DNA.')
parser.add_argument('name',
                    type=str,
                    help='El nombre del archivo con la secuencia de DNA')
parser.add_argument('-r', 
                    type=int, help='El número de decimales para la respuesta', 
                    required=False,
                    default=2)

# Parsear argumentos
args = parser.parse_args()

# Abrir archivo
try:
    file = open(args.path + args.name)
    dna_sequence = file.read().rstrip('\n').upper()
    dna_sequence = dna_sequence.split('\n')
    dna_sequence = ''.join(dna_sequence)
    file.close()

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
    print(f'El contenido de AT de la secuencia es: {get_AT_content(dna_sequence, args.r)}')