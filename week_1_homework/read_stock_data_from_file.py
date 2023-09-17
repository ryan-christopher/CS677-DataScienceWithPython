# -*- coding: utf-8 -*-
'''
Ryan Christopher
Class: CS 677
Date: 9/16/2023
Assignment 1 Starter File

=======Description of Problem=======
This file outputs the results from generate_yearly_stats.py,   
generate_all_stats.py, oracle.py, avg_up_and_down.py, and
oracle_revenge.py.

*note - to see output, uncomment the lines calling 
functions between lines 41 and 65. They are split up 
by questions, and when uncommented will output the data
used to answer the corresponding questions. 
'''
import os
from generate_yearly_stats import generate_yearly_stats
from avg_up_and_down import avgUpAndDowns
from generate_all_stats import generate_all_stats
from oracle import oracle, buy_and_hold
from oracle_revenge import wrong_best_ten, wrong_worst_ten, wrong_best_and_worst_five

ticker1 = 'COST'
ticker2 = 'SPY'
input_dir = r'/Users/ryan/Desktop/school/cs677/assignments/week_1_homework/stock_data'
ticker_file1 = os.path.join(input_dir, ticker1 + '.csv')
ticker_file2 = os.path.join(input_dir, ticker2 + '.csv')


try:   
    with open(ticker_file1) as f:
        cost = f.read().splitlines()
    print('opened file for ticker: ', ticker1)

    with open(ticker_file2) as f:
        spy = f.read().splitlines()
    print('opened file for ticker: ', ticker2)

    # ===== Question 1 and 2 =====
    #generate_yearly_stats(cost)
    #avgUpAndDowns(cost)

    # ===== Question 3 =====
    #generate_all_stats(cost, spy)

    # ===== Question 4 =====
    #oracle(cost)
    #oracle(spy)

    # ===== Question 5 =====
    #buy_and_hold(cost)
    #buy_and_hold(spy)

    # ===== Question 6 =====
    #print("wrong best ten:")
    #wrong_best_ten(cost)
    #wrong_best_ten(spy)
    #print("wrong worst 10:")
    #wrong_worst_ten(cost)
    #wrong_worst_ten(spy)
    #print("wrong best and worst 5:")
    #wrong_best_and_worst_five(cost)
    #wrong_best_and_worst_five(spy)

    
except Exception as e:
    print(e)
    print('failed to read stock data')