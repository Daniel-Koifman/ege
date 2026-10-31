F = {}
F[1] = 1
F[2] = 1
for n in range (3, 10000):
    F[n] = F[n -1] * n-2 * F[n-2]
print (F[6])