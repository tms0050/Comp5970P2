'''
Created on Feb 25, 2019

@author: Tyler
'''
import unittest
import decisionTree as dt

class Test(unittest.TestCase):


    def test100EasyArray(self):
        testMatrix = [[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1], [1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1]]
        totPos = 9
        totNeg = 7
        print(testMatrix[1][0])
        returnVal = dt.calcInfoGain(testMatrix, totPos, totNeg)
        self.assertAlmostEqual(returnVal, 0.1008, 1)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()