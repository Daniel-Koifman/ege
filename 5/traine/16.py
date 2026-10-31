a = []
for n in range(100, 1000):
    new_n = str(n)
    sm1 = (int(new_n[0])**2+int(new_n[1])**2)
    sm2 = (int(new_n[1])**2+int(new_n[2])**2)
    mn = str(max(sm1, sm2)) + str(min(sm1, sm2))
    if int(mn) == 9752:
        a.append(n)
print(max(a))