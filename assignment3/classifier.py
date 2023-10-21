'''
Ryan Christopher
Class: CS 677
Date: 10/7/2023
Assignment 3 Question 2

=======Description of Problem=======
Take the dataset of banknotes, and separate it into a 50/50 split of X(train)
and X(test). Then, plot the pairwise relationships in X(train) separately 
for class 0 and class 1 entries. 
'''
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from assign_class import createFrame
from sklearn.model_selection import train_test_split


# create dataframe with banknote data
bank_note_data = createFrame()


# applies simple classifier logic to each row of the dataframe
def simpleClassifier(df):
    # variance > 0, skewness > 0, curtosis > 0, if TWO of 
    # the three are true then it is real
    if ((df['Variance'] > 0 and df['Skewness'] > 0) or 
        (df['Variance'] > 0 and df['Curtosis'] > 0) or
        (df['Skewness'] > 0 and df['Curtosis'] > 0)):
        df['SC-Guess'] = 'green'    
    # otherwise, it is fake
    else:
        df['SC-Guess'] = 'red'
    
    # assign a True/False indicator to show which values 
    # were correctly/incorrectly guessed
    if df['Color'] == df['SC-Guess']:
        df['SC-Result'] = 'True'
    else:
        df['SC-Result'] = 'False'

    return df


# generatePairwise takes as input a dataframe, splits the 
# data into two sets as a 50/50 split, and outputs the 
# pairwise releationship
def generatePairwise(df):
    # create train and test datasets with 50/50 split
    # train, test = train_test_split(df, test_size = 0.5, train_size = 0.5)
    
    # save split datasets to csv files for consistency 
    # ==== DO NOT UNCOMMENT NEXT 2 LINES ==== will overwrite saved datasets
    # train.to_csv('train.csv',index=False)
    # test.to_csv('test.csv',index=False)

    # load saved split data to dataframe
    train_data = pd.read_csv('assignment3/banknote_data/train.csv')
    test_data = pd.read_csv('assignment3/banknote_data/test.csv')

    # to create plots, separate into class 0 and class 1 dataframes
    # class_0 = train_data.where(train_data['Class'] == 0).dropna().drop('Class', axis = 1)
    # class_1 = train_data.where(train_data['Class'] == 1).dropna().drop('Class', axis = 1)

    # use seaborn pairplot to generate plot for each class
    # sns.pairplot(class_0)
    # sns.pairplot(class_1)
    # plt.show()

    test_data = test_data.apply(simpleClassifier, axis = 1)

    # after simple classifier applied, determine stats
    # for TP, FP, TN, FN, Accuracy, TPR, and TNR
    tp = len(test_data.where((test_data['Color'] == 'green') & (test_data['SC-Result'] == 'True')).dropna())
    fp = len(test_data.where((test_data['Color'] == 'green') & (test_data['SC-Result'] == 'False')).dropna())
    tn = len(test_data.where((test_data['Color'] == 'red') & (test_data['SC-Result'] == 'True')).dropna())
    fn = len(test_data.where((test_data['Color'] == 'red') & (test_data['SC-Result'] == 'False')).dropna())
    acc = test_data['SC-Result'].value_counts()['True'] / len(test_data)

    # display performance measures
    print('TP:', tp, 'FP:', fp)
    print('TN:', tn, 'FN:', fn)
    print('Accuracy:', acc)
    print('TPR', tp / (tp + fn))
    print('TNR', tn / (tn + fp))
    

#generatePairwise(bank_note_data)