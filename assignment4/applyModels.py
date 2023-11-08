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

# chosen x feature and y feature
# Group 3: X = serum sodium, Y = serum creatinine 

# create df of x and y for surviving patients (class 0)
class_0 = class_0[['serum_sodium', 'serum_creatinine']]

# create df of x and y for deceased patients (class 1)
class_1 = class_1[['serum_sodium', 'serum_creatinine']]

# applyModel takes a class number and regression model as parameters,
# separates the data by class number and feature, then fits and 
# predicts 
def applyModel(class_num, reg_model):

    # take 50/50 split of class chosen from parameter
    if class_num == 0:
        train, test = train_test_split(class_0, test_size = 0.5, 
                                       train_size = 0.5, random_state = 13)
    else:
        train, test = train_test_split(class_1, test_size = 0.5, 
                                       train_size = 0.5, random_state = 13)


    # sort values for plotting
    test = pd.DataFrame(test).sort_values('serum_sodium')
    train = pd.DataFrame(train).sort_values('serum_sodium')


    # extract columns for x and y, assign to train and test groups
    x_train = train.iloc[:, 0:1]
    y_train = train['serum_creatinine']
    x_test = test.iloc[:, 0:1]
    y_test = test['serum_creatinine']


    # instantiate LinearRegression
    linreg = LinearRegression()


    # fit the model from parameter with X_train and 
    # compute predicted y values
    if reg_model == "Simple Linear Regression":
        linreg.fit(x_train, y_train)
        y_predict = linreg.predict(x_test)

    elif reg_model == "Quadratic":
        poly = PolynomialFeatures(2, include_bias = False)
        x_train_quad = poly.fit_transform(x_train)
        linreg.fit(x_train_quad, y_train)        
        x_test_quad = poly.fit_transform(x_test)
        y_predict = linreg.predict(x_test_quad)

    elif reg_model == "Cubic Spline":
        poly = PolynomialFeatures(3, include_bias = False)
        x_train_quad = poly.fit_transform(x_train)
        linreg.fit(x_train_quad, y_train)
        x_test_quad = poly.fit_transform(x_test)
        y_predict = linreg.predict(x_test_quad)

    elif reg_model == "GLM":
        linreg.fit(np.log(x_train), y_train)
        y_predict = linreg.predict(np.log(x_test))

    elif reg_model == "Log(y) GLM":
        linreg.fit(np.log(x_train), np.log(y_train))
        y_predict = linreg.predict(np.log(x_test))


    print(reg_model)
    print("Class", str(class_num))
    print("===============")


    # print weights 
    print("Weights:")
    print(linreg.coef_)
    print("Intercept:", linreg.intercept_)


    # initialize figure and add title
    fig = plt.figure()
    fig.suptitle(reg_model + " - Class " + str(class_num), fontsize=14)

    
    # plot actual and predicted values
    if reg_model in ['Simple Linear Regression', 'Quadratic', 'Cubic Spline', 'GLM']:
        plt.plot(x_test['serum_sodium'].tolist(), y_test.tolist(),
                 "b.", label = "Actual Values")
        plt.plot(x_test['serum_sodium'].tolist(), y_predict.tolist(),
                 "r-", label = "Predicted Values")
    
    elif reg_model in ['Log(y) GLM']:
        plt.plot(np.log(x_test['serum_sodium'].tolist()), np.log(y_test.tolist()),
                 "b.", label = "Actual Values")
        plt.plot(np.log(x_test['serum_sodium'].tolist()), y_predict.tolist(),
                 "r-", label = "Predicted Values")


    # assign x and y labels to Days and Return, add legend, and display plot
    plt.xlabel("Serum Sodium")
    plt.ylabel("Serum Creatinine")
    plt.legend()
    plt.show()


    # compute residuals (y - test_y)
    if reg_model in ['Simple Linear Regression', 'Quadratic', 'Cubic Spline', 'GLM']:
        residuals = y_test - y_predict

    elif reg_model in ['Log(y) GLM']:
        residuals = y_test - np.exp(y_predict)


    # use residuals to calculate SSE
    sse = (residuals**2).sum()
    print("SSE")
    print(sse, '\n\n')

# for each model, call applyModel on both surviving and deceased classes
for model in ['Simple Linear Regression', 'Quadratic', 'Cubic Spline', 'GLM', 'Log(y) GLM']:
    applyModel(0, model)
    applyModel(1, model)