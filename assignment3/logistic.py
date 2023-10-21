'''
Ryan Christopher
Class: CS 677
Date: 10/21/2023
Assignment 3 Questions 5 and 6

=======Description of Problem=======
Taking the train and test data from the original 50/50 split, use the
logistic regression classifier and compute the accuracy for the test 
dataset. Then, use feature selection to determine the most and 
least impactful features for accuracy.
'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# load train and test data from original split
train_data = pd.read_csv('assignment3/banknote_data/train.csv')
test_data = pd.read_csv('assignment3/banknote_data/test.csv')


# calcLogStats takes the predicted y values and the true y values for
# the logistic regression prediction and calculates the 
# TP, TN, FP, FN, TPR, and TNR of the prediction
def calcLogStats(prediction, test):
    # set test to be dataframe
    test = pd.DataFrame(test)

    # add k predictions as column
    test['log'] = prediction.tolist()

    # after column of k predictions added to dataframe, determine stats
    # for TP, FP, TN, FN, Accuracy, TPR, and TNR
    tp = len(test.where((test['Class'] == 0.0) & (test['log'] == test['Class'])).dropna())
    fp = len(test.where((test['Class'] == 0.0) & (test['log'] != test['Class'])).dropna())
    tn = len(test.where((test['Class'] == 1.0) & (test['log'] == test['Class'])).dropna())
    fn = len(test.where((test['Class'] == 1.0) & (test['log'] != test['Class'])).dropna())
    acc = len(test.where(test['log'] == test['Class']).dropna()) / len(test)
    print('TP:', tp, 'FP:', fp)
    print('TN:', tn, 'FN:', fn)
    print('Accuracy:', acc)
    print('TPR', tp / (tp + fn))
    print('TNR', tn / (tn + fp))


# logReg takes the training and testing data as parameters, and uses 
# the logistic regression classifier on the training data to 
# predict the test data class
def logReg(train, test):
    # gather train/test x and y values from split data sets
    x_train = train.iloc[:, 0:4]
    y_train = train['Class']
    x_test = test.iloc[:, 0:4]
    y_test = test['Class']

    # initialize logisticregression method
    log_reg = LogisticRegression()

    # fit to training data
    log_reg.fit(x_train,y_train)

    # predict using test data
    print(x_test)
    y_predict = log_reg.predict(x_test)
    
    # create dataframe as entry for bill x with my BUID numbers
    buid = pd.DataFrame({'Variance' : [3], 'Skewness' : [3], 
                         'Curtosis' : [6], 'Entropy' : [0]})
    
    # display prediction from bill x
    print(log_reg.predict(buid))

    # display accuracy
    print(accuracy_score(y_test, y_predict))

    calcLogStats(y_predict, y_test)

# logRegFeatureSelect takes the training and testing data as parameters, and uses 
# the logistic regression classifier on the training data to predict the 
# test data class with each missing feature
def logRegFeatureSelect(train, test):
    # gather train/test x and y values from split data sets
    x_train = train.iloc[:, 0:4]
    y_train = train['Class']
    x_test = test.iloc[:, 0:4]
    y_test = test['Class']

    # create list to store accuracies with each missing feature
    feature_accuracies = []

    # iterate through features
    for feature in ['Variance', 'Skewness', 'Curtosis', 'Entropy']:
        # remove feature from dataframe
        x_train_feature = x_train.drop(feature, axis = 1)
        x_test_feature = x_test.drop(feature, axis = 1)

        # initialize logisticregression method
        log_reg = LogisticRegression()

        # fit to training data
        log_reg.fit(x_train_feature,y_train)

        # predict using test data
        y_predict = log_reg.predict(x_test_feature)

        # append the accuracy to feature_accuracies list
        feature_accuracies.append(["Misssing feature:", feature, 
                                   "Accuracy:", accuracy_score(y_test, y_predict)])
    
    # display list of accuracies missing each feature
    for feature in feature_accuracies:
        print(feature)


#logReg(train_data, test_data)
#logRegFeatureSelect(train_data, test_data)