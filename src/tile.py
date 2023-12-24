import pygame
import constants as CONSTANTS

class Tile:
    
    
    def __init__(self, value: int, x: int, y: int):
        
        self.value = value
        self.rect = pygame.Rect((CONSTANTS.BOARD_X + CONSTANTS.PADDING + x * (CONSTANTS.PADDING + CONSTANTS.SQUARE_SIZE)),
                                (CONSTANTS.BOARD_Y + CONSTANTS.PADDING + y * (CONSTANTS.PADDING + CONSTANTS.SQUARE_SIZE)),
                                CONSTANTS.SQUARE_SIZE,
                                CONSTANTS.SQUARE_SIZE)
    
    def getValue(self) -> int: 
        return self.value
    
    def setValue(self, value: int):
        self.value = value
        
    def resetValue(self):
        self.value = CONSTANTS.TILE_DEFAULT_VALUE
    
    def draw(self, screen: pygame.Surface):

        pygame.draw.rect(screen, self.getColour(), self.rect)
        
        font = pygame.font.SysFont("segoeuisemibold", 48)
        img = font.render(str(self.value), True, (100, 100, 100))
        
        if (self.value != CONSTANTS.TILE_DEFAULT_VALUE):
            screen.blit(img, (self.rect.centerx - img.get_width() / 2, self.rect.centery - img.get_height() / 2))
       
    def getColour(self) -> tuple[int, int, int]:
        return CONSTANTS.TILE_COLOUR_DICT.get(f"{self.value}", CONSTANTS.BOARD_COLOUR)
       