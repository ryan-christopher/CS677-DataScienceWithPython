'''
Ryan Christopher
Class: CS 677
Date: 11/12/2023
Assignment 5 Question 2

=======Description of Problem=======
Take the dataset and split it 50/50, train Naive Bayesian on the training set, 
and predict the class labels in the test set. Then determine the accuracy 
and compute the confusion matrix.
'''
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from assignClass import assignClass

# nb 
def nb():
    # call assignClass to gather data and classes
    ctg = assignClass()
    train, test = train_test_split(ctg, test_size = 0.5, 
                                   train_size = 0.5, random_state = 13)
    model = GaussianNB()