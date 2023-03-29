'''
Este programa recibe del usuario una secuencia de DNA y cuenta el
contenido de cada nucleótido.
'''

# Uso la función input() para recibir una entrada del teclado
dna = input('Ingrese la secuencia de DNA: ')

# Utilizo fstrings dentro de la función print para imprimir el output
print(f'El contenido de los nucleótidos es:\n'
      # El método count de un string me permite contar las repeticiones de un caracter
       f'A: {dna.count("A")}\n'
       f'T: {dna.count("T")}\n'
       f'C: {dna.count("C")}\n'
       f'G: {dna.count("G")}'
       )

