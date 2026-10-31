F = {}
F[1] = 1
F[2] = 2
for n in range(3, 100):
    if n > 2 and n % 2 == 0:
        F[n] = int((4 * n - F[n - 3]) / 8)
    if n % 2 == 1 and n > 2:
        F[n] = int((4 * n - F[n - 1] + F[n - 2]) / 8)
print(F[52] - F[38])
