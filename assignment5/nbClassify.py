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
from sklearn.metrics import accuracy_score


# nb takes the dataset, splits it 50/50, selects the features 
# of group 2, predicts the test set classes, and computes 
# then displays the confusion matrix
def nb():
    # call assignClass to gather data and classes
    ctg = assignClass()

    # select group 2 features (ASTV, MLTV, Max, Median)
    x = ctg[['ASTV', 'MLTV', 'Max', 'Median']]

    # select y values
    y = ctg['NSP']

    # split set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5, 
                                   train_size = 0.5, random_state = 13)

    # instantiate Gaussian NB model
    model = GaussianNB()

    # fit data to model and predict
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)

    # display accuracy
    print(accuracy_score(y_test, y_predict))

    # compute confusion matrix, then plot corresponding heatmap
    mat = confusion_matrix(y_test, y_predict)
    sns.heatmap(mat.T, square=True, annot=True, fmt = 'd', cbar=True, 
                xticklabels=['abnormal', 'normal'], yticklabels=['abnormal', 'normal'])
    plt.xlabel('true label')
    plt.ylabel('predicted label')

    # display heatmap
    plt.show()

nb()