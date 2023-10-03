'''
Ryan Christopher
Class: CS 677
Date: 10/3/2023
Assignment 2 Question 2, 3, and 4

=======Description of Problem=======
With the dataframe of daily stock data, create a prediction model that takes
the past w days where w = 2, 3, and 4, and using the first three years as 
training data calculate the likelihood of the next day being either positive or
negative. 
Then, with the predictions for w = 2, 3, and 4, generate an ensemble prediction
from the three predictions. 
'''
import pandas as pd
from true_label import getTable
global wVal, accuracies

cost_stock_data = getTable('COST')
spy_stock_data = getTable('SPY')

# gatherTrainingLabels is a helper function that takes a given
# day's True Label and adds it to the string true_labels
def gatherTrainingLabels(df):
    global true_labels
    df['Date'] = int(df['Date'][:4])
    if df['Date'] < 2019:
        true_labels += df['TL']
    return df

def generatePrediction(df):
    global wVal
    ensemble = ''
    for i in range(2, wVal + 1):
        upSequence = true_labels.count(df['-' + str(i-1)] + '+')
        downSequence = true_labels.count(df['-' + str(i-1)] + '-')
        if upSequence >= downSequence:
            df['w=' + str(i)] = '+'
            ensemble += '+'
        else:
            df['w=' + str(i)] = '-'
            ensemble += '-'
    if ensemble.count('+') > ensemble.count('-'):
        df['Ensemble'] = '+'
    else:
        df['Ensemble'] = '-'
    return df

def calcAccuracy(df):
    global wVal, accuracies
    for i in range(2, wVal + 1):
        if df['w=' + str(i)] == df['Next']:
            accuracies['w=' + str(i)]['Correct'].append("True")
            if df['Next'] == '+':
                accuracies['w=' + str(i)]['TP'] += 1
            else:
                accuracies['w=' + str(i)]['TN'] += 1
        else:
            accuracies['w=' + str(i)]['Correct'].append("False")
            if df['Next'] == '+':
                accuracies['w=' + str(i)]['FN'] += 1
            else:
                accuracies['w=' + str(i)]['FP'] += 1
    if df['Ensemble'] == df['Next']:
        accuracies['Ensemble']['Correct'].append('True')
        if df['Next'] == '+':
            accuracies['Ensemble']['TP'] += 1
        else:
            accuracies['Ensemble']['TN'] += 1
    else:
        accuracies['Ensemble']['Correct'].append('False')
        if df['Next'] == '+':
            accuracies['Ensemble']['FN'] += 1
        else:
            accuracies['Ensemble']['FP'] += 1


def predictLabels(df, w):
    global wVal, accuracies, true_labels
    wVal = w
    accuracies = {}
    for i in range(2, w + 1):
        accuracies['w=' + str(i)] = {
            'Correct' : [], 'Accuracy' : 0,
            'TP' : 0, 'FP' : 0, 'TN' : 0,
            'FN' : 0, 'TPR' : 0, 'TNR' : 0
        }
    accuracies['Ensemble'] = {
        'Correct' : [], 'Accuracy' : 0,
        'TP' : 0, 'FP' : 0, 'TN' : 0,
        'FN' : 0, 'TPR' : 0, 'TNR' : 0
    }

    true_labels = ""

    # GENERATE TRAINING TL SEQUENCE
    df = df.apply(gatherTrainingLabels, axis = 1)

    # GENERATE SHIFTED COLUMNS
    shiftValues = df['TL'].shift(periods=[1, 2, 3])
    for i in range(1, w):
        df['-' + str(i)] = shiftValues['TL_' + str(i)]

    df['Next'] = df['TL'].shift(-1)

    df = df[df['Date'] > 2018]

    for i in range(1, w):
        if i == 1:
            df['-' + str(i)] = df['-' + str(i)] + df['TL']
        else:
            df['-' + str(i)] = df['-' + str(i)] + df['-' + str(i - 1)]

    colsOrder = []

    for i in range((w-1) * -1, 0):
        colsOrder.append(str(i))

    colsOrder.append('TL')
    colsOrder.append('Next')
    colsOrder.append('Return')

    df = df[colsOrder]

    for i in range(2, w + 1):
        df['w=' + str(i)] = ''

    df = df.apply(generatePrediction, axis = 1)

    df.apply(calcAccuracy, axis = 1)

    for key, vals in accuracies.items():
        print("KEY : " + key)
        vals['Accuracy'] = vals['Correct'].count('True') / len(vals['Correct'])
        vals['TPR'] = vals['TP'] / (vals['TP'] + vals['FN'])
        vals['TNR'] = vals['TN'] / (vals['TN'] + vals['FP'])
        # print('TP', vals['TP'])
        # print('FP', vals['FP'])
        # print('TN', vals['TN'])
        # print('FN', vals['FN'])
        # print('Accuracy', vals['Accuracy'])
        # print('TPR', vals['TPR'])
        # print('TNR', vals['TNR'])
        del accuracies[key]['Correct']
    #print(accuracies)
    #print(df)
    return df


#print("Cost")
#print(predictLabels(cost_stock_data, 4))
#print("===================")
#print("Spy")
#print(predictLabels(spy_stock_data, 4))