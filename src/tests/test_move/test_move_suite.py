import unittest
import test_move_right as MoveRightTestCase
import test_move_left as MoveLeftTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MoveRightTestCase.MoveRightTestCase))
    suite.addTest(unittest.makeSuite(MoveLeftTestCase.MoveLeftTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())