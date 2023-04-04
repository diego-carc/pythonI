'''
NAME
    from_raw_to_fasta.py
  
VERSION
    1.0  29/03/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa recibe la ruta a un archivo de texto plano con 
una secuencia de DNA y lo convierte a formato fasta.

CATEGORY
   Sequence    

USAGE

    % python from_raw_to_fasta.py
    
    El programa pedirá 3 datos :
    
    a) archivo de entrada. Formato raw, que es la secuencia de DNA en una sola linea
                            El nombre incluye path y nombre del archivo
    b) identificador. Nombre o identificador de la secuencia, y será colocado como id en el formato fasTA
    c) archivo de salida. Se colocará la secuencia formateada en fastA. Se debe incluir path y nombre del archivo.

ARGUMENTS
    None    

SEE ALSO

'''

# Recibir del teclado el archivo de de secuencia en formato raw
input_file_name = input("Ingrese el nombre del archivo con la secuencia de DNA: ")

# Pedir el identificador para la secuencia
identifier = input("Ingrese el nombre o identificador de la secuencia: ")

# Pedir el nombre del archivo de salida y crearlo
output_file_name = input("Ingrese el nombre para el archivo de salida (formato fastA): ")
fp_output = open(f'{output_file_name}.fasta', 'w') 

# Abrir y leer archivo de entrada con secuencia
fp_input = open(input_file_name)
dna_sequence = fp_input.read().rstrip('\n')

# Guardar secuencia en formato fastA
fp_output.write(f"> {identifier}\n{dna_sequence}\n")

fp_input.close()
fp_output.close()

print(f'El archivo {output_file_name} se ha creado correctamente')
