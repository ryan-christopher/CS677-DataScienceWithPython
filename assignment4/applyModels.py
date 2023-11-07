'''
Ryan Christopher
Class: CS 677
Date: 11/1/2023 🦃
Assignment 4 Question 2

=======Description of Problem=======
Taking the facilitator group chosen, look for the best model that best explains 
the relationship for surviving and deceased patients. For each model, fit the 
data, compute the predicted values, plot the predicted vs actual values, and
compute the corresponding loss function. 
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from createPlots import getHeartData
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


# get data
class_0, class_1 = getHeartData()


# choose one x feature and one y feature
# Group 3 - X = serum sodium   Y = serum creatinine 

# create df of x and y for surviving patients (class 0)
class_0 = class_0[['serum_sodium', 'serum_creatinine']]

# create df of x and y for deceased patients (class 1)
class_1 = class_1[['serum_sodium', 'serum_creatinine']]

def applyModel(class_num, reg_type):
    # ===== Class 0 =====
    # take 50/50 split 
    if class_num == 0:
        train, test = train_test_split(class_0, test_size = 0.5, train_size = 0.5, random_state = 13)
    else:
        train, test = train_test_split(class_1, test_size = 0.5, train_size = 0.5, random_state = 13)
    test = pd.DataFrame(test)
    train = pd.DataFrame(train)

    # extract columns for x and y, assign to train and test groups
    x_train = train.iloc[:, 0:1]
    y_train = train['serum_creatinine']
    x_test = test.iloc[:, 0:1]
    y_test = test['serum_creatinine']

    # instantiate LinearRegression
    linreg = LinearRegression()

    # fit the model with X_train and compute predicted y values
    if reg_type == "Simple Linear Regression":
        linreg.fit(x_train, y_train)
        y_predict = linreg.predict(x_test)

    elif reg_type == "Quadratic":
        poly = PolynomialFeatures(2, include_bias = False)
        x_train_quad = poly.fit_transform(x_train)
        linreg.fit(x_train_quad, y_train)
        x_test_quad = poly.fit_transform(x_test)
        y_predict = linreg.predict(x_test_quad)

    elif reg_type == "Cubic Spline":
        poly = PolynomialFeatures(3, include_bias = False)
        x_train_quad = poly.fit_transform(x_train)
        linreg.fit(x_train_quad, y_train)
        x_test_quad = poly.fit_transform(x_test)
        y_predict = linreg.predict(x_test_quad)

    elif reg_type == "GLM":
        
        linreg.fit(np.log(x_train), y_train)
        y_predict = linreg.predict(x_test)

    elif reg_type == "Log(y) GLM":
        return

    # print weights 
    print("===== Weights =====")
    print(linreg.coef_)

    # plot (if possible) predicted and actual values in x_test

    # initialize figure
    fig = plt.figure()
    # add title
    fig.suptitle(reg_type, fontsize=14)
    plt.plot(x_test['serum_sodium'].tolist(), y_test.tolist(), "b.", label = "Actual Values")
    plt.plot(x_test['serum_sodium'].tolist(), y_predict.tolist(), "r", label = "Predicted Values")

    # assign x and y labels to Days and Return
    plt.xlabel("Serum Sodium")
    plt.ylabel("Serum Creatinine")

    plt.legend()
    plt.show()

    # compute residuals (y - test_y)
    residuals = y_predict - y_test

    # estimate loss function (SSE sum of the squared of residuals)
    sse = (residuals**2).sum()
    print("===== SSE =====")
    print(sse)


applyModel(0, "GLM")