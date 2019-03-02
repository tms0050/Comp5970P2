'''
Created on Feb 28, 2019

@author: Tyler
'''
import unittest
import decisionTree as dt

class Test(unittest.TestCase):


    def testBasicString(self):
        inputString = "LFKLGAENIFLGRKAATKEEAIRFAGEQLVKGGYVEPEYVQAMLDREKLTPTYLGESIAVPHGTVEAKDRVLKTGVVFCQYPEGVRFGEEEDDIARLVIGIAARNNEHIQVITSLTNALDDESVIERLAHTTSVDEVLELLAGRK"
        outputVals = dt.calculateHighestOccurences(inputString)
        self.assertListEqual(outputVals, [1,0,0,0,0,0,1])
        
    def testBasicString2(self):
        inputString = "VLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRFKHLKTEAEMKASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGDFGADAQGAMNKALELFRKDIAAKYKELGY"
        outputVals = dt.calculateHighestOccurences(inputString)
        self.assertListEqual(outputVals, [1,0,0,0,0,0,1])
        
    def testBasicString3(self):
        inputString = "PWATAEYDYDAAEDNELTFVENDKIINIEFVDDDWWLGELEKDGSKGLFPSNYVSLGN"
        outputVals = dt.calculateHighestOccurences(inputString)
        self.assertListEqual(outputVals, [1,0,0,0,0,0,1])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBasicString']
    unittest.main()