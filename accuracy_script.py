import csv
import random
#from math import sqrt
#from sklearn.metrics import mean_squared_error
import numpy as np
def loadCsv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    return dataset

def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]



def FixedSplit(dataset,splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy= list(dataset)
    while len(trainSet) < trainSize:
        index=1
        trainSet.append(copy.pop(index))
    return [trainSet,copy]


def getAccuracy(testSetfixed, testSetfixed2):
    correct = 0
    cnt=0
    for i in range(1,len(testSetfixed)):
        if float(testSetfixed[i][3]) == float(testSetfixed2[i][2]):
            correct += 1

    return (correct)/float(len(testSetfixed)) * 100.0

def rmseErrorope(testSetfixed,testSetfixed2):
    #RMSE for ope
    print " FOR OPE:"
    for i in range(1,len(testSetfixed)):
        test1=float(testSetfixed[i][4])
        test2=float(testSetfixed2[i][3])
        rms1=np.sqrt(((test1-test2) **2)).mean()
    return rms1
def rmseErrorcon(testSetfixed,testSetfixed2):

    print " FOR CON:"
    for i in range(1,len(testSetfixed)):
        test1=float(testSetfixed[i][5])
        test2=float(testSetfixed2[i][4])
        rms2=np.sqrt(((test1-test2) **2)).mean()
    return rms2

def rmseErrorext(testSetfixed,testSetfixed2):

    print " FOR EXT:"
    for i in range(1,len(testSetfixed)):
        test1=float(testSetfixed[i][6])
        test2=float(testSetfixed2[i][5])
        rms3=np.sqrt(((test1-test2) **2)).mean()
    return rms3

def rmseErroragr(testSetfixed,testSetfixed2):
    print " FOR AGR:"
    for i in range(1,len(testSetfixed)):
        test1=float(testSetfixed[i][7])
        test2=float(testSetfixed2[i][6])
        rms4=np.sqrt(((test1-test2) **2)).mean()
    return rms4

def rmseErrorneu(testSetfixed,testSetfixed2):
    print " FOR NEU:"
    for i in range(1,len(testSetfixed)):
        test1=float(testSetfixed[i][8])
        test2=float(testSetfixed2[i][7])
        rms5=np.sqrt(((test1-test2) **2)).mean()
    return rms5

def main():
    filename='C:\Users\AadarshSam\Desktop\ML PROJECT\data\profile.csv'
    filename2= 'C:\Users\AadarshSam\Desktop\ML PROJECT\modelProfile.csv'
    splitRatio = 0.75
    dataset = loadCsv(filename)
    dataset2 = loadCsv(filename2)
    trainingSetori, testSetori = splitDataset(dataset, splitRatio)
    trainingSetmod, testSetmod = splitDataset(dataset2, splitRatio)
    trainingSetfixed, testSetfixed = FixedSplit(dataset,splitRatio)
    trainingSetfixed2, testSetfixed2 = FixedSplit(dataset2,splitRatio)
    print('Split Original data {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSetfixed), len(testSetfixed))
    print('Split Model data {0} rows into train={1} and test={2} rows').format(len(dataset2), len(trainingSetfixed2), len(testSetfixed2))
    accuracy_rand=getAccuracy(testSetori,testSetmod)
    accuracy = getAccuracy(testSetfixed,testSetfixed2 )
    print "Accuracy on the Fixed test data:"
    print accuracy
    print "Accuracy on random test data:"
    print accuracy_rand
    Rmse1= rmseErrorope(testSetfixed,testSetfixed2)
    print Rmse1
    Rmse2=rmseErrorcon(testSetfixed,testSetfixed2)
    print Rmse2
    Rmse3=rmseErrorext(testSetfixed,testSetfixed2)
    print Rmse3
    Rmse4=rmseErroragr(testSetfixed,testSetfixed2)
    print Rmse4
    Rmse5=rmseErrorneu(testSetfixed,testSetfixed2)
    print Rmse5
main()

