'''
Created on Feb 25, 2019

@author: Tyler
'''
import math
import os
import DecisionTreeObj

def calcInfoGain(infoArray, totPos, totNeg):
    negativeVals = 0
    positiveVals = 0
    infoGainTotal = 0.0
    for i in range(0, 2):
        positiveVals = infoArray[i][1]
        negativeVals = infoArray[i][0]
        infoGainTotal += ((positiveVals + negativeVals)/(totPos + totNeg)) * calcEntropy(positiveVals, negativeVals)
    return calcEntropy(totPos, totNeg) - infoGainTotal

def calcEntropy(positives, negatives):
    if ((positives == 0) | (negatives == 0)):
        return 0
    positiveRatio = float(positives/(positives+negatives))
    negativeRatio = 1 - positiveRatio
    entropyVal = -1 * positiveRatio * math.log(positiveRatio,2) - negativeRatio * math.log(negativeRatio,2)
    return entropyVal

# How to iterate through directory source:
# https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
# How to get a singular file:
# https://stackoverflow.com/questions/13223737/how-to-read-a-file-in-other-directory-in-python
def calculateDecisionTree(currentRoot):
    bestAttSoFar = ""
    bestIGSoFar = 0.0
    currentValues = currentRoot.getValues()
    rowLen = len(currentValues[0]) - 1
    posNegMatrix = [[0,0],[0,0]]
    for j in range(rowLen):
        for i in range(0, len(currentValues)):
            if(currentValues[i][j] == 0):
                if(currentValues[i][rowLen] == 0):
                    posNegMatrix[0][0] += 1
                else:
                    posNegMatrix[0][1] += 1
            else:
                if(currentValues[i][rowLen] == 0):
                    posNegMatrix[1][0] += 1
                else:
                    posNegMatrix[1][1] += 1
        thisValue = calcInfoGain(posNegMatrix, posNegMatrix[1][0] + posNegMatrix[1][1], posNegMatrix[0][0] + posNegMatrix[0][1])
        if thisValue > bestIGSoFar:
            bestIGSoFar = thisValue
            bestAttSoFar = currentRoot.getDictVal(j)
        posNegMatrix = [[0,0],[0,0]]
    if bestIGSoFar <= 0.0:
        counter = 0
        for i in range(0, len(currentValues)):
            if currentValues[i][len(currentValues[0]) - 1] == 1:
                counter+=1
            else:
                counter-=1
        if counter >= 0:
            currentRoot.paramName = "True"
        else:
            currentRoot.paramName = "False"
    elif (len(currentValues) == 2):
        if posNegMatrix[0][0] > posNegMatrix[0][1]:
            if posNegMatrix[1][0] > posNegMatrix[1][1]:
                currentRoot.paramName = "False"
            else:
                currentRoot.insertChild("False")
                currentRoot.insertChild("True")
        else:
            if posNegMatrix[1][1] > posNegMatrix[1][0]:
                currentRoot.paramName = "True"
            else:
                currentRoot.insertChild("True")
                currentRoot.insertChild("False")
    else:
        currentRoot.insertChild(bestAttSoFar, currentValues)
        currentRoot.insertChild(bestAttSoFar, currentValues)
        calculateDecisionTree(currentRoot.leftVal)
        calculateDecisionTree(currentRoot.rightVal)

def getFeatureList(aminoName):
    aminoProperties = {
        # [Hydrophobic, Polar, Small, Proline, Tiny, Aliphatic,
        # Aromatic, Positive, Negative, Charged, Placeholder for B/E Val]
        'A': [1,0,1,0,1,0,0,0,0,0,0],
        'C': [1,0,1,0,0,0,0,0,0,0,0],
        'D': [0,1,1,0,0,0,0,0,1,1,0],
        'E': [0,1,0,0,0,0,0,0,1,1,0],
        'F': [1,0,0,0,0,0,1,0,0,0,0],
        'G': [1,0,1,0,1,0,0,0,0,0,0],
        'H': [0,1,0,0,0,0,1,1,0,1,0],
        'I': [1,0,0,0,0,1,0,0,0,0,0],
        'K': [0,1,0,0,0,0,0,1,0,1,0],
        'L': [1,0,0,0,0,1,0,0,0,0,0],
        'M': [1,0,0,0,0,0,0,0,0,0,0],
        'N': [0,1,1,0,0,0,0,0,0,0,0],
        'P': [1,0,1,1,0,0,0,0,0,0,0],
        'Q': [0,1,0,0,0,0,0,0,0,0,0],
        'R': [0,1,0,0,0,0,0,1,0,1,0],
        'S': [0,1,1,0,1,0,0,0,0,0,0],
        'T': [1,1,1,0,0,0,0,0,0,0,0],
        'V': [1,0,1,0,0,1,0,0,0,0,0],
        'W': [1,0,0,0,0,0,1,0,0,0,0],
        'Y': [1,1,0,0,0,0,1,0,0,0,0]}
    return aminoProperties[aminoName]
            
def getBaseArrayDict():
    arrayDict = {
        0:'Hydrophobic', 
        1:'Polar', 
        2:'Small', 
        3:'Proline',
        4:'Tiny', 
        5:'Aliphatic', 
        6:'Aromatic', 
        7:'Positive', 
        8:'Negative', 
        9:'Charged'}
    return arrayDict     

def getBEValues(aminoString, buriedExposedString):
    BEValueArray = [[0] for _ in range(len(aminoString))]
    for i in range(0, len(aminoString)):
        BEValueArray[i] = getFeatureList(aminoString[i])
        if(buriedExposedString[i] == 'B'):
            BEValueArray[i][10] = 0
        else:
            BEValueArray[i][10] = 1
    return BEValueArray

if __name__ == "__main__":
    trainAminoString = ""
    trainBuriedExposedString = ""
    testAminoString
    trueBuriedExposedString
    fileCounter = 0
    trainingRatio = 0.75   