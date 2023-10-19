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



# generatePairwise takes as input a dataframe, splits the 
# data into two sets as a 50/50 split, and outputs the 
# pairwise releationship
def generatePairwise(df):
    x_train, x_test = train_test_split(df, test_size = 0.5, train_size = 0.5)
    print(x_train)

    #class_0 = x_train.where(x_train['Class'] == 0).dropna().drop('Class', axis = 1)
    class_1 = x_train.where(x_train['Class'] == 1).dropna().drop('Class', axis = 1)

    print(class_1)

    sns.pairplot(class_1)
    plt.show()

generatePairwise(bank_note_data)
