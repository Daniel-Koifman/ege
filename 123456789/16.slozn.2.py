F = {}
G = {}
for n in range (1, 43000 + 1):
    if n <= 7:
        F[n] = n
        G[n] = n
    if n > 7:
        F[n] = G[n-3] * 3
        G[n] = G[n - 1] + 4
print (F[43000])



