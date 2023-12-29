import unittest
import os
import sys

sys.path.append(os.path.abspath("src"))

import board as Board
import constants as CONSTANTS

class MoveLeftTestCase(unittest.TestCase):

    board = Board.Board(CONSTANTS.TILE_COUNT)
    
    def setUp(self):
        self.board.resetBoard()
    
    # 0 0 0 0 -> 0 0 0 0
    def test_moveLeftNoTiles(self):
        self.assertEqual(self.board.moveLeft(), False)
        
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                self.assertEqual(self.board.getTileValue(x,y), 0)
    
    # 2 0 0 0 -> 2 0 0 0
    def test_moveLeftOneTileNoMovement(self):
        self.board.setTileValue(0, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), False)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
         
    # 0 0 2 0 -> 2 0 0 0       
    def test_moveLeftOneTileSlideMiddle(self):
        self.board.setTileValue(2, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    # 0 0 0 2 -> 2 0 0 0
    def test_moveLeftOneTileSlideBeginning(self):
        self.board.setTileValue(CONSTANTS.TILE_COUNT - 1, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                              
    # 2 2 0 0 -> 4 0 0 0      
    def test_moveLeftTwoTileMergeEnd(self):
        self.board.setTileValue(0, 0, 2)
        self.board.setTileValue(1, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    # 0 2 2 0 -> 4 0 0 0      
    def test_moveLeftTwoTileMergeMiddle(self):
        self.board.setTileValue(0, 0, 2)
        self.board.setTileValue(1, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
      
    # 4 2 0 0 -> 4 2 0 0               
    def test_moveLeftTwoTileNoMovement(self):
        self.board.setTileValue(0, 0, 4)
        self.board.setTileValue(1, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), False)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
               
    # 0 2 0 4 -> 2 4 0 0     
    def test_moveLeftTwoTileSlide(self):
        self.board.setTileValue(1, 0, 2)
        self.board.setTileValue(3, 0, 4)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
               
    # 2 0 4 0 -> 2 4 0 0    
    def test_moveLeftOneTileSlideOneTileNoMovement(self):
        self.board.setTileValue(0, 0, 2)
        self.board.setTileValue(2, 0, 4)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
       
    # 2 2 2 0 -> 4 2 0 0
    def test_moveLeftThreeTileMergeSlide(self):
        self.board.setTileValue(0, 0, 2)
        self.board.setTileValue(1, 0, 2)
        self.board.setTileValue(2, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    # 4 2 2 0 -> 4 4 0 0 
    def test_moveLeftThreeTileMerge(self):
        self.board.setTileValue(0, 0, 4)
        self.board.setTileValue(1, 0, 2)
        self.board.setTileValue(2, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                          
    # 0 2 2 4 -> 4 4 0 0      
    def test_moveLeftThreeTileMergeSlideReverse(self):
        self.board.setTileValue(1, 0, 2)
        self.board.setTileValue(2, 0, 2)
        self.board.setTileValue(3, 0, 4)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                           
    # 0 2 4 2 -> 2 4 2 0      
    def test_moveLeftThreeTileNoMergeSlide(self):
        self.board.setTileValue(1, 0, 2)
        self.board.setTileValue(2, 0, 4)
        self.board.setTileValue(3, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 2):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                              
    # 2 4 0 8 -> 2 4 8 0     
    def test_moveLeftThreeTileSlide(self):
        self.board.setTileValue(0, 0, 2)
        self.board.setTileValue(1, 0, 4)
        self.board.setTileValue(3, 0, 8)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 2):
                    self.assertEqual(self.board.getTileValue(x,y), 8)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    # 2 2 2 2 -> 4 4 0 0      
    def test_moveLeftFourTileDoubleMerge(self):
        self.board.setTileValue(0, 0, 2)
        self.board.setTileValue(1, 0, 2)
        self.board.setTileValue(2, 0, 2)
        self.board.setTileValue(3, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)           
                    
    # 4 2 2 4 -> 4 4 4 0       
    def test_moveLeftFourTileSingleMerge(self):
        self.board.setTileValue(0, 0, 4)
        self.board.setTileValue(1, 0, 2)
        self.board.setTileValue(2, 0, 2)
        self.board.setTileValue(3, 0, 4)
        
        self.assertEqual(self.board.moveLeft(), True)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 2):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
    # 4 8 16 2 -> 4 8 16 2
    def test_moveLeftFourTileNoSlide(self):
        self.board.setTileValue(0, 0, 4)
        self.board.setTileValue(1, 0, 8)
        self.board.setTileValue(2, 0, 16)
        self.board.setTileValue(3, 0, 2)
        
        self.assertEqual(self.board.moveLeft(), False)
        
        for y in range(CONSTANTS.TILE_COUNT):
            for x in range(CONSTANTS.TILE_COUNT):
                if (y == 0 and x == 0):
                    self.assertEqual(self.board.getTileValue(x,y), 4)
                elif (y == 0 and x == 1):
                    self.assertEqual(self.board.getTileValue(x,y), 8)
                elif (y == 0 and x == 2):
                    self.assertEqual(self.board.getTileValue(x,y), 16)
                elif (y == 0 and x == 3):
                    self.assertEqual(self.board.getTileValue(x,y), 2)
                else:
                    self.assertEqual(self.board.getTileValue(x,y), 0)
                    
        
if __name__ == "__main__":
    unittest.main()