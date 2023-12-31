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
    board.addTile()
    
    run: bool = True
    prevKey: int = None
    
    while run:
        
        screen.fill(CONSTANTS.SCREEN_COLOUR)
        
        board.updateHighScore()
        board.draw(screen)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYUP:
                prevKey = None
            elif event.type == pygame.KEYDOWN:
                isTileMove: bool = False
                if event.key == pygame.K_w and prevKey != pygame.K_w:
                    isTileMove = board.moveUp() 
                    prevKey = pygame.K_w
                elif event.key == pygame.K_a and prevKey != pygame.K_a:
                    isTileMove = board.moveLeft() 
                    prevKey = pygame.K_a
                elif event.key == pygame.K_s and prevKey != pygame.K_s:
                    isTileMove = board.moveDown() 
                    prevKey = pygame.K_s
                elif event.key == pygame.K_d and prevKey != pygame.K_d:
                    isTileMove = board.moveRight()
                    prevKey = pygame.K_d
                elif event.key == pygame.K_r and prevKey != pygame.K_r:
                    board.resetBoard()
                    board.addTile()
                    prevKey = pygame.K_r
                    
                if (isTileMove is True):
                    board.addTile()
                    
                    
                
        clock.tick(CONSTANTS.FPS)
        pygame.display.update()
    

    
if __name__ == "__main__":
    gameloop()
    pygame.quit()