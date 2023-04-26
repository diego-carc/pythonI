'''
NAME
    contar_nucleotidos.py
  
VERSION
    1.1  26/04/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa recibe del teclado una secuencia de DNA y cuenta el
contenido de A's, T's, C's y G's.

CATEGORY
   Sequence    

USAGE

    % python contar_nucleotidos.py

    El programa recibirá:
      
      a) La secuencia de DNA como un string desde el teclado.
    
ARGUMENTS
    None    

SEE ALSO

'''

# Recibir secuencia de DNA desde el teclado
dna_sequence = input('Ingrese la secuencia de DNA: ')

# Imprimir el output
print(f'El contenido de los nucleótidos es:\n'
       f'A: {dna_sequence.count("A")}\n'
       f'T: {dna_sequence.count("T")}\n'
       f'C: {dna_sequence.count("C")}\n'
       f'G: {dna_sequence.count("G")}'
       )

