F = {}
F[0] = 0
for n in range(1, 1000 + 1):
    if n % 2 == 0 and n > 0:
        F[n] = F[n / 2]
    if n % 2 == 1:
        F[n] = 1 + F[n - 1]
print (F)
c = 0
for n in range(1, 1000 + 1):
    if F[n] == 3:
        c += 1
print (c)