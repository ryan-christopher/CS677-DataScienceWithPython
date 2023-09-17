'''
Ryan Christopher
Class: CS 677
Date: 9/16/2023
Assignment 1 Questions 4 and 5

=======Description of Problem=======
This file includes the oracle telling us which days to invest
on, as well as the buy and hold method.
'''

def oracle(stock):
    amount = 100
    # iterate through lines of daily stock info
    for line in stock[1:]:
        line = line.split(',')    
        # store values for day of the week, year, and the return for the day
        daily_return = float(line[13])

        # follow the oracles advice and only invest on days with positive returns
        if daily_return > 0:
            amount *= (1 + daily_return)

    print("Oracle's advice followed:", amount)
    return amount

def buy_and_hold(stock):
    amount = 100
    # iterate through lines of daily stock info
    for line in stock[1:]:
        line = line.split(',')    
        # store values for day of the week, year, and the return for the day
        daily_return = float(line[13])
        # regardless of value, change amount's value to include
        # the price change for each day
        amount *= (1 + daily_return)
    print('Buy and hold:', amount)
    return