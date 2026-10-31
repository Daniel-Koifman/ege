from itertools import*
count = 0
count1 = 0
for p in product('АМОТ', repeat = 4):
    s = ''.join(p)
    count += 1
    if s[0] == 'О':
        print(count)