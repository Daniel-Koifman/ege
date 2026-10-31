print ('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for F in range(2):
                    F = not (x <= w) or (y == z) or y
                    if F == False:
                        print(x,y,z,w,F)