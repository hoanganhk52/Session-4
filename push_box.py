play_x=1
play_y=0
box_x=2
box_y=1
point_x=1
point_y=4
map_x=5
map_y=5

def in_map(x,y,map_width,map_height):
    if x<0 or y<0 or x>map_width-1 or y>map_height-1:
        return False
    return True

def move(x,y,dx,dy):
    return[x+dx,y+dy]

def box_move(choice,box_x,box_y,play_x,play_y,dx,dy):
    if choice==("A"or"D") and box_y==play_y and (box_x==play_x-1 or box_x==play_x+1):
        return [box_x+dx,box_y]
    elif choice==("W"or"S") and box_x==play_x and (box_y==play_y-1 or box_y==play_y+1):
        return [box_x,box_y+dy]
    else:
        return [box_x,box_y]


while True:
    for y in range(map_y):
        for x in range(map_x):
            if x==play_x and y==play_y:
                print("P",end=" ")
            elif x==box_x and y==box_y:
                print("B", end=" ")
            elif x==point_x and y==point_y:
                print("*", end=" ")
            else:
                print("_", end=" ")
        print()

    choice = input("What's your choice ? ").upper()
    dx=0
    dy=0
    if choice=="A":
        dx=-1
    elif choice=="D":
        dx=1
    elif choice=="S":
        dy=1
    elif choice=="W":
        dy=-1

    [next_play_x,next_play_y]=move(play_x,play_y,dx,dy)


    if not in_map(next_play_x,next_play_y,map_x,map_y):
        print("Go away!!")
    else:
        play_x=next_play_x
        play_y=next_play_y
    [next_box_x, next_box_y] = box_move(choice,box_x,box_y,play_x,play_y,dx,dy)

    if not in_map(next_box_x,next_box_y,map_x,map_y):
        print("Go away!!")
    else:
        box_x=next_box_x
        box_y=next_box_y