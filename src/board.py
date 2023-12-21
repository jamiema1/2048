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
    
        tileMove: bool = False
        
        for y, row in enumerate(self.board):
            
            emptySpot: int = len(row) - 1
            currentTile: Tile.Tile
            nextTile: Tile.Tile
            newValue: int
                    
            for x in reversed(range(len(row))):
                
                nextTile = None
                currentTile = row[x]
                
                if currentTile.getValue() == CONSTANTS.TILE_DEFAULT_VALUE:
                    continue
                
                for x2 in reversed(range(x)):
                    if row[x2].getValue() == CONSTANTS.TILE_DEFAULT_VALUE:
                        continue
                    nextTile = row[x2]
                    break
                
                if (nextTile is not None and currentTile.getValue() == nextTile.getValue()):
                    newValue = currentTile.getValue() + nextTile.getValue()
                    nextTile.resetValue()
                    currentTile.resetValue()
                    row[emptySpot].setValue(newValue)
                    tileMove = True
                elif (x != emptySpot):
                    newValue = currentTile.getValue()
                    currentTile.resetValue()
                    row[emptySpot].setValue(newValue)
                    tileMove = True
                emptySpot -= 1
                
        return tileMove
                
                
    def moveLeft(self) -> bool:
        
        tileMove: bool = False
        
        for y, row in enumerate(self.board):
            
            emptySpot: int = 0
            currentTile: Tile.Tile
            nextTile: Tile.Tile
            newValue: int
            
            for x in range(len(row)):
                print(emptySpot, x)
                nextTile = None
                currentTile = row[x]
                
                print(currentTile)
                print(currentTile.getValue())
                if currentTile.getValue() == CONSTANTS.TILE_DEFAULT_VALUE:
                    continue
                
                for x2 in range(x + 1, len(row)):
                    if row[x2].getValue() == CONSTANTS.TILE_DEFAULT_VALUE:
                        continue
                    nextTile = row[x2]
                    break
                
                if (nextTile is not None and currentTile.getValue() == nextTile.getValue()):
                    newValue = currentTile.getValue() + nextTile.getValue()
                    nextTile.resetValue()
                    currentTile.resetValue()
                    row[emptySpot].setValue(newValue)
                    tileMove = True
                elif (x != emptySpot):
                    newValue = currentTile.getValue()
                    currentTile.resetValue()
                    row[emptySpot].setValue(newValue)
                    tileMove = True
                emptySpot += 1

        return tileMove
       