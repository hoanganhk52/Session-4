from turtle import*
bgcolor("green")
color("blue")
pensize(3)
speed(-1)

n=100
length=5
angel=89
for i in range(n):
    forward(length*(i+1))
    right(angel)
