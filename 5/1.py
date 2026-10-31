a = []
for n in range(1, 1000):
    new_n = bin(n)[2:]
    if n % 3 == 0:
        new_n = new_n + new_n[-3:]
    if n % 3 != 0:
        new_n = new_n + bin(((n % 3) - 1) * 3)[2:]
    r = int(new_n, 2)
    if r < 416:
        a.append(r)
print(max(a))
