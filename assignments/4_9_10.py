from turtle import*
bgcolor("green")
pensize(3)
color("hotpink")
speed(-1)

def draw_star():    
    for i in range(5):
        forward(100)
        right(144)
    

for i in range(5):
    draw_star()
    up()
    forward(350)
    right(144)
    down()
    
