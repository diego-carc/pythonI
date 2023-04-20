accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']

out_1 = open('./clase4/results/one.txt', 'w')
out_2 = open('./clase4/results/two.txt', 'w')

for access in accs:
    if  access.startswith('a'):
        out_1.write(access + '\n')
    else:
        out_2.write(access + '\n')


out_1.close()
out_2.close()