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
    fastaDir = os.fsencode("C:\Users\Tyler\eclipse-workspace\Comp5970P2\5970_6970_SP_19_PROJECT_2\fasta")
    decisionMatrix = [[0 for _ in range(0, 150)] in range(0, 8)]
    fileLoc = 0
    saDir = os.fsencode("C:\Users\Tyler\eclipse-workspace\Comp5970P2\5970_6970_SP_19_PROJECT_2\sa")
    for file in os.listdir(fastaDir):
        filename = os.fsdecode(file)
        saFilename = filename[:4] + ".sa"
        saFile = open(saDir+saFilename, "r")
        buriedVal = saFile.readline().count('B')
        exposedVal = saFile.readline().count('E')
        if buriedVal > exposedVal:
            decisionMatrix[fileLoc][7] = 0
        else:
            decisionMatrix[fileLoc][7] = 1
        optimalVal = calculateHighestOccurences(file.readline())
        for i in range(0, 7):
            decisionMatrix[fileLoc][i] = optimalVal[i]
        fileLoc+=1
    return decisionMatrix

def calculateHighestOccurences(aminoList):
    valueCounter = [[0 for _ in range(0, 3)] for _ in range(0,7)]
    aminoProperties = {
        'A': [1,0,0,1,1,0,0],
        'C': [1,0,0,1,0,0,0],
        'D': [0,1,1,1,0,0,0],
        'E': [0,1,1,0,0,0,1],
        'F': [1,0,0,0,0,1,1],
        'G': [1,0,0,1,1,0,0],
        'H': [0,1,2,0,0,1,1],
        'I': [1,0,0,0,0,2,1],
        'K': [0,1,2,0,0,0,1],
        'L': [1,0,0,0,0,2,1],
        'M': [1,0,0,0,0,0,1],
        'N': [0,1,0,1,0,0,0],
        'P': [1,0,0,1,0,0,0],
        'Q': [0,1,0,0,0,0,1],
        'R': [0,1,2,0,0,0,1],
        'S': [0,1,0,1,1,0,0],
        'T': [1,1,0,1,0,0,0],
        'V': [1,0,0,1,0,2,1],
        'W': [1,0,0,0,0,1,1],
        'Y': [1,1,0,0,0,1,1]}
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
            
        
        