'''
T1-Python: Secuencia de RNA

Autor: Diego Carmona Campos
Última actualización: 27/03/2023

Descripción:
Este programa imprime la secuencia de RNA que se transcribirá dada una secuencia de DNA.
El codón de inicio que se utiliza es "TAC" y el codón de paro "ATT".
'''

# Declaro una variable que almacene la secuencia de interés
dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'

# Declaro variables que contengan los codones de interés
cod_ini = 'TAC'
cod_ter = 'ATT'

# Imprimo el output
print(f'La secuencia de DNA es: {dna}\n'
      # Uso el método find para encontrar la posición del codón
      f'El codón de inicio "{cod_ini}" se encuentra en la posición: {dna.find(cod_ini)}\n' 
      f'EL codón de término "{cod_ter}" se encuentra en la posición: {dna.find(cod_ter)}\n'
      # Uso la notación [:] para extraer una subcadena
      f'La secuencia que se transcribirá en RNA es: {dna[dna.find(cod_ini):dna.find(cod_ter)]}' 
      )