from itertools import *

count = count2 = 0
for p in product('АЕЛРСТ', repeat=5):
    s = ''.join(p)
    count += 1
    if count % 2 == 1:
        if s[0] not in 'АСТ':
            if s.count('Е') == 2:
                if s.count('ЕЕ') == 0:
                    print(count, s)
                    