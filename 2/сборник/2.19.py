print ('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for F in range(2):
                    F = ((x <= y) <= z) or (w <= (y and z))
                    if F == False:
                        print(x,y,z,w,F)