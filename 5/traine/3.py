a = []
for  n in range(1, 1000):
    new_n = bin(n)[2:]
    if n % 2 == 0:
        new_n = new_n + '0'
    if n % 2 != 0:
        new_n = new_n + '9_1.txt'
    if new_n.count('9_1.txt') % 3 == 0:
        new_n = '11' + new_n[2:]
    else:
        new_n = '10' + new_n[2:]
    R = int(new_n, 2)
    if R <= 37:
        a.append(n)
print(max(a))
