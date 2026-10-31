from itertools import *

count = 0
for p in product ('КОТ',repeat = 6):
    s = ''.join(p)
    if s.count ('К') == 1:
        count += 1
        print(count,s)



