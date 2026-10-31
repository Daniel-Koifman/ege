a = []
for n in range (1, 1000):
    new_n = bin(n)[2:]
    if n % 4 == 0:
        new_n = new_n + new_n
    if n % 4 != 0:
        new_n = new_n + new_n[::-1]
    R = int(new_n, 2)
    if R >= 544:
        a.append(n)
print(min(a))
        