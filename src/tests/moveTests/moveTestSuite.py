import unittest
import moveRightTestCase as MoveRightTestCase
import moveLeftTestCase as MoveLeftTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MoveRightTestCase.MoveRightTestCase))
    suite.addTest(unittest.makeSuite(MoveLeftTestCase.MoveLeftTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())