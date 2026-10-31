print('x y w z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for F in range(2):
                    F = ((x <= y) <= w) or (z <= (y and w))
                    if F == False:
                        print(x,y,w,z, F)

