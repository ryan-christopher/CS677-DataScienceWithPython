# -*- coding: utf-8 -*-
'''
Ryan Christopher
Class: CS 677
Date: 9/9/2023
Homework Problem 1
Description of Problem:
'''
import os
import math

ticker='COST'
input_dir = r'/Users/ryan/Desktop/school/cs677/assignments/week_1_homework/'
ticker_file = os.path.join(input_dir, ticker + '.csv')

def standard_deviation(vals, mean):
    sd, n = 0, len(vals)
    for val in vals:
        sd += (val**2)
    return math.sqrt(((sd / n) - (mean**2)))

try:   
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)

    'Problem 1'

    totals = {}
    years = ['2016', '2017', '2018', '2019', '2020']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for year in years:
        totals[year] = {}
        for day in days:
            totals[year][day] = {'ret_vals' : [], 'ret_sum' : 0,
                                'n_ret_vals' : [], 'n_ret_sum' : 0 ,
                                'p_ret_vals' : [], 'p_ret_sum' : 0 }
    
    for line in lines[1:]:
        line = line.split(',')
        day, year, daily_return = line[4], line[1], float(line[13])
        totals[year][day]['ret_vals'].append(daily_return)
        totals[year][day]['ret_sum'] += daily_return
        if daily_return < 0 :
            totals[year][day]['n_ret_vals'].append(daily_return)
            totals[year][day]['n_ret_sum'] += daily_return
        elif daily_return > 0 :
            totals[year][day]['p_ret_vals'].append(daily_return)
            totals[year][day]['p_ret_sum'] += daily_return
            
    for year in totals:
        print(year, ':')
        for day in totals[year]:
            # mean and standard deviation for all values
            s = len(totals[year][day]['ret_vals'])
            mean = totals[year][day]['ret_sum'] / s
            sd = standard_deviation(totals[year][day]['ret_vals'], mean)

            # mean and standard deviation for negative values
            ns = len(totals[year][day]['n_ret_vals'])
            nmean = totals[year][day]['n_ret_sum'] / ns
            n_sd = standard_deviation(totals[year][day]['n_ret_vals'], mean)

            # mean and standard deviation for positive values
            ps = len(totals[year][day]['p_ret_vals'])
            pmean = totals[year][day]['p_ret_sum'] / ps
            p_sd = standard_deviation(totals[year][day]['p_ret_vals'], mean)

            print('---', day, '---')
            #table format: mean, sd, neg returns, mean, sd, pos returns, mean, sd
            print('Mean, SD, Neg Vals, Neg Mean, Neg SD, Pos Vals, Pos Mean, Pos SD')
            print(mean, sd, ns, nmean, n_sd, ps, pmean, p_sd, '\n')

 
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)