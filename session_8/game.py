import pygame
pygame.init()
screen = pygame.display.set_mode([400,300])

done = False
game_finish = False
COLOR_BLUE = [0,255,255]

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def calc_next_position(self,dx,dy):
        return [self.x + dx, self.y + dy]



class Box():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def calc_next_position(self,dx,dy):
        return [self.x + dx, self.y + dy]

class Gate():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Map():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.player = Player(1,1)
        self.box = Box(2,2)
        self.gate = Gate(3,3)

    def check_inside(self,x,y):
        if 0<= x < self.width and 0 <= y < self.height:
            return True
        return False

    def move_object(self,dx,dy):
        [next_px, next_py] = self.player.calc_next_position(dx,dy)
        [next_bx, next_by] = self.box.calc_next_position(dx,dy)
        if not self.check_inside(next_px,next_py):
            None
        else:
            if [next_px, next_py] == [self.box.x, self.box.y]:
                if self.check_inside(next_bx, next_by)==True:
                    self.player.move(dx,dy)
                    self.box.move(dx,dy)
            else:
                self.player.move(dx,dy)

    def check_win(self,game_finish):
        if self.box.x == self.gate.x and self.box.y == self.gate.y:
            game_finish = True
            return game_finish


map = Map(5,5)
SQUARE_SIZE = 32

mario = pygame.image.load("mario.png")
square = pygame.image.load("square.png")
box = pygame.image.load("box.png")
gate = pygame.image.load("gate.png")
you_win = pygame.image.load("you_win.png")

while not done:
    dx=0
    dy=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT or map.check_win(game_finish):
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
            else:
                dx, dy = 0, 0

    if dx !=0 or dy !=0:
        map.move_object(dx,dy)

    screen.fill(COLOR_BLUE)

    for y in range(map.height):
        for x in range(map.width):
            screen.blit(square,(x * SQUARE_SIZE, y * SQUARE_SIZE ))

    screen.blit(gate, (map.gate.x * SQUARE_SIZE, map.gate.y * SQUARE_SIZE))
    screen.blit(box, (map.box.x * SQUARE_SIZE, map.box.y * SQUARE_SIZE))
    screen.blit(mario, (map.player.x * SQUARE_SIZE, map.player.y * SQUARE_SIZE))
    if map.check_win(game_finish):
        screen.blit(you_win, (0, 0))

    pygame.display.flip()







