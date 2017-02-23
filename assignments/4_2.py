from turtle import*
color("hotpink")
bgcolor("green")
pensize(3)
def draw_square(length,quantity):
    for i in range(4):
        forward(length*quantity)
        left(90)
quantity=5
length=20

for i in range(quantity):
    draw_square(length,i+1)
    n=length/2*(i+1)
    up()
    setposition(-n,-n)
    down()


