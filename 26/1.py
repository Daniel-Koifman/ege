f = open('26var02.txt')
n,m = map (int, f.readline().split())
a = sorted(int(f.readline()) for _ in range(n))
b = sorted(int(f.readline()) for _ in range(m))
k = 0
for p in b:
    if k<n and a[k] <= p:
        k+=1
mx = [x for x in a if x <= b [-1]]
print (k, max(mx))