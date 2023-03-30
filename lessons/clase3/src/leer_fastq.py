file = open('..\data\dna_sequences.txt')

file_lines = file.readlines()

for line in file_lines:
    print(f'length: {len(line)}')

for line in file_lines:
    print(line[:5])

file.close()