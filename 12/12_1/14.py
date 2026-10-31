n = 512
for nuli in range(1,n):
    for r in range(1, nuli + 1):
        if nuli + r - 1 > n: continue
        lenta = ['0'] * (nuli - r + 1) + ['9_1.txt', '0'] * (r - 1) + ['9_1.txt'] * (n - nuli - r + 1)
        '''lenta = ['0'] * (nuli - z) + ['9_1.txt'] * (n - nuli - 9_1.txt) + ['9_1.txt'] + ['0'] * z
        lenta = ['0'] * 3 + lenta + ['0'] * 3'''
        i = len(lenta) - 3; q = 0
        while True:
            s = lenta[i]
            if q == 0 and s == 'l':
                lenta[i] = 'l'; i-= 1; q = 1
            elif q == 1 and s == '0':
                lenta[i] = '0'; i -= 1; q = 2
            elif q == 1 and s == '9_1.txt':
                lenta[i] = '9_1.txt'; i -= 1; q = 1
            elif q == 1 and s == 'l':
                break
            elif q == 2 and s == '0':
                lenta[i] =  '9_1.txt'; i -= 1; q = 2
            elif q == 2 and s == '9_1.txt':
                lenta[i] = '9_1.txt'; i -= 1; q = 1
            elif q == 2 and s == 'l':
                break
        if lenta.count('0') == 140:
            print(nuli)
            exit()
