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

def move_box(play_x,play_y,box_x,box_y):
    if choice=="A" and play_x==box_x and play_y==box_y:
        return [box_x-1,box_y]
    elif choice=="D"and play_x==box_x and play_y==box_y:
        return [box_x + 1, box_y]
    elif choice=="S"and play_x==box_x and play_y==box_y:
        return [box_x, box_y+1]
    elif choice=="W"and play_x==box_x and play_y==box_y:
        return [box_x, box_y-1]
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
    if box_x==point_x and box_y==point_y:
        print("You win!!!")
        break

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

    [next_box_x,next_box_y]= move_box(play_x,play_y,box_x,box_y)

    if not in_map(next_box_x,next_box_y,map_x,map_y):
        print("Go away!!")
    else:
        box_x=next_box_x
        box_y=next_box_y
