import unittest
import board as Board
import constants as CONSTANTS

class MoveRightTestCase(unittest.TestCase):

    board = Board.Board(CONSTANTS.TILE_COUNT)
    
    def setUp(self):
        self.board.resetBoard()
    
    def test_moveRightNoTiles(self):
        self.assertEqual(self.board.moveRight(), False)
        
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                self.assertEqual(self.board.getTileValue(x,y), 0)
    
    def test_moveRightOneTileNoMovement(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        
        self.assertEqual(self.board.moveRight(), False)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                
    def test_moveRightOneTileSlide(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
                    
    def test_moveRightTwoTileMerge(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    def test_moveRightTwoTileNoMovement(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 4)
        
        self.assertEqual(self.board.moveRight(), False)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    def test_moveRightOneTileSlideOneTileNoMovement(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 4)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    def test_moveRightTwoTileSlide(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 4)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    def test_moveRightTwoTileMergeSlide(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    def test_moveRightTwoTileMergeSlideOneTileSlide(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 4)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    def test_moveRightFourTileMergePairs(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 4)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 4)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 8)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
    
    def test_moveRightFourTileMergeMiddle(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 4)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 4)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 3):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    def test_moveRightFourTileNoMovement(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 4)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 16)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 32)
        
        self.assertEqual(self.board.moveRight(), False)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 3):
                    self.assertEqual(self.board.getTileValue(x,y), 16)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 4):
                    self.assertEqual(self.board.getTileValue(x,y), 32)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
    
if __name__ == "__main__":
    unittest.main()