F = {}
F[1] = 1
for n in range (2, 10000):
    F[n] = n * F[n - 1]
print (((F[3000]//150)+F[2999])/F[2998])