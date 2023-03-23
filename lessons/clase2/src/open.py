my_file_name = "../data/dna.txt"

my_file = open(my_file_name)

my_file_contents = my_file.read()

print(f'La secuencia de DNA es: {my_file_contents}\ny su longitud es: {len(my_file_contents)}')

