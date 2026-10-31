from itertools import *

count = count2 = 0
for p in product('123456', repeat=5):
    s = ''.join(p)
    count += 1
    if s.count('3') == 1:
        if s.count('9_1.txt') <= 1:
            if s.count('2') <= 1:
                if s.count('4') <= 1:
                    if s.count('5') <= 1:
                        if s.count('6') <= 1:
                            if s.count ('2') + s.count ('4') + s.count ('6') <= s.count ('9_1.txt') + s.count ('3') + s.count ('5'):
                                count2 += 1
print(count2, s)
