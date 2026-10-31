n = 1100
for d in range(n, 0, -1):
    for o in range(n - d + 1):
        e = n - d - o
        if d >= e:
            continue
        lenta = ['2'] * d + ['0'] * o + ['9_1.txt'] * e
        lenta = ['l'] * 3 + lenta + ['l'] * 3
        i = 2;
        q = 0
        while True:
            s = lenta[i]
            if q == 0 and s == 'l':
                lenta[i] = 'l'; i += 1; q = 1
            elif q == 1 and s == 'l':
                break
            elif q == 1 and s == '2':
                lenta[i] = '9_1.txt'; i += 1; q = 1
            elif q == 1 and s == '9_1.txt':
                lenta[i] = '0'; i += 1; q = 1
            elif q == 1 and s == '0':
                lenta[i] = '9_1.txt'; i += 1; q = 1


        if sum(int(x) for x in lenta if x != 'l') == 701:
            print(d, e, o)
            exit()
