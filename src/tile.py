import pygame
import constants

class Tile:
    
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, value: int, x: int, y: int):
        
        self.value = value
        self.rect = pygame.Rect((constants.BOARD_X + constants.PADDING + x * (constants.PADDING + constants.SQUARE_SIZE)),
                                (constants.BOARD_Y + constants.PADDING + y * (constants.PADDING + constants.SQUARE_SIZE)),
                                constants.SQUARE_SIZE,
                                constants.SQUARE_SIZE)
    
    def getValue(self) -> int: 
        return self.value
    
    def setValue(self, value: int):
        self.value = value
        
    def resetValue(self):
        self.value = constants.TILE_DEFAULT_VALUE
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.getColour(), self.rect)
       
    def getColour(self) -> tuple[int, int, int]:
        return constants.TILE_COLOUR_DICT.get(f"{self.value}", constants.BOARD_COLOUR)
       