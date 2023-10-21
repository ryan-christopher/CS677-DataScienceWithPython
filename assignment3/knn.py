'''
Ryan Christopher
Class: CS 677
Date: 10/20/2023
Assignment 3 Questions 3 and 4

=======Description of Problem=======
Taking the train and test data from the original 50/50 split, use k-NN
for the values k = 3, 5, 7, 9, 11 to determine the best k value for 
accuracy. Then, use feature selection to determine the most and 
least impactful features for accuracy.
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# load train and test data from original split
train_data = pd.read_csv('assignment3/banknote_data/train.csv')
test_data = pd.read_csv('assignment3/banknote_data/test.csv')


# calcBestKStats takes the predicted y values and the true y values for
# the optimal value of K and calculates the TP, TN, FP, FN, TPR, and TNR
# of the prediction
def calcBestKStats(prediction, test):
    # set test to be dataframe
    test = pd.DataFrame(test)

    # add k predictions as column
    test['k'] = prediction.tolist()

    # after column of k predictions added to dataframe, determine stats
    # for TP, FP, TN, FN, Accuracy, TPR, and TNR
    tp = len(test.where((test['Class'] == 0.0) & (test['k'] == test['Class'])).dropna())
    fp = len(test.where((test['Class'] == 0.0) & (test['k'] != test['Class'])).dropna())
    tn = len(test.where((test['Class'] == 1.0) & (test['k'] == test['Class'])).dropna())
    fn = len(test.where((test['Class'] == 1.0) & (test['k'] != test['Class'])).dropna())
    acc = len(test.where(test['k'] == test['Class']).dropna()) / len(test)
    # print('TP:', tp, 'FP:', fp)
    # print('TN:', tn, 'FN:', fn)
    # print('Accuracy:', acc)
    # print('TPR', tp / (tp + fn))
    # print('TNR', tn / (tn + fp))


# knn takes the train and test data as parameters, applies the standard scaler,
# and calculates the accuracy of k for the list of k values
def knn(train, test):
    # gather train/test x and y values from split data sets
    x_train = train.iloc[:, 0:4]
    y_train = train['Class']
    x_test = test.iloc[:, 0:4]
    y_test = test['Class']

    # scale values using StandardScaler
    standardScaler = StandardScaler()
    x_train_scaled = standardScaler.fit_transform(x_train)
    x_test_scaled = standardScaler.fit_transform(x_test)

    # create list to store accuracies for each k value
    k_accuracies = []

    # create list of k values to iterate over
    k_vals = [3,5,7,9,11]

    for k in k_vals:
        # apply knn classifier for each value of k = 3, 5, 7, 9, 11
        classifier = KNeighborsClassifier(n_neighbors=k)

        # fit classifier to x training data
        classifier.fit(x_train_scaled, y_train)

        # predict test values using classifier fit to train values
        y_predict = classifier.predict(x_test_scaled)

        if k == 5:
            # call calcBestKStats when k = 5 to generate  
            # performance measures
            calcBestKStats(y_predict, y_test)

            # predict bill x containing the last 4 digits of my BUID
            buid_predict = classifier.predict([[0.3360, 0.3360, 0.3360, 0.3360]])
            print(buid_predict)

        # append the accuracy to k_accuracies list
        k_accuracies.append(accuracy_score(y_test, y_predict))

    # display list of accuracies for k
    # print(k_accuracies)

    # create plot of accuracies vs k values
    # kplot = plt.axes()
    # kplot.set_xticks(k_vals)
    # plt.plot(k_vals, k_accuracies)
    # plt.xlabel('k')
    # plt.ylabel('Accuracy')
    # plt.title('Accuracy vs k')
    # plt.show()

# knn takes the train and test data as parameters, applies the standard scaler,
# and calculates the accuracy for each mising feature
def knnFeatureSelect(train, test, k):
    # gather train/test x and y values from split data sets
    x_train = train.iloc[:, 0:4]
    y_train = train['Class']
    x_test = test.iloc[:, 0:4]
    y_test = test['Class']

    # create list to store accuracies with each missing feature
    feature_accuracies = []

    # iterate through features
    for feature in ['Variance', 'Skewness', 'Curtosis', 'Entropy']:

        x_train_feature = x_train.drop(feature, axis = 1)
        x_test_feature = x_test.drop(feature, axis = 1)

        # scale values using StandardScaler
        standardScaler = StandardScaler()
        x_train_scaled = standardScaler.fit_transform(x_train_feature)
        x_test_scaled = standardScaler.fit_transform(x_test_feature)

        # apply knn classifier for each value of k = 3, 5, 7, 9, 11
        classifier = KNeighborsClassifier(n_neighbors=k)

        # fit classifier to x training data
        classifier.fit(x_train_scaled, y_train)

        # predict test values using classifier fit to train values
        y_predict = classifier.predict(x_test_scaled)

        # append the accuracy to feature_accuracies list
        feature_accuracies.append(["Misssing feature:", feature, 
                                   "Accuracy:", accuracy_score(y_test, y_predict)])

    # display list of accuracies missing each feature
    for feature in feature_accuracies:
        print(feature)


#knn(train_data, test_data)
#knnFeatureSelect(train_data, test_data, 5)