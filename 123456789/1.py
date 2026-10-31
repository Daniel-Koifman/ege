f = {}
for n in range(-10000, 10000):
    f[1] = 1
    if n > 1:
        f[n] = f[n - 1] + 1 + 2*n
print(f[2024]-f[2022])