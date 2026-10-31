a = []
for k in range(100, 1000):
    new_n = str(k)
    r = []
    r.extend([(int(new_n[0])), (int(new_n[1])), (int(new_n[2]))])
    s1 = int(new_n[0]) ** 2 + int(new_n[1]) ** 2
    s2 = int(new_n[1]) ** 2 + int(new_n[2]) ** 2
    s = str(max (s1, s2)) + str(min(s1, s2))
    if int(s) == 13085:
        a.append(k)
print(max(a))