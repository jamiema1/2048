import pygame
import random

random.seed()

pygame.init()
pygame.display.set_caption('2048')

# TODO: change icon
# pygame.display.set_icon()

clock=pygame.time.Clock()
FPS = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SCREEN_COLOUR = (0,0,0)

PADDING = 10
SQUARE_SIZE = 150

BOARD_COLOUR = (105, 105, 105)
BOARD_X = SCREEN_WIDTH / 2 - (2 * SQUARE_SIZE + 2.5 * PADDING)
BOARD_Y = SCREEN_HEIGHT / 2 - (2 * SQUARE_SIZE + 2.5 * PADDING)
BOARD_SIZE = 4 * SQUARE_SIZE + 5 * PADDING


COLOUR_1 = (255, 223, 107)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# grid = [
#     [None, None, None, None],
#     [None, None, None, None],
#     [None, None, None, None],
#     [None, None, None, None],
# ]

tiles = []

startTile = pygame.Rect((BOARD_X + PADDING + random.randint(0,3) * (PADDING + SQUARE_SIZE),
                         BOARD_Y + PADDING + random.randint(0,3) * (PADDING + SQUARE_SIZE),
                         SQUARE_SIZE,
                         SQUARE_SIZE))

tiles.append(startTile)

run = True

board = pygame.Rect((BOARD_X, BOARD_Y, BOARD_SIZE, BOARD_SIZE))


# for x in range(4):
#     for y in range(4):
#         startTile = pygame.Rect((PADDING + x * (PADDING + SQUARE_SIZE),PADDING + y * (PADDING + SQUARE_SIZE),SQUARE_SIZE,SQUARE_SIZE))
#         tiles.append(startTile)


while run:
    
    screen.fill(SCREEN_COLOUR)
    
    
    pygame.draw.rect(screen, BOARD_COLOUR, board)
    
    for tile in tiles:
        pygame.draw.rect(screen, COLOUR_1, tile)
    
    key = pygame.key.get_pressed()
    
    # if key[pygame.K_s] == True:
    #     square.move_ip(0, 1)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    clock.tick(FPS)
    pygame.display.update()
            
pygame.quit()