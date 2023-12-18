import pygame

pygame.init()
pygame.display.set_caption('2048')

# TODO: change icon
# pygame.display.set_icon()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

PADDING = 10
SQUARE_SIZE = 50

COLOUR_1 = (255, 223, 107)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

tiles = []

# startTile = pygame.Rect((PADDING,PADDING,SQUARE_SIZE,SQUARE_SIZE))

# tiles.append(startTile)

run = True

BACKGROUND_COLOUR = (0,0,0)

for x in range(4):
    for y in range(4):
        startTile = pygame.Rect((PADDING + x * (PADDING + SQUARE_SIZE),PADDING + y * (PADDING + SQUARE_SIZE),SQUARE_SIZE,SQUARE_SIZE))
        tiles.append(startTile)


while run:
    
    screen.fill(BACKGROUND_COLOUR)
    
    for tile in tiles:
        pygame.draw.rect(screen, COLOUR_1, tile)
    
    key = pygame.key.get_pressed()
    
    # if key[pygame.K_s] == True:
    #     square.move_ip(0, 1)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()