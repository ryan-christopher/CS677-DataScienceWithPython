'''
Ryan Christopher
Class: CS 677
Date: 9/16/2023
Assignment 1 Question 3

=======Description of Problem=======
Taking the information of daily stock values for the years 2016-2020,
these functions generate the means and standard deviations for each 
day of the week for all 5 years for both my stock and SPY.
'''
from generate_yearly_stats import standard_deviation

# generate_stats compiles the info displayed in the tables of Question 1. 
# It takes as input the list of lines containing the daily stock info
# created by read_stock_data_from_file.py 
def generate_all_stats(cost, spy):
    # create initial values for key value pairs of years and days
    totals = {}
    stocks = ['COST', 'SPY']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # iterate through years to create year : day key value pair 
    # for all weekdays for each year
    for stock in stocks:
        totals[stock] = {}
        # for each day of each year, store a dictionary that stores the
        # return values for all returns, strictly negative returns, and 
        # strictly non-negative returns as well as their corresponding sums
        for day in days:
            totals[stock][day] = {'ret_vals' : [], 'ret_sum' : 0,
                                'n_ret_vals' : [], 'n_ret_sum' : 0 ,
                                'p_ret_vals' : [], 'p_ret_sum' : 0 }
    
    # iterate through lines of daily stock info
    for line in cost[1:]:
        line = line.split(',')    
        
        # store values for day of the week, year, and the return for the day
        day, daily_return = line[4], float(line[13])
        
        # add current day info to list and sum of all values
        totals['COST'][day]['ret_vals'].append(daily_return)
        totals['COST'][day]['ret_sum'] += daily_return
        
        # add current day info to list and sum of negative values
        if daily_return < 0 :
            totals['COST'][day]['n_ret_vals'].append(daily_return)
            totals['COST'][day]['n_ret_sum'] += daily_return
        
        # add current day info to list and sum of non-negative values
        elif daily_return > 0 :
            totals['COST'][day]['p_ret_vals'].append(daily_return)
            totals['COST'][day]['p_ret_sum'] += daily_return

    # iterate through lines of daily stock info
    for line in spy[1:]:
        line = line.split(',')    
        
        # store values for day of the week, year, and the return for the day
        day, daily_return = line[4], float(line[13])
        
        # add current day info to list and sum of all values
        totals['SPY'][day]['ret_vals'].append(daily_return)
        totals['SPY'][day]['ret_sum'] += daily_return
        
        # add current day info to list and sum of negative values
        if daily_return < 0 :
            totals['SPY'][day]['n_ret_vals'].append(daily_return)
            totals['SPY'][day]['n_ret_sum'] += daily_return
        
        # add current day info to list and sum of non-negative values
        elif daily_return > 0 :
            totals['SPY'][day]['p_ret_vals'].append(daily_return)
            totals['SPY'][day]['p_ret_sum'] += daily_return


    # table format: mean, sd, neg returns, mean, sd, pos returns, mean, sd
    print('Mean, SD, Neg Vals, Neg Mean, Neg SD, Pos Vals, Pos Mean, Pos SD')

    # iterate through years to calculate stats for each day of the week      
    for stock in totals:
        print(stock, ':')
        # iterate through days and use the corresponding lists of values and
        # sums to calculate means and standard deviations 
        for day in totals[stock]:
            # mean and standard deviation for all values
            s = len(totals[stock][day]['ret_vals'])
            mean = totals[stock][day]['ret_sum'] / s
            sd = standard_deviation(totals[stock][day]['ret_vals'], mean)

            # mean and standard deviation for negative values
            ns = len(totals[stock][day]['n_ret_vals'])
            nmean = totals[stock][day]['n_ret_sum'] / ns
            n_sd = standard_deviation(totals[stock][day]['n_ret_vals'], mean)

            # mean and standard deviation for non-negative positive values
            ps = len(totals[stock][day]['p_ret_vals'])
            pmean = totals[stock][day]['p_ret_sum'] / ps
            p_sd = standard_deviation(totals[stock][day]['p_ret_vals'], mean)

            # for presenting in table only, multiply averages and standard deviations 
            # by 100 in order to display them as a percentage value and round to four 
            # decimal places
            # FOR UNROUNDED VALUES: comment out the three lines below
            mean, sd = round(mean * 100, 3), round(sd * 100, 3)
            nmean, n_sd = round(nmean * 100, 3), round(n_sd * 100, 3)
            pmean, p_sd = round(pmean * 100, 3), round(p_sd * 100, 3)
            

            print(day, ' : ', mean, sd, ns, nmean, n_sd, ps, pmean, p_sd)