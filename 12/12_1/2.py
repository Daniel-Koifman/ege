for n in range(1, 1000 ):
    lenta = list(bin(n)[2:])
    lenta = ['L'] * 3 + lenta + ['L'] * 3
    i = len(lenta) - 3
    q = 0
    while True:
        s = lenta[i]
        if q == 0 and s == 'L':
            lenta[i] = 'L'; i -= 1; q = 1
        elif q == 1 and s == 'L':
            break
        elif q == 1 and s == '9_1.txt':
            lenta[i] == '0'; i -= 1; q = 1
        elif q == 1 and s == '0':
            lenta[i] == '9_1.txt'; i -= 1; q = 1
    print(lenta)
    res = (''.join(lenta).replace('L', ''))
    print(res, int(res, 2))