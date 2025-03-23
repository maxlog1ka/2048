import pygame
import random
import math

pygame.init()
FPS = 60
WIDTH = 400
HEIGHT = 400
ROWS = 4
COLS = 4
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS
KONTUR_COLOR = (40, 90, 40)
KONTUR_WIDTH = 10
BG_COLOR = (50, 110, 0)
FONT_COLOR = (119,110,101)

FONT = pygame.font.SysFont("comicsans",60,bold = True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def draw_grid(window):
    for row in range(1,ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window,KONTUR_COLOR,(0,y),(WIDTH,y), KONTUR_WIDTH)
    for col in range(1,COLS):
        x = col * RECT_HEIGHT
        pygame.draw.line(window,KONTUR_COLOR,(x,0),(x,HEIGHT), KONTUR_WIDTH)
    
    pygame.draw.rect(window,KONTUR_COLOR, (0,0,WIDTH,HEIGHT), KONTUR_WIDTH)

def draw(window):
    window.fill(BG_COLOR)
    draw_grid(window)
    
    
    pygame.display.update()

def main(self):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(WINDOW)
    pygame.quit()
            

if __name__ == "__main__":
    main(WINDOW)

def pretty_print(mas):
    print('------------')
    for row in mas:
        print(*row)
    print('------------')
    
def get_number_from_index(i,j):
    return i*4+j+1
def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i,j)
                empty.append(num)
    return empty
                

                   

mas = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
mas [2][3] = 2
mas [1][0] = 4

print(get_empty_list(mas))
pretty_print(mas)