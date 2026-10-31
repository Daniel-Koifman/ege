from itertools import *

count = count2 = 0
for p in product('АГЕИЛНРТ', repeat=5):
    s = ''.join(p)
    count += 1
    if count % 2 == 1:
        if s[0] != 'Т':
            if s.count('Н') == 1 or s.count('Н') == 2:
                count2 += 1
                print(count2, s)