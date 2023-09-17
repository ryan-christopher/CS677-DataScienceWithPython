'''
Ryan Christopher
Class: CS 677
Date: 9/16/2023
Assignment 1 Question 6

=======Description of Problem=======
This file includes the upset oracle, where the oracle
will give wrong information for the best 10 days, the worst 10 days,
and swapping the 5 best days for the 5 worst days.
I wanted to name this file episode_III_revenge_of_the_oracle however
that seemed excessive.
'''

# wrong_best_ten takes the stock data as input, and calculates the profit
# from $100 dollars invested and following the oracle's advice, however
# the best 10 days will not be included
def wrong_best_ten(stock):
    amount = 100
    ret_amounts = []

    # iterate through lines of daily stock info
    for line in stock[1:]:
        line = line.split(',')    
        # store values for day of the week, year, and the return for the day
        daily_return = float(line[13])

        #store positive returns
        if daily_return > 0:
            ret_amounts.append(daily_return)

    # sort the positive return values in descending order, then omit the first 10
    ret_amounts.sort(reverse=True)
    ret_amounts = ret_amounts[10:]

    # calculate profit
    for ret in ret_amounts:
        amount *= (1 + ret)

    print(amount)
    return amount

# wrong_worst_ten takes the stock data as input, and calculates the profit
# from $100 dollars invested and following the oracle's advice, however
# the worst 10 days will also be included 
def wrong_worst_ten(stock):
    amount = 100
    pos_ret_amounts = []
    neg_ret_amounts = []

    # iterate through lines of daily stock info
    for line in stock[1:]:
        line = line.split(',')    
        # store values for day of the week, year, and the return for the day
        daily_return = float(line[13])

        # store positive returns
        if daily_return > 0:
            pos_ret_amounts.append(daily_return)

        # store negative returns 
        elif daily_return < 0:
            neg_ret_amounts.append(daily_return)

    # sort the negative return values in ascending order, and get the lowest 10
    neg_ret_amounts.sort(reverse=False)
    neg_ret_amounts = neg_ret_amounts[:10]

    # combine the lists to now calculate returns including the 10 worst days
    ret_amounts = pos_ret_amounts + neg_ret_amounts

    # calculate profit
    for ret in ret_amounts:
        amount *= (1 + ret)

    print(amount)
    return amount

# wrong_best_and_worst_five takes the stock data as input, and calculates the profit
# from $100 dollars invested and following the oracle's advice, however
# the worst 5 days will be included and the best 5 days will not be included
def wrong_best_and_worst_five(stock):
    amount = 100
    pos_ret_amounts = []
    neg_ret_amounts = []

    # iterate through lines of daily stock info
    for line in stock[1:]:
        line = line.split(',')    
        # store values for day of the week, year, and the return for the day
        daily_return = float(line[13])

        # store positive returns
        if daily_return > 0:
            pos_ret_amounts.append(daily_return)

        # store negative returns 
        elif daily_return < 0:
            neg_ret_amounts.append(daily_return)
    
    # sort the positive return values in descending order, then omit the first 5
    pos_ret_amounts.sort(reverse = True)
    pos_ret_amounts = pos_ret_amounts[5:]

    # sort the negative return values in ascending order, and get the lowest 5
    neg_ret_amounts.sort(reverse = False)
    neg_ret_amounts = neg_ret_amounts[:5]

    # combine the lists to now calculate returns excluding the 5 best days and 
    # including the 5 worst days
    ret_amounts = pos_ret_amounts + neg_ret_amounts

    # calculate profit
    for ret in ret_amounts:
        amount *= (1 + ret)

    print(amount)
    return amount
