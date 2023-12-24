import unittest
import os
import sys

sys.path.append(os.path.abspath("src"))

import board as Board
import constants as CONSTANTS

class MoveRightTestCase(unittest.TestCase):

    board = Board.Board(CONSTANTS.TILE_COUNT)
    
    def setUp(self):
        self.board.resetBoard()
    
    # 0 0 0 0 -> 0 0 0 0
    def test_moveRightNoTiles(self):
        self.assertEqual(self.board.moveRight(), False)
        
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                self.assertEqual(self.board.getTileValue(x,y), 0)
    
    # 0 0 0 2 -> 0 0 0 2
    def test_moveRightOneTileNoMovement(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        
        self.assertEqual(self.board.moveRight(), False)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
         
    # 0 0 2 0 -> 0 0 0 2       
    def test_moveRightOneTileSlideMiddle(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    # 2 0 0 0 -> 0 0 0 2       
    def test_moveRightOneTileSlideBeginning(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                              
    # 0 0 2 2 -> 0 0 0 4      
    def test_moveRightTwoTileMergeEnd(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    # 0 2 2 0 -> 0 0 0 4      
    def test_moveRightTwoTileMergeMiddle(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
      
    # 0 0 2 4 -> 0 0 2 4               
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
               
    # 0 2 0 4 -> 0 0 2 4     
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
               
    # 2 0 4 0 -> 0 0 2 4    
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
       
    # 0 2 2 2 -> 0 0 2 4
    def test_moveRightThreeTileMergeSlide(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    # 0 2 2 4 -> 0 0 4 4 
    def test_moveRightThreeTileMerge(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 4)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                          
    # 4 2 2 0 -> 0 0 4 4      
    def test_moveRightThreeTileMergeSlideReverse(self):
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
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                           
    # 2 4 2 0 -> 0 2 4 2      
    def test_moveRightThreeTileNoMergeSlide(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 4)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 3):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                              
    # 2 4 0 8 -> 0 2 4 8     
    def test_moveRightThreeTileSlide(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 8)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 4)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 8)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 3):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    # 2 2 2 2 -> 0 0 4 4      
    def test_moveRightFourTileDoubleMerge(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 2)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 2)
        
        self.assertEqual(self.board.moveRight(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)           
                    
    # 4 2 2 4 -> 0 4 4 4       
    def test_moveRightFourTileSingleMerge(self):
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
                    
    # 4 8 16 2 -> 4 8 16 2
    def test_moveRightFourTileNoSlide(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 4)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 2, 0, 8)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 3, 0, 16)
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 4, 0, 2)
        
        self.assertEqual(self.board.moveRight(), False)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == CONSTANTS.TILE_COUNT - 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 2):
                    self.assertEqual(self.board.getTileValue(x,y), 8)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 3):
                    self.assertEqual(self.board.getTileValue(x,y), 16)
                elif (y == 0 and x == CONSTANTS.TILE_COUNT - 4):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
        
if __name__ == "__main__":
    unittest.main()