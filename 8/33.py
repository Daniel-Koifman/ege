from itertools import*
a = []
count = 0
for p in product('АВЛОПР', repeat =  4):
    s = ''.join(p)
    count += 1
    if s[0] == 'П':
        print(count)
        break