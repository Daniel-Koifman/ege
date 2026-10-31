F = {}
for n in range(-1000, 1000 + 1):
    if n < 10:
        F[n] = n
    else:
        F[n] = n ** 3 + F[n - 11]
print (F[900] - F[856])

