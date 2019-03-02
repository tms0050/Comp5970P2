'''
Created on Feb 25, 2019

@author: Tyler
'''
import math
import os
import DecisionTreeObj

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

# How to iterate through directory source:
# https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
# How to get a singular file:
# https://stackoverflow.com/questions/13223737/how-to-read-a-file-in-other-directory-in-python
def calculateDecisionMatrix():
    decisionMatrix = [[0 for _ in range(0, 8)] for _ in range(0, 150)]
    if not os.path.exists('X:\\fasta'):
        return 0
    fileLoc = 0
    for file in os.listdir('X:\\fasta'):
        filename = os.fsdecode(file)
        fastaFile = open('X:\\fasta\\' + filename, 'r')
        fastaLine = ""
        saLine = ""
        for i, line in enumerate(fastaFile):
            fastaLine = line
        saFilename = filename[:4] + '.sa'
        saFile = open('X:\\sa\\'+saFilename, 'r')
        for i, line in enumerate(saFile):
            saLine = line
        buriedVal = saLine.count('B')
        exposedVal = saLine.count('E')
        if buriedVal > (3 * exposedVal):
            decisionMatrix[fileLoc][7] = 0
        else:
            decisionMatrix[fileLoc][7] = 1
        optimalVal = calculateHighestOccurences(fastaLine[:len(fastaLine) - 1])
        for i in range(0, 7):
            decisionMatrix[fileLoc][i] = optimalVal[i]
        fileLoc+=1
    return decisionMatrix

def calculateHighestOccurences(aminoList):
    valueCounter = [[0 for _ in range(0, 3)] for _ in range(0,7)]
    aminoProperties = {
        # [Hydrophobic, Polar, Small, Proline, Tiny, Aliphatic,
        # Aromatic, Positive, Negative, Charged]
        'A': [1,0,1,0,1,0,0,0,0,0],
        'C': [1,0,1,0,0,0,0,0,0,0],
        'D': [0,1,1,0,0,0,0,0,1,1],
        'E': [0,1,0,0,0,0,0,0,1,1],
        'F': [1,0,0,0,0,0,1,0,0,0],
        'G': [1,0,1,0,1,0,0,0,0,0],
        'H': [0,1,0,0,0,0,1,1,0,1],
        'I': [1,0,0,0,0,1,0,0,0,0],
        'K': [0,1,0,0,0,0,0,1,0,1],
        'L': [1,0,0,0,0,1,0,0,0,0],
        'M': [1,0,0,0,0,0,0,0,0,0],
        'N': [0,1,1,0,0,0,0,0,0,0],
        'P': [1,0,1,1,0,0,0,0,0,0],
        'Q': [0,1,0,0,0,0,0,0,0,0],
        'R': [0,1,0,0,0,0,0,1,0,1],
        'S': [0,1,1,0,1,0,0,0,0,0],
        'T': [1,1,1,0,0,0,0,0,0,0],
        'V': [1,0,1,0,0,1,0,0,0,0],
        'W': [1,0,0,0,0,0,1,0,0,0],
        'Y': [1,1,0,0,0,0,1,0,0,0]}
    for i in range(0, len(aminoList)):
        currentChar = aminoProperties[aminoList[i]]
        for j in range(0, 7):
            valueCounter[j][currentChar[j]]+=1
    optimalMatrix = [0 for _ in range(0, 7)]
    for i in range(0, 7):
        if (valueCounter[i][2] > valueCounter[i][1]) & (valueCounter[i][2] > valueCounter[i][0]):
            optimalMatrix[i] = 2
        elif valueCounter[i][1] > valueCounter[i][0]:
            optimalMatrix[i] = 1
        else:
            optimalMatrix[i] = 0
    return optimalMatrix
            
        
        