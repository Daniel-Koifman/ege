from itertools import *

count = 0
for p in product('АВИКЛ', repeat=6):
    s = ''.join(p)
    count += 1
    if s.count('А') <= 2:
        if s.count('В') == 2:
            if s.count ('И') == 0:
                print(count, s)
                break
