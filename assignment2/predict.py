'''
Ryan Christopher
Class: CS 677
Date: 9/19/2023
Assignment 2 Question 2

=======Description of Problem=======

'''
import pandas as pd
from true_label import getTable
global wVal, accuracies, valuesDict

cost_stock_data = getTable('COST')
spy_stock_data = getTable('SPY')

# create global level string to store sequence of +'s and -'s
# (global level works best as it is mainly 
# being used with an apply method)
true_labels = ""

# gatherTrainingLabels is a helper function that takes a given
# day's True Label and adds it to the string true_labels
def gatherTrainingLabels(df):
    global true_labels
    if int(df['Year']) < 2019:
        true_labels += df['True Label']


def generateLabelSequence(df):
    global wVal
    for i in range(1, wVal + 1):
        df["Past" + str(i)] = "*" * i
    if int(df['Year']) > 2018:
        sequence = ""
        for i in range(1, wVal + 1):
            sequence += df['Day-' + str(i)]
            df["Past" + str(i)] = sequence
    return df


def generateProbabilities(df):
    global true_labels
    global wVal
    if int(df['Year']) > 2018:
        ensemble = ''
        for i in range(2, wVal + 1):
            seqAndUp = true_labels.count(df['Past' + str(i)] + '+')
            seqAndDown = true_labels.count(df['Past' + str(i)] + '-')
            if seqAndUp > seqAndDown:
                df['w=' + str(i)] = '+'
                ensemble += '+'
            else:
                df['w=' + str(i)] = '-'
                ensemble += '-'
        if ensemble.count('+') > 1:
            df['Ensemble'] = '+'
        else:
            df['Ensemble'] = '-'
    return df

def calculateAccuracy(df):
    global wVal, accuracies, valuesDict
    if int(df['Year']) > 2018:
        for i in range(2, wVal + 1):
            if df['w=' + str(i)] == df['True Label']:
                valuesDict['W=' + str(i)].append(True)
            else:
                valuesDict['W=' + str(i)].append(False)
        if df['Ensemble'] == df['True Label']:
            valuesDict['Ensemble'].append(True)
        else:
            valuesDict['Ensemble'].append(False)
        
    

def predictWSequence(df, w):
    global true_labels, wVal, accuracies, valuesDict
    true_labels, wVal = "", w
    df.apply(gatherTrainingLabels, axis = 1)
    wList = [val for val in range(w + 1)]
    shiftValues = df['True Label'].shift(periods=wList)
    for i in range(1, w + 1):
        df['Day-' + str(i)] = shiftValues['True Label_' + str(i)]
    df = df.apply(generateLabelSequence, axis = 1)
    #print(df)
    df = df.apply(generateProbabilities, axis = 1)
    df = df.dropna()
    #print(df)
    accuracies, valuesDict = {}, {}
    for i in range(2, wVal + 1):
        valuesDict['W=' + str(i)] = []
    valuesDict['Ensemble'] = []
    df.apply(calculateAccuracy, axis = 1)
    #print(valuesDict)
    for i in range(2, wVal + 1):
        accuracies['W=' + str(i) + ' Accuracy : '] = str(valuesDict['W=' + str(i)].count(True) / len(valuesDict['W=' + str(i)]))
    accuracies['Ensemble'] = str(valuesDict['Ensemble'].count(True) / len(valuesDict['Ensemble']))
    #print(accuracies)
    print(df.to_string())
    return df

cost_stock_data = predictWSequence(cost_stock_data, 4)
#spy_stock_data = predictWSequence(spy_stock_data, 4)