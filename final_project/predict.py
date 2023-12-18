import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#TO DO: 
# first goal is to create  a 2d arrray of chords at each soprano point in time
# create 4 dictionaries separated by voice
# get list of Soprano values from start step from OUTPUT SEQUENCE
# go through each of the other 3 voices and gather corresponding note values at each S point in time
# store as 2d array

data = pd.read_json(path_or_buf='final_project/data-test-1.jsonl', lines=True)
#data = pd.read_json(path_or_buf='final_project/bach-doodle-1k.jsonl', lines=True)
data = data.drop(['backend','composition_time', 'country', 'loops_listened', 'request_id', 'session_id'], axis = 1)

#print(data)

noteinput = data['input_sequence']
notevals = {}
inputsequence = []

bassdf = pd.DataFrame(columns = ["Soprano", "Prev", "Class"])
tenordf = pd.DataFrame(columns = ["Soprano", "Bass", "Prev", "Class"])
altodf = pd.DataFrame(columns = ["Soprano", "Bass", "Tenor", "Prev", "Class"])

def format_output(df):

    global bassdf
    global tenordf
    global altodf

    soprano, alto, tenor, bass = [], [], [], []

    for note in data['output_sequence'][0][0]['notes']:
        if 'startTime' not in note.keys():
            note['startTime'] = 0.0
        if 'instrument' not in note.keys():
            soprano.append([note['startTime'], note['pitch']])
        elif note['instrument'] == 1:
            alto.append([note['startTime'], note['pitch']])
        elif note['instrument'] == 2:
            tenor.append([note['startTime'], note['pitch']])
        else:
            bass.append([note['startTime'], note['pitch']])

    x = 0
    while x < len(soprano):
        if x < len(alto):
            if alto[x][0] > soprano[x][0]:
                alto.insert(x, [soprano[x][0], alto[x-1][1]])
                x -= 1
        else: 
            alto.append(soprano[x])
        x += 1
    x = 0
    while x < len(soprano):
        if x < len(tenor):
            if tenor[x][0] > soprano[x][0]:
                tenor.insert(x, [soprano[x][0], tenor[x-1][1]])
                x -= 1
        else: 
            tenor.append(soprano[x])
        x += 1
    x = 0
    while x < len(soprano):
        if x < len(bass):
            if bass[x][0] > soprano[x][0]:
                bass.insert(x, [soprano[x][0], bass[x-1][1]])
                x -= 1
        else: 
            bass.append(soprano[x])
        x += 1

    for x in range(len(soprano)):
        soprano[x] = soprano[x][1]
        alto[x] = alto[x][1]
        tenor[x] = tenor[x][1]
        bass[x] = bass[x][1]

    for x in range(len(soprano)-1, 0, -1):
        bassdf = pd.concat([pd.DataFrame([[soprano[x], bass[x-1], bass[x]]], columns = bassdf.columns), bassdf])
        bassdf.index += 1
        tenordf = pd.concat([pd.DataFrame([[soprano[x], bass[x], tenor[x-1], tenor[x]]], columns = tenordf.columns), tenordf])
        tenordf.index += 1
        altodf = pd.concat([pd.DataFrame([[soprano[x], bass[x], tenor[x], alto[x-1], alto[x]]], columns = altodf.columns), altodf])
        altodf.index += 1
        
    return df

data = data.apply(format_output, axis = 1)



# print(bassdf)
# print(tenordf)
# print(altodf)
    
#print(bassdf)

bass_train, bass_test = train_test_split(bassdf, test_size = 0.25, train_size = 0.75, random_state = 13)

# gather train/test x and y values from split data sets
x_train = bass_train.iloc[:, 0:2]
#print(bass_train.iloc[:, 2])
y_train = bass_train["Class"].astype(int)
x_test = bass_test.iloc[:, 0:2]
y_test = bass_test["Class"].astype(int)

# initialize logisticregression method
bass_log_reg = LogisticRegression(multi_class='ovr', solver='liblinear')
# fit to training data
bass_log_reg.fit(x_train,y_train)
# predict using test data
y_predict = bass_log_reg.predict(x_test)
#print(y_train)
print(y_test)
print(y_predict)
# display accuracy
print(accuracy_score(y_test, y_predict))


