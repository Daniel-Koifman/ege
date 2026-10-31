from itertools import *

count = count2 = 0
for p in product('АЕИКЛПР', repeat=6):
    s = ''.join(p)
    count += 1
    if count % 2 == 0:
        if s[0] != 'И':
            if s.count ('И') >= 2:
                count2 += 1
print(count2, s)
