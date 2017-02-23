from turtle import*
color("hotpink")
bgcolor("green")
pensize(3)
def draw_square(length):
    for i in range(4):
        forward(length)
        left(90)
    

quantity=5
length=20

for i in range(quantity):
    draw_square(length)
    up()
    setposition(length*(2*(i+1)),0)
    down()
    
