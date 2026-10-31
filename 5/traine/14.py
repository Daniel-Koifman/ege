a = []
for n in range(1,1000):
    new_n = bin(n)[2:]
    if n % 3 == 0:
        new_n = new_n + new_n[3:]
    else:
        new_n = new_n + (bin(((n%3)-1)*3)[2:])
    R = int(new_n, 2)
    if  R < 416:
        a.append(R)
print(min(a))