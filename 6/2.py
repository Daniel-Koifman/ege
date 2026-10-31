from turtle import *
screensize (20_000, 20_000, 'black')
k = 20
tracer(0)
color('red')
width(1)

for x in range(4):
    forward(19 * k)
    left (180)
    backward(10 * k)
    right(90)

penup()


bk(5 * k)
lt (90)
fd(4 * k)
rt(90)

pendown()
color('green')

for x in range(2):
    fd(15 * k)
    lt(90)
    fd(8 * k)
    lt(90)


penup()
t=30
for x in range(-t,t):
    for y in range(-t,t):

        dot(2, 'white')
        goto(x * k, y * k)




























done ()