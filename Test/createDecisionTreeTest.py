'''
Created on Mar 3, 2019

@author: Tyler
'''
import unittest
import decisionTree as dt
import DecisionTreeObj as dtobj

class Test(unittest.TestCase):


    def test100GenericRoot(self):
        aminoString = "ERVVINISGLRFEVQLKTLAQFPETLLGDPKKRMRYFDPLRNEYFFDRNRPSFDAILYYYQSGGRLRRPVNVPLDIFSEEIRFYELG"
        buriedExposedString = "BBEEEEEBBBBEBEBBBEEBBEBBEEEEBBBEEBBBBBBBBBEEBEBBBBBEEBEEEBEEBBBBBBBBBBBEBBBBEBBEEBEEBEB"
        featureArray = [[0] for _ in range(len(aminoString))]
        for i in range(0, len(aminoString)):
            featureArray[i] = dt.getFeatureList(aminoString[i])
            if(buriedExposedString[i] == 'B'):
                featureArray[i][10] = 0
            else:
                featureArray[i][10] = 1
        arrayDict = {0:'Hydrophobic', 1:'Polar', 2:'Small', 3:'Proline', 4:'Tiny', 5:'Aliphatic', 6:'Aromatic', 7:'Positive', 8:'Negative', 9:'Charged'}
        rootObj = dtobj.DecisionTreeObj("root", featureArray, arrayDict)
        dt.calculateDecisionTree(rootObj)
        self.assertEqual(True, True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test100GenericRoot']
    unittest.main()