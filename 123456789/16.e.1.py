F = {}
F[1] = 1
for n in range(2, 10000):
    if n % 2 == 0 and n > 2:
        F[n] = 2 * n * F[n - 1] + F[n - 3]
    if n % 2 == 1 and n > 1:
        F[n] = F[n - 2] * 3
print(F[2026] / F[2021])
