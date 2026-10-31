from itertools import *

count = 0
for p in product('01234567', repeat=5):
    s = ''.join(p)
    if s[0] != '0':
        if s.count('4') == 1:
            if s.count ('04') == 0:
                if s.count('24') == 0:
                    if s.count('44') == 0:
                        if s.count('64') == 0:
                            if s.count('46') == 0:
                                if s.count('42') == 0:
                                    if s.count('40') == 0:
                                        count += 1
                                        print(count, s)