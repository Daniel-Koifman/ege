from turtle import *

print('155')
screensize(20_000, 20_000, 'black')
k = 40
tracer(0)
width(2)
color('red')
for x in range(2):
    forward(9 * k)
    right(90)
    forward(5 * k)
    right(270)

backward(18 * k)
left(90)
forward(10 * k)
right(90)
penup()

forward(5 * k)
right(90)
forward(4 * k)
left(90)
pendown()

color('blue')

for x in range(4):
    forward(5 * k)
    right(90)
penup()

t = 25
for x in range(-t, t):
    for y in range(-t, t):
        dot(2, 'white')
        goto(x * k, y * k)

done()
