from itertools import *

count = 0
for p in product('АБВГЕИО', repeat=6):
    s = ''.join(p)
    if s.count('А') + s.count('Е') + s.count('И') + s.count('О') > s.count('Б') + s.count('В') + s.count('Г'):
        if s[0] in 'БВГ':
            count += 1
print(count)
