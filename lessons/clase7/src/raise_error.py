import re

dna = 'CTGCATTATATCGTACGAAATTATACGCGCG'
matches = re.finditer(r'[AT]{5,}', dna)
for match in matches:
    print(f'{match.group()} found at position {match.start()}')

dna = 'CTGCATTATATCGTACGAAAAAAATTAATTTTTTACGCGCG'
matches = re.finditer(r'((A{5,})|(T{5,}))', dna)
for match in matches:
    print(f'{match.group()} found at position {match.start()}')

dna = "CGCTCnTAGATGCGCrATGACTGCAyTGC" 
result = re.split(r"[^ATGC]", dna) 
print(result)