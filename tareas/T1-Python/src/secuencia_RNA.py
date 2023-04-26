'''
NAME
    secuencia_RNA.py
  
VERSION
    1.1  26/04/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa identifica los codones de inicio y término en una
cadena de DNA e imprime la secuencia entre ellos.

CATEGORY
   Sequence    

USAGE

    % python secuencia_RNA.py
    
ARGUMENTS
    None    

SEE ALSO

'''

# Declarar las secuencias de interés
dna_sequence = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
initiation_codon = 'TAC'
termination_codon = 'ATT'

# Imprimir el output
print(f'La secuencia de DNA es: {dna_sequence}\n'
      # Usar el método find para encontrar la posición del codón
      f'El codón de inicio "{initiation_codon}" se encuentra en la posición: {dna_sequence.find(initiation_codon)}\n' 
      f'EL codón de término "{termination_codon}" se encuentra en la posición: {dna_sequence.find(termination_codon)}\n'
      f'La secuencia que se transcribirá en RNA es: {dna_sequence[dna_sequence.find(initiation_codon):dna_sequence.find(termination_codon)]}' 
      )