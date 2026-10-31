from itertools import *

count = count2 = 0
for p in product('АГИЛМНОФ', repeat=5):
    s = ''.join(p)
    count += 1
    if count % 2 == 1:
        if s[0] != 'И':
            if s.count('О') <= 1:
               count2 += 1
print(count2, s)

