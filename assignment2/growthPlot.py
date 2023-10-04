'''
Ryan Christopher
Class: CS 677
Date: 10/3/2023
Assignment 2 Question 5

=======Description of Problem=======
Plot the growth of the amount for years 4 and 5 if I trade based on best W 
prediction and on the ensemble prediction where I start with $100. Additionally,
plot the growth of my portfolio if I used a buy and hold strategy. 
'''
import matplotlib.pyplot as plt
from predict import predictLabels
from true_label import getTable

cost_stock_data = getTable('COST')
spy_stock_data = getTable('SPY')

# generatePlot gathers the list of predictions and calculates the return if the
# best W prediction was followed, the ensemble prediction was followed, and if 
# a buy and hold strategy was used. Then, it graphs the three return values 
# over the period of years 4 and 5 for the given stock.
def generatePlot(df, stats, name):
    # set initial w value to 0
    bestW = 0
    bestWaccuracy = 0

    # find best W value by iterating through stats dictionary
    for key, value in stats.items():
        # reassign bestW if current accuracy is larger than bestW
        if (key[0] == 'w') and (float(value['Accuracy']) > bestWaccuracy):
            bestW = key[-1]
            bestWaccuracy = float(value['Accuracy'])

    # generate lists of return values, best W predictions, 
    # and ensemble predictions
    returns = df['Return'].tolist()
    bestWlabels = df['w=' + bestW].tolist()
    ensembleLables = df['Ensemble'].tolist()

    # set initial return value and empty list for w, ensemble, 
    # and Buy and Hold Strategy
    wReturn, ensembleReturn, holdReturn = 100, 100, 100
    wReturnList, ensembleReturnList, holdReturnList = [], [], []

    # iterate through list of returns
    for i in range(len(returns)):

        # append current return value to each of the
        # three strategies 
        wReturnList.append(wReturn)
        ensembleReturnList.append(ensembleReturn)
        holdReturnList.append(holdReturn)

        # if predicted value for ensemble or w is positive, change
        # the return variable by the return value of current day
        if (ensembleLables[i-1] == "+"):
            ensembleReturn *= (1 + returns[i])
        if (bestWlabels[i-1] == "+"):
            wReturn *= (1 + returns[i])

        # change buy and hold return amount by return of given day
        holdReturn *= (1 + returns[i])

    # initialize figure
    fig = plt.figure()

    # add title
    fig.suptitle(name + " Portfolio Growth", fontsize=14)

    # plot lists of data along and add corresponding labels
    plt.plot(ensembleReturnList, label = "Ensemble Prediction")
    plt.plot(wReturnList, label = "Best W Prediction")
    plt.plot(holdReturnList, label = "Buy and Hold")

    # assign x and y labels to Days and Return
    plt.xlabel("Days")
    plt.ylabel("Return")

    # display legend and show plot
    plt.legend()
    plt.show()

data, stats = predictLabels(cost_stock_data, 4)
generatePlot(data, stats, "COST")