'''
Ryan Christopher
Class: CS 677
Date: 9/19/2023
Assignment 2 Question 2

=======Description of Problem=======

'''
import pandas as pd
from true_value import getTable

stock_data = getTable('COST')
print(type(stock_data))

def predictWSequence(df, w):
    wList = [val for val in range(w + 1)]
    shiftValues = df['True Value'].shift(periods=wList)
    for i in range(1, w + 1):
        df['Day-' + str(i)] = shiftValues['True Value_' + str(i)]
    print(shiftValues)
    return df

shift = predictWSequence(stock_data, 4)
print(shift)