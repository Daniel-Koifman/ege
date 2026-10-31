from itertools import *
count = 0
for p in product ('АГИНРТ', repeat = 6):
    s = ''.join(p)
    count += 1
    if count % 2 == 0:
        if s[0] not in 'АГ':
            if s.count ('Т') == 1:
                if s.count ('А') <= 1:
                    print (count, s)
                    break