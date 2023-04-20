class AmbiguousBaseError(Exception):
    pass

def get_at_content(dna=''):
    length = len(dna)

    if not length:
        raise AmbiguousBaseError(f'The sequence is empty') 
    if dna.count('N') > 0:
        raise AmbiguousBaseError(f'Sequence contains {dna.count("N")} N\'s')
 
    a_count = dna.count('A')
    t_count = dna.count('T')
    
    return((a_count + t_count) / length)

sequences = ['ATCATCGATCGATCGAT', 'ATCGATGCN', 'ATCG', '']

for seq in sequences:
    try:
        print(f'AT content for {seq} is {get_at_content(seq)}')
    except AmbiguousBaseError as ex:
        print(f'skipping invalid sequence: {ex.args[0]}')



