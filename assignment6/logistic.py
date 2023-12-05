'''
Ryan Christopher
Class: CS 677
Date: 12/1/2023
Assignment 6 Question 2

=======Description of Problem=======
Taking the logitstic regression classifier to the dataset, compute the accuracy and generate
the confusion matrix. Then, compare it to the three SVMs from the prior 
question.
'''
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import seaborn as sns
from svm import loadData
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

seeds = loadData()

# logReg takes the training and testing data as parameters, and uses 
# the logistic regression classifier on the training data to 
# predict the test data class
def logReg(seeds):
    train, test = train_test_split(seeds, test_size = 0.5, 
                                       train_size = 0.5, random_state = 13)
    # gather train/test x and y values from split data sets
    x_train = train.iloc[:, 0:7]
    y_train = train['Class']
    x_test = test.iloc[:, 0:7]
    y_test = test['Class']

    # initialize logisticregression method
    log_reg = LogisticRegression()
    # fit to training data
    log_reg.fit(x_train,y_train)
    # predict y values
    y_predict = log_reg.predict(x_test)

    # display accuracy
    print(accuracy_score(y_test, y_predict))

    # compute confusion matrix, then plot corresponding heatmap
    mat = confusion_matrix(y_test, y_predict)
    sns.heatmap(mat.T, square=True, annot=True, fmt = 'd', cbar=True, 
                xticklabels=["L = 1", "L = 2"], yticklabels=["L = 1", "L = 2"])
    plt.xlabel('true label')
    plt.ylabel('predicted label')
    plt.suptitle("logistic")

    # display heatmap
    plt.show()

logReg(seeds)