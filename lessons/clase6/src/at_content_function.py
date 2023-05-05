def at_content(dna = str, r = int(2)):

    dna = dna.upper()

    a_count= dna.count('A')
    t_count = dna.count('T')
    sequence_length = len(dna)

    at_content = round((a_count+t_count)/sequence_length*100, r)

    return(at_content)

print(at_content(input('Ingrese la cadena de DNA: '),
                 int(input('Ingrse el número de decimales para redondear: '))))
