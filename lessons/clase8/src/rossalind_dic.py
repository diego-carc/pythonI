import re

input_string = open('..\doc\lyrics.txt').read()

words = set(re.split(r'[ \n,!?()]', input_string))

rossalind_dic = {word : input_string.count(word) for word in words}

for key, value in sorted(rossalind_dic.items()):
    print(f'{key} : {value}')

