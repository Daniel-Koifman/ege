count = 0
for s in open('1.txt'):
    a = list(map(int, s.split()))
    ch = [a.count(i) for i in a]
    if ch.count(3) == 3 and ch.count(1) == 4:
        p = [a[i] for i in range(len(a)) if ch[i] == 3][0]
        print(ch,a,p)



    '''
    
        
        np = [a[i] for i in range(len(a)) if ch[i] == 1]
        if sum(np) / len(np) <= p:
            count = sum(a)
print(count)'''
