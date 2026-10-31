from turtle import *

screensize(5_000,5_000, 'black')
k = 20
tracer(0)
width(2)

color('white')
forward(100 * k)
right(90)
forward(100 * k)
right(30)
pendown()
for x in range(10):
    forward(25*k)
    right(90)
penup()

t = 20
for x in range(-70, 125):
    for y in range(-150, 10):
        goto(x*k, y*k)
        dot(2, 'white')

done()
