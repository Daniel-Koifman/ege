from itertools import *
count =0
for p in product('0123456789ABCDEF',repeat=5):
    s = ''.join(p)
    if s[0] != '0':
        if s.count ('0') == 1:
            if s.count ('01') == 0:
                if s.count('10') == 0:
                    if s.count('30') == 0:
                        if s.count('50') == 0:
                            if s.count('70') == 0:
                                if s.count('90') == 0:
                                    if s.count('B0') == 0:
                                        if s.count('D0') == 0:
                                            if s.count('F0') == 0:
                                                if s.count('03') == 0:
                                                    if s.count('05') == 0:
                                                        if s.count('07') == 0:
                                                            if s.count('09') == 0:
                                                                if s.count('0B') == 0:
                                                                    if s.count('0D') == 0:
                                                                        if s.count('0F') == 0:



                                                                                count += 1
print(count)