'''
T4-Python: From raw to fasta

Autor: Diego Carmona Campos

Última Actualización: 29/03/2023

Descripción:
El programa recibe la ruta a un archivo de texto plano con 
una secuencia de DNA y lo convierte a formato fasta.
'''

# Recibo del teclado el archivo de texto y los datos para crear el archivo fasta
ruta = input("Ingrese la ruta al archivo con la secuencia de DNA: ")
nombre = input("Ingrese el nombre para el archivo de salida: ")
secuencia = input("Ingrese el nombre para la secuencia en el archivo fasta: ")

# Abro el archivo de texto
archivo = open(ruta)

# Creo un nuevo archivo para escritura
nuevo = open(f'{nombre}.fasta', 'w') 

salto_de_linea = '\n' # Uso la variable para eliminar último salto de línea

# Escribo en el archivo la secuencia y su nombre
nuevo.write(f"> {secuencia}\n{archivo.read().rstrip(salto_de_linea)}")

# Cierro los archivos
archivo.close()
nuevo.close()

print('El archivo se ha convertido correctamente')