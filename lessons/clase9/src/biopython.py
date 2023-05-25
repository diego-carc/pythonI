from Bio.Seq import Seq 

my_sequence = Seq('ATCGGATGATCGATAGCTAGCTATATTCGAT')
print(my_sequence.reverse_complement())