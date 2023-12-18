import pygame

pygame.init()
pygame.display.set_caption('2048')

# TODO: change icon
# pygame.display.set_icon()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((50,50,50,50))

run = True

BACKGROUND_COLOUR = (0,0,0)

while run:
    
    screen.fill(BACKGROUND_COLOUR)
    
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    
    amount = 1
    if key[pygame.K_w] == True:
        player.move_ip(0, -amount)
    elif key[pygame.K_a] == True:
        player.move_ip(-amount, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, amount)
    elif key[pygame.K_d] == True:
        player.move_ip(amount, 0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()