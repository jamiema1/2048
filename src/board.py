import tile as Tile
import constants as CONSTANTS
import random
import pygame

class Board:
    
    def __init__(self, size: int):
        self.board: list[list[Tile.Tile]] = [ [None]*size for i in range(size)]
        self.rect = pygame.Rect((CONSTANTS.BOARD_X, 
                                 CONSTANTS.BOARD_Y, 
                                 CONSTANTS.BOARD_SIZE,
                                 CONSTANTS.BOARD_SIZE))
    
    def getBoard(self) -> list[list[Tile.Tile]]:
        return self.board
    
    def getTile(self, x: int, y: int) -> Tile.Tile:
        return self.board[y][x]
    
    def getTileValue(self, x: int, y: int) -> int:
        return self.board[y][x].getValue()
        
    def setTileValue(self, x: int, y: int, value: int):
        self.board[y][x].setValue(value)
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, CONSTANTS.BOARD_COLOUR, self.rect)
        
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                self.board[y][x].draw(screen)
    
    def resetBoard(self):
        for y, row in enumerate(self.board):
            for x in range(len(row)):
                self.board[y][x] = Tile.Tile(CONSTANTS.TILE_DEFAULT_VALUE, x, y)
                
    def addTile(self):
        while True:
            x = random.randint(0, CONSTANTS.TILE_COUNT - 1)
            y = random.randint(0, CONSTANTS.TILE_COUNT - 1)
            
            tile = self.board[y][x]
            if (tile.getValue() == CONSTANTS.TILE_DEFAULT_VALUE):
                value = random.randint(1,2)
                tile.setValue(pow(2, value))
                return
        
    def moveRight(self) -> bool:
    
        isTileMove: bool = False
        
        for y in range(CONSTANTS.TILE_COUNT):
            
            emptySpot: int = CONSTANTS.TILE_COUNT - 1
                
            for x in reversed(range(CONSTANTS.TILE_COUNT)):
                
                currentTile: Tile.Tile = self.getTile(x,y)
                currentTileValue: int = self.getTileValue(x,y)
                nextTile: Tile.Tile = None
                nextTileValue: int = CONSTANTS.TILE_DEFAULT_VALUE
                newValue: int = CONSTANTS.TILE_DEFAULT_VALUE
    
                # Skip if current Tile is Empty
                if currentTileValue == CONSTANTS.TILE_DEFAULT_VALUE:
                    continue
                
                # Find next Non-Empty Tile
                for x2 in reversed(range(x)):
                    if self.getTileValue(x2, y) != CONSTANTS.TILE_DEFAULT_VALUE:
                        nextTile = self.getTile(x2,y)
                        nextTileValue = nextTile.getValue()
                        break
                    
                merge: bool = nextTile is not None and currentTileValue == nextTileValue
                slide: bool = x != emptySpot
                if (merge or slide):
                    if (merge):
                        newValue = nextTileValue
                        nextTile.resetValue()
                    newValue += currentTileValue
                    currentTile.resetValue()
                    self.setTileValue(emptySpot, y, newValue)
                    isTileMove = True
                    
                emptySpot -= 1
                
        return isTileMove
                
                
    def moveLeft(self) -> bool:
        
        isTileMove: bool = False
        
        for y in range(CONSTANTS.TILE_COUNT):
            
            emptySpot: int = 0
            
            for x in range(CONSTANTS.TILE_COUNT):
                
                currentTile: Tile.Tile = self.getTile(x,y)
                currentTileValue: int = self.getTileValue(x,y)
                nextTile: Tile.Tile = None
                nextTileValue: int = CONSTANTS.TILE_DEFAULT_VALUE
                newValue: int = CONSTANTS.TILE_DEFAULT_VALUE
                
                if currentTileValue == CONSTANTS.TILE_DEFAULT_VALUE:
                    continue
                
                for x2 in range(x + 1, CONSTANTS.TILE_COUNT):
                    if self.getTileValue(x2, y) != CONSTANTS.TILE_DEFAULT_VALUE:
                        nextTile = self.getTile(x2, y)
                        nextTileValue = nextTile.getValue()
                        break
                
                merge: bool = nextTile is not None and currentTileValue == nextTileValue
                slide: bool = x != emptySpot
                if (merge or slide):
                    if (merge):
                        newValue = nextTileValue
                        nextTile.resetValue()
                    newValue += currentTileValue
                    currentTile.resetValue()
                    self.setTileValue(emptySpot, y, newValue)
                    isTileMove = True
                    
                emptySpot += 1

        return isTileMove
       
    def moveUp(self) -> bool:
        return True
    
    
    def moveDown(self) -> bool:
        return True