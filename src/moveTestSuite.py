import unittest
import moveRightTestCase as moveRightTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(moveRightTestCase.MoveRightTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())