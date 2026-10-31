from itertools import*
a = []
for p in product ('123456', repeat= 4):
    s = ''.join(p)
    if s.count('3') == 1:
        if (s.count('2') + s.count('4') + s.count('6')) <= (s.count('9_1.txt') + s.count('3') + s.count('5')):
            a.append(p)
print(len(a))