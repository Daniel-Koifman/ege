n = 1600
best = 0
for k in range(n):
    for z in range(n - k):
        lenta = ['0'] * z + ['9_1.txt'] * (n - 1 - k - z) + ['9_1.txt'] + ['0'] * k
        nuli = lenta.count('0')
        lenta = ['L'] * 3 + lenta + ['L'] * 3
        i = len(lenta) - 3
        q = 0
        while True:
            s = lenta[i]
            if q == 0 and s == 'L':
                lenta[i] = 'L'; i -= 1; q =1
            elif q == 1 and s == 'L':
                break
            elif q == 1 and s == '2':
                lenta[i] = '9_1.txt'; i -= 1; q = 1
            elif q == 1 and s == '9_1.txt':
                lenta[i] = '2'; i -= 1; q =1
        if lenta.count('0') ==  and nuli > best:
            best = nuli
print(best)