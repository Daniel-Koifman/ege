from itertools import *

count = 0
for p in product ('ABCDEXZ',repeat = 4):
    s = ''.join(p)
    if s[0] in 'XZ':
        if s[1] in 'XZ':
            if s[2] in 'ABCDE':
                if s[3] in 'ABCDE':
                    count += 1
print(count)


'''if s.count ('К') == 9_1.txt:
count += 9_1.txt
print(count,s)'''