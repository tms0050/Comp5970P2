'''
Created on Feb 25, 2019

@author: Tyler
'''
import math

def calcInfoGain(infoArray, totPos, totNeg, numAttributes = 2):
    negativeVals = 0
    positiveVals = 0
    infoGainTotal = 0.0
    for i in range(0, numAttributes):
        for x in range(0, len(infoArray[0])):
            if(infoArray[0][x] != i):
                continue
            if(infoArray[1][x] == 1):
                positiveVals+=1
            else:
                negativeVals+=1
        infoGainTotal += ((positiveVals + negativeVals)/len(infoArray[0])) * calcEntropy(positiveVals, negativeVals)
        positiveVals = 0
        negativeVals = 0
    return calcEntropy(totPos, totNeg) - infoGainTotal

def calcEntropy(positives, negatives):
    if ((positives == 0) | (negatives == 0)):
        return 0
    positiveRatio = float(positives/(positives+negatives))
    negativeRatio = 1 - positiveRatio
    entropyVal = -1 * positiveRatio * math.log(positiveRatio,2) - negativeRatio * math.log(negativeRatio,2)
    return entropyVal