from itertools import *

count = count2 = 0
for p in product('0123456789', repeat=4):
    s = ''.join(p)
    count += 1
    if s[0] != '0':
        if s[-1] in '02468':
            if s.count('0') == 1:
                if s.count ('00') == 0:
                    if s.count('02') == 0:
                        if s.count('20') == 0:
                            if s.count('40') == 0:
                                if s.count('04') == 0:
                                    if s.count('06') == 0:
                                        if s.count('60') == 0:
                                            if s.count('08') == 0:
                                                if s.count('80') == 0:
                                                    count2 += 1
                                                    print(count2, s)
