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

# read CSV data and store into dataframe called stock_data
stock_data = pd.read_csv('assignment2/stock_data/COST.csv')

# remove extra info that we will not need to use
stock_data = stock_data.drop(['Week_Number', 'Year_Week', 'Open', 'High', 'Low', 
                  'Close', 'Volume', 'Adj Close', 'Short_MA', 'Long_MA'], 
                  axis = 1)

# ========== Part 1 ==========

# determineTrueValue assigns the True Value column to + if the 
# day's return is positive, and - if the day's return is negative
def determineTrueValue(df):
    if float(df['Return']) >= 0:
        df['True Value'] = '+'
    else:
        df['True Value'] = '-'
    return df

# use the apply method on the dataframe to assign the correct 
# True Value for each day
stock_data = stock_data.apply(determineTrueValue, axis = 1)
# print(stock_data)

# ========== Part 2 ==========

# taking years 1, 2, and 3, determine the probability
# of the next day being an "up" day

true_labels = ""

def gatherValues(df):
    global true_labels
    if int(df['Year']) < 2019:
        true_labels += df['True Value']

def upDayProb(df):
    global true_labels
    true_labels = ""
    df.apply(gatherValues, axis = 1)
    return true_labels.count("+") / len(true_labels)

# print(upDayProb(stock_data))

# ========== Part 3 and 4 ==========

def kSequenceProbability(df, sequenceVal, targetVal):
    global true_labels
    true_labels, probabilities = "", []
    df.apply(gatherValues, axis = 1)
    for k in [1, 2, 3]:
         numTarget = true_labels.count((sequenceVal * k) + targetVal)
         numOpposite = true_labels.count((sequenceVal * k) + sequenceVal)
         probabilities.append(numTarget / (numTarget + numOpposite))
    return probabilities

print(kSequenceProbability(stock_data, '-', '+'))
print(kSequenceProbability(stock_data, '+', '-'))
