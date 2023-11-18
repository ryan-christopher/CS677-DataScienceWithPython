'''
Ryan Christopher
Class: CS 677
Date: 11/17/2023
Assignment 5 Question 3

=======Description of Problem=======
Take the dataset and split it 50/50, train Random Forest on the training set for n values 
(num of sub trees) 1 through 10 and d values 1 through 5 (max depth). Train the set 
with the random tree classifier, compute the error rate for the test set, and plot the error
rates to find the best combination of n and d. Then determine the accuracy and compute the 
confusion matrix of the best combination of n and d.
'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from assignClass import assignClass
from sklearn.metrics import accuracy_score

# randomForest
def randomForest():
    # call assignClass to gather data and classes
    ctg = assignClass()

    # select group 2 features (ASTV, MLTV, Max, Median)
    x = ctg[['ASTV', 'MLTV', 'Max', 'Median']]

    # select y values
    y = ctg['NSP']

    # split set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5, 
                                   train_size = 0.5, random_state = 13)

    best_combination = {
        'n' : 0,
        'd' : 0,
        'accuracy' : 0,
        'error rate' : 0,
        'y_predict' : []
    }

    for n in range(1, 11):
        for d in range(1, 6):
            # instantiate random forest classifier with n subtrees and max depth d
            model = RandomForestClassifier(n_estimators = n, max_depth = d, criterion = 'entropy')

            # fit data to model and predict
            model.fit(x_train, y_train)
            y_predict = model.predict(x_test)

            # display accuracy
            acc = accuracy_score(y_test, y_predict)
            #print(acc)
            if acc > best_combination['accuracy']:
                best_combination['n'] = n
                best_combination['d'] = d
                best_combination['accuracy'] = acc
                best_combination['error rate'] = 1 - acc
                best_combination['y_predict'] = y_predict
    
    print(best_combination['accuracy'])
    print(best_combination['n'])
    print(best_combination['d'])    


    # compute confusion matrix, then plot corresponding heatmap
    # mat = confusion_matrix(y_test, y_predict)
    # sns.heatmap(mat.T, square=True, annot=True, fmt = 'd', cbar=True, 
    #             xticklabels=['abnormal', 'normal'], yticklabels=['abnormal', 'normal'])
    # plt.xlabel('true label')
    # plt.ylabel('predicted label')

    # display heatmap
    #plt.show()

randomForest()
