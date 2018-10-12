# https://practice.geeksforgeeks.org/problems/save-ironman/0

import re
a = 'Ab?/Ba'
pattern = r'\w+'
matches = re.findall(pattern, a)
the_string = ''.join(matches)
print(the_string)
half_len = len(the_string) // 2
part_1 = list(the_string[:half_len+1])
part_2 = list(the_string[-half_len:])
part_2.reverse()
for char1, char2 in zip(part_1, part_2):
    #print(char1.upper(), char2.upper())
    if char1.upper() != char2.upper():
        print('False')
print('True')
