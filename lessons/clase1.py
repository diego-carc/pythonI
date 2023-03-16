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
