'''
Ryan Christopher
Class: CS 677
Date: 9/19/2023
Assignment 2 Question 2

=======Description of Problem=======

'''
import pandas as pd
from true_label import getTable
global wVal

cost_stock_data = getTable('COST')

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

def predictWSequence(df, w):
    global true_labels
    global wVal
    true_labels, wVal = "", w
    df.apply(gatherTrainingLabels, axis = 1)
    wList = [val for val in range(w + 1)]
    shiftValues = df['True Label'].shift(periods=wList)
    for i in range(1, w + 1):
        df['Day-' + str(i)] = shiftValues['True Label_' + str(i)]
    df = df.apply(generateLabelSequence, axis = 1)
    print(df)
    return df

cost_stock_data = predictWSequence(cost_stock_data, 4)