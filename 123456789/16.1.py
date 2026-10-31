F = {}
F[1] = 1
for n in range(2, 10000):
    if n % 2 == 0:
        F[n] = n + F[n - 1]
    if n % 2 == 1 and n > 1:
        F [n] = 2 * F[n-2]
print (F[26])
