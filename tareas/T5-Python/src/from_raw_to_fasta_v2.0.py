'''
NAME
    from_raw_to_fasta_v2.0.py
  
VERSION
    2.0  05/05/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa recibe un archivo de texto plano con una secuencia de DNA y lo convierte a formato fasta.

CATEGORY
   Sequence    

USAGE

    % python from_raw_to_fasta_v2.0.py
    
ARGUMENTS

path: La ruta al directorio con el archivo input

name: El nombre del archivo con la secuencia row

identifier: El identificador de la secuencia 

output_file_name: El nombre para el archivo de salida

--output_path: La ruta al directorio donde se desea guardar el archivo fasta. Def: Directorio desde donde se ejecuta el script

--cut: El número de bases por línea para el archivo fasta. Def: 100

SEE ALSO
'''

import argparse
import re

# Main
# Definir errores
class AmbiguousBaseError(Exception):
    pass

# Iniciar el parseador 
description = 'El programa genera un archivo en formato fasta a partir de un archivo row con una secuencia de DNA.'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('path',
                    type=str,
                    help='La ruta a la ubicación del archivo con la secuencia de DNA')
parser.add_argument('file_name',
                    type=str,
                    help='El nombre del archivo con la secuencia de DNA')
parser.add_argument('identifier', 
                    type=str, 
                    help='El identificador para la seucencia')
parser.add_argument('output_file_name',
                    type=str,
                    help='El nombre para generar el archivo .fasta',
                    default='output_file')
parser.add_argument('--output_path',
                    type=str,
                    help='La ruta para guardar el archivo. Def:".\\"',
                    default='.\\',
                    required=False)
parser.add_argument('--cut',
                    type=int,
                    help='El número de bases por línea para el archivo de salida.. Def: 100',
                    required=False,
                    default=100)

# Parsear argumentos
args = parser.parse_args()

# Abrir archivo
try:
    file = open(args.path + args.file_name)
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
    # Abrir archivo de salida
    output = open(f'{args.output_path+args.output_file_name}.fasta', 'w') 
    identifier = args.identifier

    # Guardar secuencia en formato fasta
    output.write(f"> {identifier}")

    for base in range(len(dna_sequence)):
        if not base % args.cut:
            output.write('\n')

        output.write(dna_sequence[base])

    # Cerrar archivo
    output.close()


