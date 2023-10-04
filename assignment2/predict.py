'''
Ryan Christopher
Class: CS 677
Date: 10/3/2023
Assignment 2 Questions 2, 3, and 4

=======Description of Problem=======
With the dataframe of daily stock data, create a prediction model that takes
the past w days where w = 2, 3, and 4, and using the first three years as 
training data calculate the likelihood of the next day being either 
positive or negative. 
Then, with the predictions for w = 2, 3, and 4, generate an ensemble 
prediction from the three predictions. 
'''
import pandas as pd
from true_label import getTable, countOccurences
global wVal, accuracies

cost_stock_data = getTable('COST')
spy_stock_data = getTable('SPY')

# gatherTrainingLabels is a helper function that takes a given
# day's True Label and adds it to the string true_labels
def gatherTrainingLabels(df):
    # get global variable true_labels so it can be used by
    # other functions
    global true_labels

    # reassign 'Date' column to only have the year
    df['Date'] = int(df['Date'][:4])

    # only add day's True Label to true_labels if the 
    # year is before 2019
    if df['Date'] < 2019:
        true_labels += df['TL']

    # return row
    return df

# generatePrediction counts the sequence of w days and checks how many
# times w days + '+' occur as well as how many times w days + '-'
# occur to determine the prediction of the next day's value
def generatePrediction(df):
    # get global wVal
    global wVal

    # assign ensemble value to be empty string at start of each row
    ensemble = ''

    # for each w val from 2 to w, count number of occurences of prior w days
    # with '+' and '-' to calculate prediction of next day's true label
    for i in range(2, wVal + 1):

        # generate number of sequences ending in '+'
        upSequence = countOccurences(true_labels, df['-' + str(i-1)] + '+')
        #upSequence = true_labels.count(df['-' + str(i-1)] + '+')

        # generate number of sequences ending in '-'
        downSequence = countOccurences(true_labels, df['-' + str(i-1)] + '-')
        #downSequence = true_labels.count(df['-' + str(i-1)] + '-')

        # assign prediction for next day to '+' if there are more occurences 
        # of the sequence ending in '+' than the sequence ending in '-'
        if upSequence >= downSequence:
            df['w=' + str(i)] = '+'
            ensemble += '+'

        # otherwise predict '-' for next day
        else:
            df['w=' + str(i)] = '-'
            ensemble += '-'

    # determine majority of ensemble string, assign '+' if there are more
    # '+' predictions and '-' if there are more '-' predictions
    if ensemble.count('+') > ensemble.count('-'):
        df['Ensemble'] = '+'
    else:
        df['Ensemble'] = '-'

    # return row
    return df

# calcStats takes a row as input, and adds up the number of 
# True/False Positives and True/False Negatives
def calcStats(df):
    # gather global vals for w and accuracies dict
    global wVal, accuracies

    # for each day, examine the columns for w = 2, 3, and 4 and 
    # compare the predicted value to the next day's true label
    for i in range(2, wVal + 1):
        if df['w=' + str(i)] == df['Next']:
            # Add prediction as correct
            accuracies['w=' + str(i)]['Correct'].append("True")

            # Check if true label is positive to update
            # accuracies dict for TP and TN count
            if df['Next'] == '+':
                accuracies['w=' + str(i)]['TP'] += 1
            else:
                accuracies['w=' + str(i)]['TN'] += 1

        else:
            # Add prediction as incorrect
            accuracies['w=' + str(i)]['Correct'].append("False")

            # Check if true label is positive or negative
            # accuracies dict for TP and TN count
            if df['Next'] == '+':
                accuracies['w=' + str(i)]['FN'] += 1
            else:
                accuracies['w=' + str(i)]['FP'] += 1
    
    if df['Ensemble'] == df['Next']:
        # add ensemble as correctly predicted if the same as next day's True Label
        accuracies['Ensemble']['Correct'].append('True')
        if df['Next'] == '+':
            accuracies['Ensemble']['TP'] += 1
        else:
            accuracies['Ensemble']['TN'] += 1
    else:
        # add ensemble as incorrectly predicted if the same as next day's True Label
        accuracies['Ensemble']['Correct'].append('False')
        if df['Next'] == '+':
            accuracies['Ensemble']['FN'] += 1
        else:
            accuracies['Ensemble']['FP'] += 1

# predictLabels takes in a dataframe and w sequences, and uses helper functions 
# through the apply method to generate the predicted labels for w from 2 up 
# to w as well as the ensemble prediction
def predictLabels(df, w):
    # get global variables for w, accuracies dictionary, and
    # true labels list
    global wVal, accuracies, true_labels
    # assign global variable wVal to w and accuracies to blank dictionary
    wVal, accuracies = w, {}

    # include dictionary to keep list of correct/incorrect predictions,
    # accuracy (to be calculated later), TP, FP, TN, FN, TPR, and TNR 
    # for each value for w and ensemble
    for i in range(2, w + 1):
        accuracies['w=' + str(i)] = {
            'Correct' : [], 'Accuracy' : 0, 'TP' : 0, 'FP' : 0, 
            'TN' : 0, 'FN' : 0, 'TPR' : 0, 'TNR' : 0
        }
    accuracies['Ensemble'] = {
        'Correct' : [], 'Accuracy' : 0, 'TP' : 0, 'FP' : 0, 
        'TN' : 0, 'FN' : 0, 'TPR' : 0, 'TNR' : 0 
    }

    # set true_labels to be empty at first
    true_labels = ""

    # generate training label sequence to update 
    # true_labels
    df = df.apply(gatherTrainingLabels, axis = 1)

    # generate shifted columns to store previous w days
    # worth of true labels
    shiftValues = df['TL'].shift(periods=[1, 2, 3])
    for i in range(1, w):
        df['-' + str(i)] = shiftValues['TL_' + str(i)]

    # add column to include the next day's True Label
    # that can be used to compare predictions
    df['Next'] = df['TL'].shift(-1)

    # remove days that are part of training data
    df = df[df['Date'] > 2018]

    # generate prior w days sequence (including current day)
    for i in range(1, w):
        # place current day in front
        if i == 1:
            df['-' + str(i)] = df['-' + str(i)] + df['TL']
        # place w+1 days sequence ahead of current day's label
        else:
            df['-' + str(i)] = df['-' + str(i)] + df['-' + str(i - 1)]

    # create colsOrder list to store new order of columns
    colsOrder = []
    # add in -w days columns
    for i in range((w-1) * -1, 0):
        colsOrder.append(str(i))
    # add columns for TL, Next, and Return
    colsOrder = colsOrder + ['TL', 'Next', 'Return']
    # rearrange df to be in colsOrder
    df = df[colsOrder]

    # add in column for label predictions for w sequences
    for i in range(2, w + 1):
        df['w=' + str(i)] = ''

    # apply generatePrediction then calcStats methods on df
    df = df.apply(generatePrediction, axis = 1)
    df.apply(calcStats, axis = 1)

    # calculate Accuracy, TPR, and TNR by using the Correct list,
    # TP, FP, TN, and FN sums
    for key, vals in accuracies.items():
        vals['Accuracy'] = vals['Correct'].count('True') / len(vals['Correct'])
        vals['TPR'] = vals['TP'] / (vals['TP'] + vals['FN'])
        vals['TNR'] = vals['TN'] / (vals['TN'] + vals['FP'])

        # print("KEY : " + key)
        # print('TP', vals['TP'])
        # print('FP', vals['FP'])
        # print('TN', vals['TN'])
        # print('FN', vals['FN'])
        # print('Accuracy', vals['Accuracy'])
        # print('TPR', vals['TPR'])
        # print('TNR', vals['TNR'])

        # remove Correct list to make prining the accuracies dict not 
        # take up the entire page
        del accuracies[key]['Correct']

    # return both the dataframe and accuracies dictionary
    return df, accuracies

# print("Cost")
# print(predictLabels(cost_stock_data, 4))
# print("Spy")
# print(predictLabels(spy_stock_data, 4))