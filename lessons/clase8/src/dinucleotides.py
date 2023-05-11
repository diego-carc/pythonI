dna_sequence = 'ATCGCGCATCGCGGCATAGATCGATACGATCAGATATATTAGCCATAGCGATAGATCGCGCGCATGAGATCGATCGGTATCGAT'

dinucleotide_dic = {}
for i in range(len(dna_sequence) - 1):
    dinucleotide =dna_sequence[i:i+2]
    dinucleotide_dic[dinucleotide] = dna_sequence.count(dinucleotide)

for key, value in dinucleotide_dic.items():
    if value >= 2:
        print(f'{key}:{value}')

