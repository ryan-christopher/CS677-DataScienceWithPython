'''
Ryan Christopher
Class: CS 677
Date: 10/6/2023
Assignment 3 Question 1

=======Description of Problem=======
Taking the data of real and forged bank notes, load the data into a dataframe 
and create a column 'color'. Then, assign each data entry either green or red 
depending on it's class and for each feature and class determine the mean and 
standard deviation (rounded to 2 decimal places)
'''
import pandas as pd
import numpy as np


# createFrame takes the notedata txt file and returns a dataframe
# with the appropriate columns as well as the correctly assigned 
# color for each entry
def createFrame():
    # read CSV data and store into dataframe called notes_data
    colNames = ['Variance', 'Skewness', 'Curtosis', 'Entropy', 'Class']
    notes_data = pd.read_csv('assignment3/banknote_data/notedata.txt', 
                             names = colNames, sep = ',')
    
    # call setColor on dataframe to assign color depending on class
    notes_data = notes_data.apply(setColor, axis = 1)

    # return a dataframe with the banknote data
    return notes_data


# setColor takes each row of data from notes_data, and assigns the
# Color column depending on the entry's Class
def setColor(df):
    if df['Class'] == 0:
        df['Color'] = 'green'
    else:
        df['Color'] = 'red'

    return df


# analyzeFrame takes the dataframe of banknotes as input, and calculates
# the mean and standard deviation for each class and each feature
def analyzeFrame(df):
    # create dictionaries for all banknotes, class 0 banknotes, 
    # and class 1 banknotes
    all_entries, green_entries, red_entries = {}, {}, {}

    # iterate through features
    for term in ['Variance', 'Skewness', 'Curtosis', 'Entropy']:

        # regardless of class add full column to all_entries dict
        all_entries[term] = df[term].to_numpy()
        # create lists for green_entries and red_entries feature
        green_entries[term], red_entries[term] = [], []

        # iterate through all_entries
        for entry in range(len(all_entries[term])):    
            # add current entry to green_entries dict if class 0
            if df.loc[entry]['Color'] == 'green':
                green_entries[term].append(all_entries[term][entry])
            # add current entry to red_entries dict if class 1
            else:
                red_entries[term].append(all_entries[term][entry])
        
        # convert both arrays to nparrays to efficiently calculate mean and sd
        green_entries[term] = np.array(green_entries[term])
        red_entries[term] = np.array(red_entries[term])

        # calculate mean and sd of all three groups (all, green, and red)
        all_entries[term + ' - mean'] = np.mean(all_entries[term])
        all_entries[term + ' - sd'] = np.std(all_entries[term])
        green_entries[term + ' - mean'] = np.mean(green_entries[term])
        green_entries[term + ' - sd'] = np.std(green_entries[term])
        red_entries[term + ' - mean'] = np.mean(red_entries[term])
        red_entries[term + ' - sd'] = np.std(red_entries[term])

        # remove lists to make print statements more readable 
        del all_entries[term], green_entries[term], red_entries[term]

    # print("===== All Entries =====")
    # for key, value in all_entries.items():
    #     print(key)
    #     print(value)
    # print("===== Green Entries =====") 
    # for key, value in green_entries.items():
    #     print(key)
    #     print(value)
    # print("===== Red Entries =====")
    # for key, value in red_entries.items():
    #     print(key)
    #     print(value)


bank_note_data = createFrame()
#analyzeFrame(bank_note_data)