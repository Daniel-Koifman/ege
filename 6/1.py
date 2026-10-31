from turtle import *
screensize(20_000, 20_000, 'white')
color('red')
k = 30
tracer(1)
width(2)

for x in range(4):
    forward(9 * k)
    left(180)
    backward(10 * k)
    right(90)

penup()
backward(7 * k)
left(90)
forward(3 * k)
right(90)
pendown()

color('pink')
for x in range(2):
    forward(17 * k)
    left(90)
    forward(20 * k)
    left(90)

penup()
t = 25
for x in range(-t, t):
    for y in range(-t, t):
        goto(x * k, y * k)
        dot(2, 'black')

done()