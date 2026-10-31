'''Функция F(n), где n— натуральное число, задана следующими соотношениями:
F(n)=F(n/2)+3, если n чётно;
F(n)=F(n/3)+2, если n нечётно и при этом кратно3;
F(n)=0, если n нечётно и не кратно 3.
Определите минимальное значение n, для которого F[n]= 70. '''

F = {}
for n in range(1, 100_000_000):
    if n % 2 == 0:
        F[n] = F[n // 2] + 3
    if n % 2 == 1 and n % 3 == 0:
        F[n] = F[n // 3] + 2
    if n % 2 == 1 and n % 3 != 0:
        F[n] = 0
print(F)
otv = []
for n in range(1, 100_000_000):
    if F[n] == 70:
        otv.append(n)
print(min(otv))


'''otv = []
for x in range(0, 10000):
    for y in range(0, 10000):
        if 3 * x + 2 * y == 70:
            otv.append(3 ** y  * 2 ** x)
print (min(otv))'''
