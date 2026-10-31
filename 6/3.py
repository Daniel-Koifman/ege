from turtle import *

screensize(2_000, 2_000, 'black')
color('blue')
k = 30
tracer(0)
width(2)

for x in range(3):
    pendown()

    for y in range(2):
        forward(10 * k)
        right(90)
        forward(10 * k)
        right(90)
    penup()

    forward(10 * k)
    right(90)
    forward(5 * k)
    left(90)

penup()
t = 50
for x in range(-t, t):
    for y in range(-t, t):
        goto(x * k, y * k)
        dot(2, 'white')
done()
