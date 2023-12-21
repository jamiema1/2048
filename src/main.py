import pygame
import random
import board as Board
import constants as CONSTANTS

random.seed()

pygame.init()
pygame.display.set_caption('2048')

# TODO: change icon
# pygame.display.set_icon()

clock=pygame.time.Clock()

screen: pygame.Surface = pygame.display.set_mode((CONSTANTS.SCREEN_WIDTH, CONSTANTS.SCREEN_HEIGHT))


board: Board.Board = Board.Board(CONSTANTS.TILE_COUNT)
 
        
def gameloop():
    board.resetBoard() 
    # board.addTile() 
    # grid[0][0].setValue(2)
    # grid[0][1].setValue(2)
    # # grid[0][2].setValue(2)
    board.setTileValue(3,0,2)
    
    run: bool = True
    prevKey: int = None
    while run:
    
        screen.fill(CONSTANTS.SCREEN_COLOUR)
        
        board.draw(screen)    
        
        # key = pygame.key.get_pressed()
        
        # if key[pygame.K_r] == True:
        #     resetGrid(grid)
        #     addTile(grid)
        # elif key[pygame.K_d] == True:
        #     moveRight(grid)
        # elif key[pygame.K_a] == True:
        #     addTile(grid)
            
        
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYUP:
                prevKey = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and prevKey != pygame.K_a:
                    if board.moveLeft():   
                        board.addTile()
                    prevKey = pygame.K_a
                if event.key == pygame.K_d and prevKey != pygame.K_d:
                    if board.moveRight():   
                        board.addTile()
                    prevKey = pygame.K_d
                if event.key == pygame.K_r and prevKey != pygame.K_r:
                    board.resetBoard()
                    board.addTile()
                    prevKey = pygame.K_r
                if event.key == pygame.K_q and prevKey != pygame.K_q:
                    board.addTile()
                    prevKey = pygame.K_q
                    
                
        clock.tick(CONSTANTS.FPS)
        pygame.display.update()
    

    
if __name__ == "__main__":
    gameloop()
    pygame.quit()