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

print(predictLabels(cost_stock_data, 4))

