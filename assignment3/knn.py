'''
Ryan Christopher
Class: CS 677
Date: 10/7/2023
Assignment 3 Question 3

=======Description of Problem=======
Taking the train and test data from the original 
50/50 split, use k-NN for the values k = 3, 5, 7, 9, 11
to determine the best k value for accuracy. 
'''
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# load train and test data from original split
train_data = pd.read_csv('assignment3/banknote_data/train.csv')
test_data = pd.read_csv('assignment3/banknote_data/test.csv')

def knn(train, test):
    # gather train/test x and y values from split data sets
    train_x = train.iloc[:, 0:4]
    train_y = train['Class']
    test_x = test.iloc[:, 0:4]
    test_y = test['Class']

    # scale values using StandardScaler
    standardScaler = StandardScaler()
    train_x_scaled = standardScaler.fit_transform(train_x)
    test_x_scaled = standardScaler.fit_transform(test_x)

    # create list to store accuracies for each k value
    k_accuracies = []

    # create list of k values to iterate over
    k_vals = [3,5,7,9,11]

    for k in k_vals:
        # apply knn classifier for each value of k = 3, 5, 7, 9, 11
        classifier = KNeighborsClassifier(n_neighbors=k)

        # fit classifier to x training data
        classifier.fit(train_x_scaled, train_y)

        # predict test values using classifier fit to train values
        y_predict = classifier.predict(test_x_scaled)

        if k == 5:
            print(y_predict)
            print(len(y_predict))

        # append the accuracy to k_accuracies list
        k_accuracies.append(accuracy_score(test_y, y_predict))

    # display list of accuracies for k
    print(k_accuracies)

    # create plot of accuracies vs k values
    # kplot = plt.axes()
    # kplot.set_xticks(k_vals)
    # plt.plot(k_vals, k_accuracies)
    # plt.xlabel('k')
    # plt.ylabel('Accuracy')
    # plt.title('Accuracy vs k')
    # plt.show()


knn(train_data, test_data)