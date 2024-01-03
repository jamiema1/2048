import pygame
import button as Button
import constants as CONSTANTS

class Menu:
    
    
    def __init__(self, buttons: list[Button.Button]):
        
        self.rect = pygame.Rect((CONSTANTS.MENU_CENTER_X - CONSTANTS.MENU_WIDTH / 2,
                                 CONSTANTS.MENU_CENTER_Y - CONSTANTS.MENU_HEIGHT / 2,
                                 CONSTANTS.MENU_WIDTH,
                                 CONSTANTS.MENU_HEIGHT))
        self.buttons = buttons

    def mouseIsOver(self, mousePosition: tuple) -> bool:
        return CONSTANTS.MENU_CENTER_X - CONSTANTS.MENU_WIDTH / 2 <= mousePosition[0] <= CONSTANTS.MENU_CENTER_X + CONSTANTS.MENU_WIDTH / 2 and CONSTANTS.MENU_CENTER_Y - CONSTANTS.MENU_HEIGHT / 2 <= mousePosition[1] <= CONSTANTS.MENU_CENTER_Y + CONSTANTS.MENU_HEIGHT / 2
       

    def draw(self, screen: pygame.Surface):

        pygame.draw.rect(screen, CONSTANTS.SCREEN_COLOUR, self.rect)
        
        for button in self.buttons:
            button.draw(screen)
        
        
       
       