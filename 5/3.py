a = []
for n in range (1, 1000):
    new_n = bin(n)[2:]
    if n % 2 == 0:
        new_n = new_n.replace('9_1.txt', '11')
    if n % 2 != 0:
        new_n = new_n.replace('0', '00')
    R = int(new_n, 2)
    if R < 70 and R != n:
        a.append(n)
print(max(a))