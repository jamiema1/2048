import pygame
import random
import tile as Tile
import constants

random.seed()

pygame.init()
pygame.display.set_caption('2048')

# TODO: change icon
# pygame.display.set_icon()

clock=pygame.time.Clock()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))


board = pygame.Rect((constants.BOARD_X, constants.BOARD_Y, constants.BOARD_SIZE, constants.BOARD_SIZE))



grid: list[list[Tile.Tile]] = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]

def moveRight(grid: list[list[Tile.Tile]]):
    
    tileMove: bool = False
    
    for y, row in enumerate(grid):
        
        emptySpot: int = len(row) - 1
        currentTile: Tile.Tile
        nextTile: Tile.Tile
        newValue: int
                
        for x in reversed(range(len(row))):
            
            nextTile = None
            currentTile = row[x]
            
            if currentTile.getValue() == constants.TILE_DEFAULT_VALUE:
                continue
            
            for x2 in reversed(range(x)):
                if row[x2].getValue() == constants.TILE_DEFAULT_VALUE:
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
            
            
def moveLeft(grid: list[list[Tile.Tile]]):
    
    tileMove: bool = False
    
    for y, row in enumerate(grid):
        
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
            if currentTile.getValue() == constants.TILE_DEFAULT_VALUE:
                continue
            
            for x2 in range(x + 1, len(row)):
                if row[x2].getValue() == constants.TILE_DEFAULT_VALUE:
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
            
            
            
            
def resetGrid(grid: list[list[Tile.Tile]]):
    for y, row in enumerate(grid):
        for x in range(len(row)):
            grid[y][x] = Tile.Tile(constants.TILE_DEFAULT_VALUE, x, y)

def addTile(grid: list[list[Tile.Tile]]):
    while True:
        x = random.randint(0,constants.TILE_COUNT - 1)
        y = random.randint(0,constants.TILE_COUNT - 1)
        
        tile = grid[y][x]
        if (tile.getValue() == constants.TILE_DEFAULT_VALUE):
            value = random.randint(1,2)
            tile.setValue(pow(2, value))
            return
        
        
def gameloop():
    resetGrid(grid) 
    grid[0][0].setValue(2)
    grid[0][1].setValue(2)
    # grid[0][2].setValue(2)
    # grid[0][3].setValue(2)  
    # addTile(grid)
    
    run: bool = True
    prevKey: int = None
    while run:
    
        screen.fill(constants.SCREEN_COLOUR)
        pygame.draw.rect(screen, constants.BOARD_COLOUR, board)
        
        
        # key = pygame.key.get_pressed()
        
        # if key[pygame.K_r] == True:
        #     resetGrid(grid)
        #     addTile(grid)
        # elif key[pygame.K_d] == True:
        #     moveRight(grid)
        # elif key[pygame.K_a] == True:
        #     addTile(grid)
            
            
        
        for x in range(4):
            for y in range(4):
                grid[y][x].draw(screen)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYUP:
                prevKey = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and prevKey != pygame.K_a:
                    if moveLeft(grid):   
                        addTile(grid)
                    prevKey = pygame.K_a
                if event.key == pygame.K_d and prevKey != pygame.K_d:
                    if moveRight(grid):   
                        addTile(grid)
                    prevKey = pygame.K_d
                if event.key == pygame.K_r and prevKey != pygame.K_r:
                    resetGrid(grid)
                    addTile(grid)
                    prevKey = pygame.K_r
                if event.key == pygame.K_q and prevKey != pygame.K_q:
                    addTile(grid)
                    prevKey = pygame.K_q
                    
                
        clock.tick(constants.FPS)
        pygame.display.update()
    

    
if __name__ == "__main__":
    gameloop()
    pygame.quit()