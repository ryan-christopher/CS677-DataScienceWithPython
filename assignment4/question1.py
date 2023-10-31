'''
Ryan Christopher
Class: CS 677
Date: 10/31/2023 👻
Assignment 4 Question 1

=======Description of Problem=======
Load the heart failure data into a Pandas dataframe, and extract two dataframes with
the features creatinine phosphokinase, serum creatinine, serum sodium, and platelets. 
Then for each dataset, construct the visual representations of correponding 
correlation matrices M0 and M1, and examine the correlation matrix plots.
'''
import pandas as pd

# getHeartData reads the csv of heat failure data, extracts two dataframes 
# with the 4 features mentioned above, and generates plots for both
# classes of death_event
def getHeartData():

    # read CSV data and store into dataframe
    heart_data = pd.read_csv('assignment4/heart_data/heart_failure_data.csv')

    # remove extra columns
    heart_data = heart_data.drop(['anaemia', 'diabetes', 'ejection_fraction', 'age',
                                  'high_blood_pressure', 'sex', 'smoking', 'time'], axis = 1)
    
    # reorder columns 
    heart_data = heart_data[['creatinine_phosphokinase', 'serum_creatinine', 
                             'serum_sodium', 'platelets', 'DEATH_EVENT']]

    # separate into 2 classes based on DEATH_EVENT
    class_0 = heart_data.where(heart_data['DEATH_EVENT'] == 0).dropna()
    class_1 = heart_data.where(heart_data['DEATH_EVENT'] == 1).dropna()

    print(class_1)

    #print(heart_data)


getHeartData()