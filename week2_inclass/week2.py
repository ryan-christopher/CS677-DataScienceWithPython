import pandas as pd

# 1. Write a function that creates a Pandas DataFrame from a two-dimensional list. The function should
# take the list as input and return the dataframe. E.g. if the input list is lst = [['a',1],['b',2],['c',3]],
# your function should create a dataframe with a column 'str' containing 'a', 'b', and 'c' and a second
# column 'num' containing 1, 2, and 3.

def createFrameFrom2d(inputList):
    strs, nums = [], []
    for val in inputList:
        strs.append(val[0])
        nums.append(val[1:])
    return pd.DataFrame({"str" : strs, "num" : nums})

lst = [['a',1],['b',2],['c',3]]
print('----- 1 -----')
print(createFrameFrom2d(lst), '\n')

# 2. Write a function that discounts 10% off of the price given in the 'Cost' column of a DataFrame. Your
# function should take as input a Pandas DataFrame (with a column called 'Cost' of type float), and
# return the original DataFrame with the column 'Discounted Price' added. E.g. consider prices = pd.
# DataFrame([['Apple',2],['Banana',3],['Orange',4]],columns=['Fruit','Cost']).

def takeTen(frame): 
    frame.Cost *= 0.9
    return frame

prices = pd.DataFrame([['Apple',2],['Banana',3],['Orange',4]],columns=['Fruit','Cost'])
print('----- 2 -----')
print(takeTen(prices))

# 3. With a given DataFrame containing US city and region information (city in a column called 'City' and
# Region in a column called 'Region'), write a function to create a new DataFrame with cities only in the
# Northeast. E.g. consider cities = pd.DataFrame({'City':['Boston','Atlanta','LA','San Diego','New York
# City'], 'Region':['Northeast','Southeast','West Coast','West Coast','Northeast']},columns=['City','Region
# ']).

def northeastOnly(frame):
    return frame[frame.Region == "Northeast"]

cities = pd.DataFrame({'City':['Boston','Atlanta','LA','San Diego','New York City'], 
                       'Region':['Northeast','Southeast','West Coast','West Coast','Northeast']},
                       columns=['City','Region'])

print(northeastOnly(cities))

# 4. Using the where function, write a function to take as input a dataframe of stock prices (cols 'Ticker','Year',
# 'Month','Day','Price') and output records with price greater than $10 and month either January or
# June. E.g. stocks = pd.DataFrame({'Ticker':['MSFT','SPY','VOO','GME','VHG'], 'Year': [2022,2022,2022,2022,2022],
# 'Month': [1,3,5,6,8], 'Day': [2,4,6,12,18], 'Price': [100.,200.,300.,5.,500.]},columns=['Ticker','Year',
# 'Month','Day','Price']).

def returnInJanOrJune(frame):
    return frame.where((frame.Price > 10) & (frame.Month.isin([1,6]))).dropna()

stocks = pd.DataFrame({'Ticker':['MSFT','SPY','VOO','GME','VHG'], 
                       'Year': [2022,2022,2022,2022,2022],
                       'Month': [1,3,5,6,8], 'Day': [2,4,6,12,18], 
                       'Price': [100.,200.,300.,5.,500.]},
                       columns=['Ticker','Year','Month','Day','Price'])

print(returnInJanOrJune(stocks))
