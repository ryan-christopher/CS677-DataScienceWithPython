'''
Ryan Christopher
Class: CS 677
Date: 9/19/2023
Assignment 2 Question 1

=======Description of Problem=======
Taking the csv of my stock and SPY, create a dataframe with that info.
Then, add in a column of the "True Value" of the stock as a + or -,
and write a function that can determine the likelihood of a day's "True Value"
based off the prior sequence of up and down days.
'''

import pandas as pd

data = pd.read_csv('assignment2/stock_data/COST.csv')
print(data)