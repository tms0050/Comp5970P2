'''
Created on Mar 1, 2019

@author: Tyler
'''
import unittest
import decisionTree as dt

class Test(unittest.TestCase):


    def test100BaseTest(self):
        answer = dt.calculateDecisionMatrix()
        self.assertEqual(answer, 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100BaseTest']
    unittest.main()