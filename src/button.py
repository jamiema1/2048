import pygame
import constants as CONSTANTS

class Button:
    
    
    def __init__(self, x: int, y: int, width: int, height: int, text: str):
        
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect((x, y, width, height))

    
    def draw(self, screen: pygame.Surface):

        pygame.draw.rect(screen, CONSTANTS.BOARD_COLOUR, self.rect)
        
        font = pygame.font.SysFont("segoeuisemibold", CONSTANTS.TEXT_SIZE_2)
        img = font.render(self.text, True, CONSTANTS.TEXT_COLOUR)
        
        screen.blit(img, (self.rect.centerx - img.get_width() / 2, self.rect.centery - img.get_height() / 2))
        
    def mouseIsOverButton(self, mousePosition: tuple) -> bool:
        return self.x <= mousePosition[0] <= self.x + self.width and self.y <= mousePosition[1] <= self.y + self.height
       
       