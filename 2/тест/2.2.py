print ('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                 F = ((x and w) or (w and z)) == ((z <= y) and (y <= x))
                 if F == True:
                    print(x,y,z,w,F)