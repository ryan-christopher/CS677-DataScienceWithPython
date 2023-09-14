# -*- coding: utf-8 -*-
'''
Ryan Christopher
Class: CS 677
Date: 9/9/2023
Assignment 1 Starter File

=======Description of Problem=======
This file outputs the results from generate_stats.py 
and oracle.py.
'''
import os
from generate_stats import generate_stats

ticker='COST'
input_dir = r'/Users/ryan/Desktop/school/cs677/assignments/week_1_homework/stock_data'
ticker_file = os.path.join(input_dir, ticker + '.csv')

try:   
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)

    generate_stats(lines)
    
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)