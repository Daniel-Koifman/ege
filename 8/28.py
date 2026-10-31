from itertools import*
count = 0
for p in product('АВКОМС', repeat = 6):
    s = ''.join(p)
    count += 1
    if count % 2 == 0:
        if s[0] != 'А':
            if s[0] != 'В':
                if s[0] != 'К':
                    if s.count ('К') == 2:
                        if s.count ('КК') == 0:
                            print(count)
