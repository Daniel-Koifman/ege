a = []
for n in range(1,1000):
    new_n = bin(n)[2:]
    if n % 4 == 0:
        new_n = new_n + new_n[-2:]
    else:
        new_n = new_n + (bin((n%4) + 1)[2:])
    R = int(new_n, 2)
    if R <= 986:
        a.append(n)
print(max(a))