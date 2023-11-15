'''
Week 11 In class programming exercise
'''
# Goal - train an SVM for data that classifies whether 
# a room is occupied or not based on temperature, humidity,
# light, CO2, and humidity ratio
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC # support vector classification
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt


def isOccupied():

    test = pd.read_csv('week11_inclass/Occupancy Test Set.csv')
    train = pd.read_csv('week11_inclass/Occupancy Training Set.csv')
    
    # use only C02 and Humidity Ratio features
    X = train.iloc[:,5:7]

    # class occupied/not occupied
    y = test['Occupancy']
    print(X)
    print(y)

    # for margin
    c = 100
    
    # instantiate linearSVC
    linear_svm = LinearSVC(C=c,loss="hinge")

    # scale x values
    X_scaled = StandardScaler().fit_transform(X)

    # Fit model to data
    linear_svm.fit(X_scaled, y)

    # Plot the decision boundary, use a meshgrid
    x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
    y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
    Z = linear_svm.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(figsize=(8,6))
    plt.contourf(xx, yy, Z, cmap='RdBu')

    # Separate observations that are iris and are not for plotting
    X_occupied = X_scaled[[i for i in range(len(y)) if y[i] == 1],:]
    X_not_occupied = X_scaled[[i for i in range(len(y)) if y[i] == 0],:]

    # Make scatterplots
    not_iris = plt.scatter(X_not_occupied[:,0], X_not_occupied[:,1], marker='o', color='r')
    yes_iris = plt.scatter(X_occupied[:,0], X_occupied[:,1], marker='^', color='b')

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
    plt.legend((not_iris,yes_iris),
            ('Not Occupied', 'Occupied'),
            title='True Labels',
            scatterpoints=1,
            loc='lower right',
            ncol=1,
            fontsize=8)
    plt.xlabel("CO2 z-score")
    plt.ylabel("Humidity Ratio z-score")
    plt.title("Linear SVM Decision Boundary for Two Features (C = %i)" % (c))
    plt.xlim([x_min,x_max])
    plt.ylim([y_min,y_max])
    plt.show()


isOccupied()