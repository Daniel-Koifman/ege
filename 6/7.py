from turtle import *
screensize(5000,5000)
r = 30
tracer(0)
down()
for i in range(2):
    fd(21*r)
    rt(90)
    fd(32*r)
    rt(90)
up()

for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(4, 'red')
done()