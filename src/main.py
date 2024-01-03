import pygame
import random
import board as Board
import menu as Menu
import button as Button
import constants as CONSTANTS

random.seed()

pygame.init()
pygame.display.set_caption('2048')

# TODO: change icon
# pygame.display.set_icon()

clock=pygame.time.Clock()

screen: pygame.Surface = pygame.display.set_mode((CONSTANTS.SCREEN_WIDTH, CONSTANTS.SCREEN_HEIGHT))

board: Board.Board = Board.Board(CONSTANTS.TILE_COUNT)

menuButton: Button.Button = Button.Button(CONSTANTS.MENU_BUTTON_CENTER_X - CONSTANTS.MENU_BUTTON_WIDTH / 2,
                                          CONSTANTS.MENU_BUTTON_CENTER_Y - CONSTANTS.MENU_BUTTON_HEIGHT / 2,
                                          CONSTANTS.MENU_BUTTON_WIDTH,
                                          CONSTANTS.MENU_BUTTON_HEIGHT,
                                          "MENU")

restartButton: Button.Button = Button.Button(CONSTANTS.MENU_CENTER_X - CONSTANTS.MENU_BUTTON_WIDTH / 2,
                                             CONSTANTS.MENU_CENTER_Y - CONSTANTS.MENU_BUTTON_HEIGHT / 2 - CONSTANTS.BUTTON_PADDING,
                                             CONSTANTS.MENU_BUTTON_WIDTH,
                                             CONSTANTS.MENU_BUTTON_HEIGHT,
                                             "RESTART")
        
quitButton: Button.Button = Button.Button(CONSTANTS.MENU_CENTER_X - CONSTANTS.MENU_BUTTON_WIDTH / 2,
                                          CONSTANTS.MENU_CENTER_Y - CONSTANTS.MENU_BUTTON_HEIGHT / 2 + CONSTANTS.BUTTON_PADDING,
                                          CONSTANTS.MENU_BUTTON_WIDTH,
                                          CONSTANTS.MENU_BUTTON_HEIGHT,
                                          "QUIT")

gameOverButton: Button.Button = Button.Button(CONSTANTS.MENU_CENTER_X - CONSTANTS.GAME_OVER_TEXT_WIDTH / 2,
                                              CONSTANTS.GAME_OVER_TEXT_Y - CONSTANTS.MENU_BUTTON_WIDTH / 2,
                                              CONSTANTS.GAME_OVER_TEXT_WIDTH,
                                              CONSTANTS.MENU_BUTTON_HEIGHT,
                                              "GAME OVER")

menu: Menu.Menu = Menu.Menu([restartButton, quitButton])

def gameloop():
    
    board.resetBoard() 
    board.addTile()
    
    run: bool = True
    prevKey: int = None
    isMenuOpen: bool = False
    isGameOver: bool = False
    
    while run:
        
        mousePosition = pygame.mouse.get_pos()
        
        screen.fill(CONSTANTS.SCREEN_COLOUR)
        
        board.updateHighScore()
        board.draw(screen)
        
        menuButton.draw(screen)
        
        if isGameOver:
            gameOverButton.draw(screen)
            isMenuOpen = True
            
        if isMenuOpen:
            menu.draw(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menuButton.mouseIsOverButton(mousePosition):
                    isMenuOpen = True
                elif not menu.mouseIsOver(mousePosition):
                    isMenuOpen = False
                elif quitButton.mouseIsOverButton(mousePosition):
                    run = False
                elif restartButton.mouseIsOverButton(mousePosition):   
                    isMenuOpen = False
                    isGameOver = False
                    board.resetBoard() 
                    board.addTile()
                    
            if isMenuOpen:
                break
            if event.type == pygame.KEYUP:
                prevKey = None
            elif event.type == pygame.KEYDOWN:
                isTileMove: bool = False
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and prevKey != pygame.K_UP:
                    isTileMove = board.moveUp() 
                    prevKey = pygame.K_UP
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT)  and prevKey != pygame.K_LEFT:
                    isTileMove = board.moveLeft() 
                    prevKey = pygame.K_LEFT
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN)  and prevKey != pygame.K_DOWN:
                    isTileMove = board.moveDown() 
                    prevKey = pygame.K_DOWN
                elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT)  and prevKey != pygame.K_RIGHT:
                    isTileMove = board.moveRight()
                    prevKey = pygame.K_RIGHT
                    
                if (isTileMove is True):
                    board.addTile()
                    isGameOver = board.isFull()
                    
        clock.tick(CONSTANTS.FPS)
        pygame.display.update()
    

    
if __name__ == "__main__":
    gameloop()
    pygame.quit()