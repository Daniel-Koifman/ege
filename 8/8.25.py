from itertools import *

count = count2 = 0
for p in product('АВКМОС', repeat=6):
    s = ''.join(p)
    count += 1
    if count % 2 == 0:
        if s[0] not in 'АВК':
            if s.count('К') == 2:
                if s.count('КК') == 0:
                    print(count, s)
                    break