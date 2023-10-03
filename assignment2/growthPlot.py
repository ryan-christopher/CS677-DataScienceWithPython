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
import matplotlib
from predict import predictLabels
from true_label import getTable

cost_stock_data = getTable('COST')
spy_stock_data = getTable('SPY')

def generatePlot(df, stats):

    # find best W value
    bestW = 0
    bestWaccuracy = 0
    for key, value in stats.items():
        if (key[0] == 'w') and (float(value['Accuracy']) > bestWaccuracy):
            bestW = key[-1]
            bestWaccuracy = float(value['Accuracy'])
    #print(bestW)
    #print(bestWaccuracy)
    returns = df['Return'].tolist()
    bestWlabels = df['w=' + bestW].tolist()
    ensembleLables = df['Ensemble'].tolist()

    ensembleReturn = 100
    ensembleReturnList = []
    for i in range(len(returns)):
        ensembleReturnList.append(ensembleReturn)
        ensembleReturn *= (1 + returns[i])

    print(ensembleReturn)

    #amount *= (1 + daily_return)
    return
    

data, stats = predictLabels(spy_stock_data, 4)
generatePlot(data, stats)
print(data)

