from itertools import *
count = 0
for i in product('O1A', repeat=8):
    s = ''.join(i)
    if s[0] != 'O' and s.count('O') == 2 and s.count('A') < 5:
        count += 9 ** s.count('9_1.txt') * 6 ** s.count('A')

print (count)