'''
NAME
    from_raw_to_fasta.py
  
VERSION
    2.0  26/08/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa recibe la ruta a un archivo de texto plano con 
una secuencia de DNA y lo convierte a formato fasta.

CATEGORY
   Sequence    

USAGE

    % python from_raw_to_fasta.py -s [ruta al archivo con la secuencia] -i [identificador] -o [nombre del archivo de salida]
    -c [número de nucleótidos por línea]

ARGUMENTS
    --sequence: Ruta al archivo de texto plano con la secuencia de DNA
    --identifier: Identificador para asignar a la secuencia en formato fasta
    --output: Nombre del archivo de salida en formato fasta
    --cut: Número de nucleótidos para cortar la secuencia en formato fasta   

SEE ALSO
	Me he convertido en la muerte, el destructor de mundos.
'''

# Imports
import argparse

# Argumentos
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sequence",
                    help="Ruta al archivo de texto plano con la secuencia de ADN")
parser.add_argument("-i", "--identifier",
                    help="Identificador de la secuencia para el formato fasta")
parser.add_argument("-o", "--output",
                    help="Nombre del archivo de salida en formato fasta") 
parser.add_argument("-c", "--cut",
                    help="Número de nucleótidos por línea",
                    type=int,
                    default=100,)
args = parser.parse_args()

# Convertir a fasta
with open(args.sequence) as file:
    seq = file.read()
    seq = "".join(seq.split('\n'))

with open(f"{args.output}.fasta", 'w') as file:
    file.write(f">{args.identifier}\n")
    for i,nuc in enumerate(seq):
        if i and not i % args.cut:
            file.write('\n')
        file.write(nuc)

            
