for n in range(1, 10000):
    lenta = list(bin(n)[2:])
    lenta = ['l'] * 3 + lenta + ['l'] * 3
    i = 2; q = 0
    while True:
        s = lenta[i]
        if q == 0 and s == 'l':
            lenta[i] = 'l'; i += 1; q = 1
        elif q == 1 and s == 'l':
            lenta[i] = '0'; i -= 1; q = 2
        elif q == 1 and s == '0':
            lenta[i] = '0'; i += 1; q = 1
        elif q == 1 and s == '9_1.txt':
            lenta[i] = '9_1.txt'; i += 1; q = 1
        elif q == 2 and s == 'l':
            lenta[i] = '9_1.txt'; i -= 1; q = 3
        elif q == 2 and s == '0':
            lenta[i] = '9_1.txt'; i -= 1; q = 2
        elif q == 2 and s == '9_1.txt':
            lenta[i] = '9_1.txt'; i -= 1; q = 2
        elif q == 3 and s == 'l':
            lenta[i] = '0'; i -= 1; q = 4
        elif q == 4 and s == 'l':
            lenta[i] = '9_1.txt'; break
    res = ''.join(lenta).replace('l', '')
    if int(res, 2) <= 903:
        print(int(res, 2))

        def f4(n):
            s = ''
            while n > 0:
                s = s + str(n%4)
                n = int(n/4)
