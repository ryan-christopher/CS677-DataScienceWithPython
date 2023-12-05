'''
Ryan Christopher
Class: CS 677
Date: 11/30/2023
Assignment 6 Question 1

=======Description of Problem=======
Using a 50/50 split for training and testing, implement a linear kernel SVM, 
Gaussian kernel SVM, and polynomial kernel SVM of degree 3 on the dataset.
For each of the three, calculate the accuracy and generate a conusion 
matrix.
'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# the last digit in my id is 0, so I'll say that my remainder R is
# 0 as my result is undefined.
# For my file, class L = 1 = negative
#                and L = 2 = positive

# load data takes the csv file and loads it into a dataframe
def loadData():
    # store column names
    col_names = ["Area", "Perimeter", "Compactness", "Length", "Width", "Asymmetry",
                "GrooveLength", "Class"]
    
    # read CSV data and store into dataframe
    seed_data = pd.read_csv('assignment6/data/seeds_dataset.csv', names = col_names, 
                            header=None, delim_whitespace=True)
    
    # get subset of class L = 1 and L = 2
    seed_data = seed_data.where(seed_data['Class'] != 3).dropna()
    
    return seed_data

seeds = loadData()

# applySVM takes a dataset and kernel type as input then splits the dataset with
# a 50/50 split and fits the train data to the specified kernel type of SVM. 
# It then predicts the y values for the test data, calculates the accuracy, 
# and displayes 
def applySVM(seeds, kernelType):

        # split dataset 50/50
        train, test = train_test_split(seeds, test_size = 0.5, 
                                       train_size = 0.5, random_state = 13)
        
        # gather train and test data
        x_train = train.iloc[:,0:7]
        y_train = train["Class"]
        x_test = test.iloc[:, 0:7]
        y_test = test["Class"]

        # instantiate svc
        linear_svm = SVC(kernel=kernelType)
        # fit to train data
        linear_svm.fit(x_train, y_train)
        # predict y values
        y_predict = linear_svm.predict(x_test)

        # display accuracy
        print(accuracy_score(y_test, y_predict))
    
        # compute confusion matrix, then plot corresponding heatmap
        mat = confusion_matrix(y_test, y_predict)
        sns.heatmap(mat.T, square=True, annot=True, fmt = 'd', cbar=True, 
                xticklabels=["L = 1", "L = 2"], yticklabels=["L = 1", "L = 2"])
        plt.xlabel('true label')
        plt.ylabel('predicted label')
        plt.suptitle(kernelType)

        # display heatmap
        plt.show()


applySVM(seeds, "linear")
applySVM(seeds, "rbf")
applySVM(seeds, "poly")