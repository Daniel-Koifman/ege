from itertools import *

count = 0
for p in product('0123', repeat=5):
    s = ''.join(p)
    if s[0] != '0':
        if s.count('3') == 1:
            if s.count ('03') == 0:
                if s.count('30') == 0:

                    count += 1
print(count, s)

