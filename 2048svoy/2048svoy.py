import pygame
import random
import math


pygame.init()
FPS = 60
WIDTH = 800
HEIGHT = 800
ROWS = 4
COLS = 4
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS
KONTUR_COLOR = (0, 180, 230)
KONTUR_WIDTH = 10
BG_COLOR = (0, 250, 230)
FONT_COLOR = (119,110,101)

FONT = pygame.font.SysFont("comicsans",60,bold = True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

class Tile:
    COLORS = [
        (255, 255, 0),
        (255, 180, 0),
        (255, 100, 0),
        (200, 0, 0),
        (200, 0, 80),
        (200, 0, 130),
        (200, 0, 210),
        (200, 130, 210),
        (162, 142, 255),
        (90, 145, 255),
        (0, 145, 255)
    ]

    def __init__(self,value,row,col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col*RECT_WIDTH
        self.y = row*RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color
    def draw(self,window):
        color = self.get_color()
        pygame.draw.rect(window,color,(self.x,self.y,RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(self.value),1,FONT_COLOR)
        window.blit(
            text,
            (
                self.x + (RECT_WIDTH/2 - text.get_width()/2),
                self.y + (RECT_HEIGHT /2 -text.get_height()/2),
            ),
        )
    def set_pos(self):
        pass
    def move(self,delta):
        pass


def draw_grid(window):
    for row in range(1,ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window,KONTUR_COLOR,(0,y),(WIDTH,y), KONTUR_WIDTH)
    for col in range(1,COLS):
        x = col * RECT_HEIGHT
        pygame.draw.line(window,KONTUR_COLOR,(x,0),(x,HEIGHT), KONTUR_WIDTH)
    
    pygame.draw.rect(window,KONTUR_COLOR, (0,0,WIDTH,HEIGHT), KONTUR_WIDTH)

def draw(window,tiles):
    window.fill(BG_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)
    
    
    pygame.display.update()

def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randrange(0,ROWS)
        col = random.randrange(0,COLS)
        
        if f"{row}{col}" not in tiles:
            break
    return row,col

def generate_tiles():
    tiles = {}
    for _ in range(2):
        row,col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(2,row,col)
    return tiles
def main(self):
    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(WINDOW, tiles)
    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)
#--------------------------------------------------------------------------------
#def pretty_print(mas):
#    print('------------')
#    for row in mas:
#        print(*row)
#    print('------------')
#    
#def get_number_from_index(i,j):
#    return i*4+j+1
#def get_empty_list(mas):
#    empty = []
#    for i in range(4):
#        for j in range(4):
#           if mas[i][j] == 0:
#                num = get_number_from_index(i,j)
#                empty.append(num)
#    return empty
                

                   

#mas = [
#    [0,0,0,0],
#    [0,0,0,0],
#    [0,0,0,0],
#    [0,0,0,0],
#]
#mas [2][3] = 2
#mas [1][0] = 4

#print(get_empty_list(mas))
#pretty_print(mas)