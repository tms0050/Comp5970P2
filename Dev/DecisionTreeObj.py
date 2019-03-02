'''
Created on Feb 28, 2019

@author: Tyler
'''

class DecisionTreeObj(object):
    '''
    classdocs
    '''


    def __init__(self, objectName=None, valueMatrix=None):
        self.leftVal = None
        self.rightVal = None
        self.paramName = objectName
        self.values = valueMatrix
        '''
        Constructor
        '''
    
    def insertChild(self, objectName=None, valueMatrix=None):
        if self.leftVal is None:
            self.leftVal = DecisionTreeObj(objectName, valueMatrix)
        else:
            self.rightVal = DecisionTreeObj(objectName, valueMatrix)
            
    def getName(self):
        return self.paramName
    
    def getValues(self):
        return self.values