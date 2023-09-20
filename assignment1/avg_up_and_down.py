'''
Ryan Christopher
Class: CS 677
Date: 9/16/2023
Assignment 1 Question 1 Part 4

=======Description of Problem=======
Determine if a stock loses more on a down day than it
gains on an up day.
'''

# avgUpAndDowns finds the average amount that is lost on a down 
# day and gained on an up day 
def avgUpAndDowns(lines):
    positives = []
    pos_sum = 0
    negatives = []
    neg_sum = 0
    # iterate through lines of daily stock info
    for line in lines[1:]:
        line = line.split(',')    
        
        # store values for day of the week, year, and the return for the day
        daily_return = float(line[13])

        # store positive returns
        if daily_return > 0:
            positives.append(daily_return)
            pos_sum += daily_return

        # store negative returns
        elif daily_return < 0:
            negatives.append(daily_return)
            neg_sum += daily_return

    # find average of positive and negative days
    print("Positive Days:", len(positives), "Avg:", pos_sum / len(positives))
    print("Negative Days:", len(negatives), "Avg:", neg_sum / len(negatives))
