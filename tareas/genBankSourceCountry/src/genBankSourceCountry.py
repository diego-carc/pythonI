"""
NAME
    genBankSourceCountry.py
  
VERSION
    1.0  27/09/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa recibe un archivo GenBank, ya sea en forma de path o ID, y lo parsea
    para obtener el isolation source al que pertenece así como la fecha de creación.
    

CATEGORY
   Sequence    

USAGE

    % python genBankSourceCountry.py [-h] [-g GENBANK] [-f] [-e EMAIL]

ARGUMENTS
    -g GENBANK, --genBank GENBANK : ID of the GenBank or path to the file. 
                                    If passing a path use -f
    -f, --file : Use this flag id passing a file path to --genBank
    -e EMAIL, --email EMAIL Email to access Entrez. Only required when --genBank is ID  
"""

# Imports
from Bio import Entrez
from Bio import SeqIO
import argparse

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--genBank", help="ID of the GenBank or path to the file.\
                     If passing a path use -f")
parser.add_argument("-f", "--file", help="Use this flag id passing a file path to --genBank", action="store_true")
parser.add_argument("-e", "--email", help="Email to access Entrez. Only required when --genBank is ID", required=False)
args = parser.parse_args()
Entrez.email = args.email

# Parse GenBank 
if args.file:
     try: record = SeqIO.parse(args.genBank, format="genbank")
     except:
          print(f"The file {args.genBank} doesn't exist")
          exit()
else:
    with Entrez.efetch("nucleotide", id=args.genBank, rettype="gb") as handle:
        for gb_record in SeqIO.parse(handle, format='genbank'):
            for f in gb_record.features:
                for k,v in f.qualifiers.items():
                    if k != "country" and k != "isolation_source": continue
                    print(f"{k} : {v[0]}")
            
    exit()

for gb_record in record:
            for f in gb_record.features:
                for k,v in f.qualifiers.items():
                    if k != "country" and k != "isolation_source": continue
                    print(f"{k} : {v[0]}")




