"""
NAME
    countFastQs.py
  
VERSION
    1.0  27/09/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa recibe la ruta a un archivo de texto plano con 
una secuencia de DNA en formato fastq y obtiene el número de 
secuencias con una calidad menor a una línea de corte. 

CATEGORY
   Sequence    

USAGE

    % python countFastQs.py [-h] [-f FILE] [-t TRESHOLD]

ARGUMENTS
    -f FILE, --file FILE: Path to the file containing the fastq sequence
    -t TRESHOLD, --treshold TRESHOLD: Treshold to mean the sequences' quality   

"""
# Imports
from Bio import SeqIO
import argparse

# Functions
def mean(v):
    return(sum(v)/len(v))

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to the file containing the fastq sequence")
parser.add_argument("-t", "--treshold", help="Treshold to mean the sequences' quality", type=int)
args = parser.parse_args()

# Count sequences with a mean quality under a treshold 
t = args.treshold
f = args.file
try: seq = SeqIO.parse(f, format="fastq")
except : 
    print(f"The file {f} doesn't exist")
    exit()
    
print(len([m for record in seq 
           if (m:=mean([int(q) for q in record.letter_annotations["phred_quality"]])) < t]))
 