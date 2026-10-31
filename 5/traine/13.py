a = []
def f(n):
    s = ''
    while n > 0:
        s = str(n%4) + s
        n //= 4
    return s
for n in range(1,1000):
    new_n = f(n)
    if n %4 == 0:
        new_n = new_n + new_n[2:]
    if n%4 != 0:
        new_n = new_n + f((n%4)*2)
    R = int(new_n, 4)
    if R < 369:
        a.append(n)
print(max(a))