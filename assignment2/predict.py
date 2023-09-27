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

def shiftTest(df):
    return df['True Value'].shift(periods=[0, 1, 2, 3, 4])

shift = shiftTest(stock_data)
print(shift)