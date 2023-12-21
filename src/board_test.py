import unittest
import tile as Tile

class BoardTest(unittest.TestCase):

    
    def setUp(self):
        self.tile = Tile.Tile(0, 0, 0)
    
    def test_getValue(self):
        self.assertEqual(self.tile.getValue(), 0)
    
    
if __name__ == "__main__":
    unittest.main()