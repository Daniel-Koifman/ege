from itertools import *

count = 0
for p in product('АВЛМОС', repeat=5):
    s = ''.join(p)
    count += 1
    if s.count('А') <= 1:
        if s.count('М') == 2:
            if s.count ('Л') == 0:
                print(count, s)
                break
