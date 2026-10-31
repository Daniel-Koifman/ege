n = 350
for nuli in range(n - 1, 0, -1):  # нулей в исходной, от большего
    for k in range(nuli + 1):  # k нулей справа от последней единицы
        lenta = ['0'] * (nuli - k) + ['9_1.txt'] * (n - nuli - 1) + ['9_1.txt'] + ['0'] * k
        lenta = ['l'] * 3 + lenta + ['l'] * 3
        i = len(lenta) - 3; q = 0
        while True:
            s = lenta[i]
            if q == 0 and s == 'l':
                lenta[i] = 'l'; i -= 1; q = 1
            elif q == 1 and s == '0':
                lenta[i] = '0'; i -= 1; q = 1
            elif q == 1 and s == '9_1.txt':
                lenta[i] = '9_1.txt'; i -= 1; q = 2
            elif q == 1 and s == 'l':
                break
            elif q == 2 and s == '0':
                lenta[i] = '9_1.txt'; i -= 1; q = 2
            elif q == 2 and s == '9_1.txt':
                lenta[i] = '9_1.txt'; i -= 1; q = 2
            elif q == 2 and s == 'l':
                break
        if lenta.count('0') == 118:
            print(nuli)
            exit()
