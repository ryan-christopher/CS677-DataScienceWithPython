'''
Ryan Christopher
Class: CS 677
Date: 11/12/2023
Assignment 5 Question 1

=======Description of Problem=======
Load the "raw data" worksheet from the excel file into a Pandas dataframe,
then combine the NSP labels into two groups: N for normal and A for 
abnormal. 
'''
import pandas as pd

# assignClass reads the excel file, assigns the NSP class,
# and returns a dataframe containing the raw data
def assignClass():
    # create ctg dataframe from excel worksheet
    ctg = pd.read_excel('assignment5/data/CTG.xls', sheet_name="Raw Data")

    # remove extra columns
    ctg = ctg.drop(['FileName', 'Date', 'SegFile', 'b', 'e', 'LBE', 'AC', 'FM', 'UC',
                    'DL', 'DS', 'DP', 'DR', 'Nmax', 'Nzeros', 'Tendency', 'A', 'B', 
                    'C', 'D', 'E', 'AD', 'DE', 'LD', 'FS', 'SUSP', 'CLASS'], 
                    axis = 1)
    
    # separate normal and abnormal entries
    normal = ctg.where(ctg['NSP'] == 1).dropna().drop('NSP', axis = 1)
    abnormal = ctg.where(ctg['NSP'] != 1).dropna().drop('NSP', axis = 1)

    # update NSP label to be 0 for normal and 1 for abnormal
    normal['NSP'], abnormal['NSP'] = '1', '0'

    # join the two dataframes together once class names updated
    ctg = pd.concat([normal, abnormal]).sort_index()

    # return dataframe
    return ctg

assignClass()