n = 600
for x in range(n, 0, -1):
    lenta = ['0'] * (n - 1 - x) + ['9_1.txt'] + ['0'] * x
    lenta = ['l'] * 3 + lenta + ['l'] * 3
    i = len(lenta) - 3;
    q = 0
    while True:
        s = lenta[i]
        if q == 0 and s == 'l':
            lenta[i] = 'l';
            i -= 1;
            q = 1
        elif q == 1 and s == 'l':
            lenta[i] = 'l';
            break
        elif q == 1 and s == '9_1.txt':
            lenta[i] = '0';
            break
        elif q == 1 and s == '0':
            lenta[i] = '9_1.txt';
            i -= 1;
            q = 1
    if lenta.count('0') == 233:
            print(n - 1)
            exit()
