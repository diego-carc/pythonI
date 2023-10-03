"""
NAME
    getGenInfo.py
  
VERSION
    1.0  02/10/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa recibe un archivo GenBank y lo parsea para obtener
    la secuencia, el transcrito y la proteína asociadas a uno o más genes.
    

CATEGORY
   Sequence    

USAGE

    % python getGeneInfo.py [-h] [-f FILE] [-g GENES [GENES ...]]

ARGUMENTS
     -f FILE, --file FILE:   Path to the GenBank file
     -g GENES [GENES ...], --genes GENES [GENES ...]: Name(s) of the gene(s) to print info
"""
from Bio.SeqIO import parse
from Bio.SeqRecord import SeqRecord
import argparse

# Functions
def get_coords(record:SeqRecord, gene:str):
    """
    Iterates over the GenBank *record* features until
    it finds the one with the name *gene* and parse the
    location atribute to get the gene's coords

    Args:
        record(SeqRecords): The SeqRecord object returned
        by SeqIO.parse.
        gene(str): The name of the gene to get the coords
    
    Returns:
        A tuple containing the (start,end) coords of the gene
    """
    for ft in record.features:
        if ft.type == "gene" and ft.qualifiers.get("gene")[0] == gene:
            coords = ft.location
            return((int(coords.start),int(coords.end)))
    

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to the GenBank file", type=str)
parser.add_argument("-g", "--genes", help="Name(s) of the gene(s) to print info", type=str, nargs='+')
args = parser.parse_args()

# Main
for gb_record in parse(args.file, format='genbank'):
    for gene in args.genes:
        if not (coords := get_coords(gb_record, gene)):
            print(f"# Gene {gene} not found in any record")
        seq = gb_record.seq[coords[0]:coords[1]]
        print(f"# Gene {gene}\n>Seq\n{seq}\n>Transcription\n{seq.transcribe()}\n>Translation\n{seq.translate()}")