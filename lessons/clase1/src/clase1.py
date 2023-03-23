'''
Clase 16/03/2023
Introducción 
Strings
'''

dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
codon_inicio = 'TAC'
codon_final = 'ATT'

print(f'El codón de inicio está en la posición {dna.find(codon_inicio)}')

pos = dna.find(codon_inicio)
print('El codón de inicio está en la posición', pos)

mensaje = 'Buenos días'
print(mensaje)

mensaje = mensaje.replace('días', 'noches')
mensaje = mensaje.replace('nos', 'nas')
print(mensaje)

print(mensaje[1:5])
print(mensaje[7:])
print(mensaje[:10])
print(mensaje[:-12])

print(f'La secuencia que se transcribe es: {dna[dna.find(codon_inicio):dna.find(codon_final)]}')

'''
Clase 23/03/2023
'''

exon = 'ATCGCGATCGCTAGCGTTACGCTACG'

print(f'El fragmento de exon es: {exon}')
print(f'La longitud del exon es: {len(exon)}')
print('La longitud del exon es:', len(exon))

nucleotides = ['A', 'T', 'C','G']
for nucleotide in nucleotides:
    print(f'{nucleotide}: {exon.count(nucleotide)}')