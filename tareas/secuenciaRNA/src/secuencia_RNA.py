'''
NAME
    secuencia_RNA.py
  
VERSION
    2.0  26/08/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa identifica los codones de inicio e imprime la secuencia entre ellos.

CATEGORY
   Sequence    

USAGE

    % python secuencia_RNA.py -s [Ruta al archivo con la secuencia DNA] -i [Codón de inicio] -t [Codón de paro]
    
ARGUMENTS
    --sequence: Ruta a un archivo de texto plano con una secuencia de ADN
    --initiation: Codón de inicio
    --termination: Codón de paro

SEE ALSO

'''

# Imports
import argparse

# Argumentos
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sequence",
                    help="Ruta al archivo de texto plano con la secuencia ADN")
parser.add_argument("-i", "--initiation",
                    help="Codón de inicio en la cadena codificante de DNA",
                    default="ATG")
parser.add_argument("-t", "--termination",
                    help="Codón de paro en la secuencia de ADN",
                    default="TAG")
args = parser.parse_args()

# Leer la secuencia
with open(args.sequence) as file:
    seq = file.read()
    seq = "".join(seq.split('\n'))

# Buscar los codones
if (i:=args.initiation) not in seq or (t:=args.termination) not in seq:
    print("La secuencia no tiene un marco de lectura abierto")
else:
    print("El marco de lectura es:")
    print(seq[seq.find(i):seq.find(t)])