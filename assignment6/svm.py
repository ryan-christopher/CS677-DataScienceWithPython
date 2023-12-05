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
from sklearn.svm import LinearSVC 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

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

def linearSVM(seeds):

    train, test = train_test_split(seeds, test_size = 0.5, 
                                       train_size = 0.5, random_state = 13)

    X = train.iloc[:,0:7]
    y = train.iloc[:,7:8]

    c = 100 # for margin
    linear_svm = LinearSVC(C=c,loss="hinge", max_iter = 5000)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    linear_svm.fit(X_scaled, y)
    y.describe

    x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
    y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
    Z = linear_svm.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(figsize=(16,12))
    plt.contourf(xx, yy, Z, cmap='RdBu')

    # Separate observations that are occupied or not for plotting
    X_occ = X_scaled[[i for i in range(len(y)) if y[i] == 1],:]
    X_not_occ = X_scaled[[i for i in range(len(y)) if y[i] == 0],:]

    # Make scatterplots
    not_occ = plt.scatter(X_not_occ[:,0], X_not_occ[:,1], marker='o', color='r')
    yes_occ = plt.scatter(X_occ[:,0], X_occ[:,1], marker='^', color='b')

    # Find paramters to make margins
    w = linear_svm.coef_[0]
    b = linear_svm.intercept_[0]
    x_points = np.linspace(x_min, x_max)
    y_points = -(w[0] / w[1]) * x_points - b / w[1]

    # Getting margin
    w_hat = linear_svm.coef_[0] / (np.sqrt(np.sum(linear_svm.coef_[0] ** 2))) # normal vector to decision boundary
    margin = 1 / np.sqrt(np.sum(linear_svm.coef_[0] ** 2))

    boundary_points = np.array(list(zip(x_points, y_points)))
    above = boundary_points + w_hat * margin
    below = boundary_points - w_hat * margin

    # Above margin
    plt.plot(above[:, 0],
            above[:, 1],
            'k--',
            linewidth=2)

    # Below margin
    plt.plot(below[:, 0],
            below[:, 1],
            'k--',
            linewidth=2)

    # Make legend
    plt.legend((not_occ,yes_occ),
            ('Not Occupied', 'Occupied'),
            title='True Labels',
            scatterpoints=1,
            loc='lower right',
            ncol=1,
            fontsize=8)
    plt.xlabel("CO2 z-score")
    plt.ylabel("HumidityRatio z-score")
    plt.title("Linear SVM Decision Boundary for Two Features (C = %i)" % (c))
    plt.xlim([x_min,x_max])
    plt.ylim([y_min,y_max])
    plt.show()


print(linearSVM(seeds))