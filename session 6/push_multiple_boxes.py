p={}
p["x"] = 3
p["y"] = 3


boxes=[]
boxes.append({"x":1,"y":1})
boxes.append({"x":4,"y":2})
boxes.append({"x":6,"y":3})


gates=[]
gates.append({"x":1,"y":4})
gates.append({"x":5,"y":5})
gates.append({"x":7,"y":8})


map_width=10
map_height=10

def check_object(objects,x,y):
    for object in objects:
        if object["x"]==x and object["y"]==y:
            return True
    return False

def print_map(p,boxes,gates,map_width,map_height):
    for y in range(map_height):
        for x in range(map_width):
            if x==p["x"] and y==p["y"]:
                print("P ",end="")
            elif check_object(boxes,x,y):
                print("B ", end="")
            elif check_object(gates,x,y):
                print("G ",end="")
            else:
                print("_ ",end="")
        print()


def move(x,y,dx,dy):
    return [x+dx,y+dy]


def check_in_map(x,y,screen_width,screen_height):
    if x < 0 or y < 0 or x > screen_width-1 or y > screen_height-1:
        return False
    return True

def check_next_position(objects,x,y):
    for object in objects:
        if object["x"]==x and object["y"]==y:
            return object
    return None


while True:
    print_map(p,boxes,gates,map_width,map_height)

    choice=input("What is your choice? ").upper()
    dx=0
    dy=0
    if choice=="A":
        dx = -1
    elif choice=="D":
        dx = 1
    elif choice=="W":
        dy = -1
    elif choice=="S":
        dy = 1

    [next_px,next_py]=move(p["x"], p["y"],dx,dy)
    found_box=check_next_position(boxes,next_px,next_py)
    if check_in_map(next_px,next_py,map_width,map_height)==False:
        None
    else:
        if found_box is not None:
            next_box_x=found_box["x"]+dx
            next_box_y=found_box["y"]+dy
            if check_in_map(next_box_x,next_box_y,map_width,map_height)==True and check_object(boxes,next_box_x,next_box_y)==False:
                found_box["x"],found_box["y"]=next_box_x,next_box_y
                p["x"], p["y"] = next_px, next_py
        else:
            p["x"], p["y"] = next_px, next_py
    point=0
    for box in boxes:
        for gate in gates:
            if box == gate:
                point+=1

    if point==3:
        print_map(p, boxes, gates, map_width, map_height)
        print("You win!!!")
        break








