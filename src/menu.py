import pygame
import button as Button
import constants as CONSTANTS

class Menu:
    
    
    def __init__(self):
        
        self.rect = pygame.Rect((CONSTANTS.MENU_CENTER_X - CONSTANTS.MENU_WIDTH / 2,
                                 CONSTANTS.MENU_CENTER_Y - CONSTANTS.MENU_HEIGHT / 2,
                                 CONSTANTS.MENU_WIDTH,
                                 CONSTANTS.MENU_HEIGHT))
        
        self.restartButton: Button.Button = Button.Button(CONSTANTS.MENU_CENTER_X - CONSTANTS.MENU_BUTTON_WIDTH / 2,
                                                          CONSTANTS.MENU_CENTER_Y - CONSTANTS.MENU_BUTTON_HEIGHT / 2 - CONSTANTS.BUTTON_PADDING,
                                                          CONSTANTS.MENU_BUTTON_WIDTH,
                                                          CONSTANTS.MENU_BUTTON_HEIGHT,
                                                          "Restart")
        
        self.quitButton: Button.Button = Button.Button(CONSTANTS.MENU_CENTER_X - CONSTANTS.MENU_BUTTON_WIDTH / 2,
                                                       CONSTANTS.MENU_CENTER_Y - CONSTANTS.MENU_BUTTON_HEIGHT / 2 + CONSTANTS.BUTTON_PADDING,
                                                       CONSTANTS.MENU_BUTTON_WIDTH,
                                                       CONSTANTS.MENU_BUTTON_HEIGHT,
                                                       "Quit")

    def getRestartButton(self):
        return self.restartButton
    
    def getQuitButton(self):
        return self.quitButton

    def draw(self, screen: pygame.Surface):

        pygame.draw.rect(screen, CONSTANTS.SCREEN_COLOUR, self.rect)
        self.restartButton.draw(screen)
        self.quitButton.draw(screen)
        
        
       
       