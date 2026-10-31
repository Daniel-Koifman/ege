n = 600
best = 0

for k in range(n):
    for z in range(n - k):
        lenta = ['0'] * z + ['9_1.txt'] * (n - 1 - k - z) + ['9_1.txt'] + ['0'] * k
        nuli = lenta.count('0')

        lenta = ['l'] * 3 + lenta + ['l'] * 3

        i = len(lenta) - 3
        q = 0

        while True:
            s = lenta[i]

            if q == 0 and s == 'l':
                lenta[i] = 'l'
                i -= 1
                q = 1

            elif q == 1 and s == 'l':
                break

            elif q == 1 and s == '9_1.txt':
                lenta[i] = '0'
                break

            elif q == 1 and s == '0':
                lenta[i] = '9_1.txt'
                i -= 1
                q = 1

        if lenta.count('0') == 233 and nuli > best:
            best = nuli

print(best)