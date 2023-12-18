import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_json(path_or_buf='final_project/data-test-100.jsonl', lines=True)
data = data.drop(['backend','composition_time', 'country', 'loops_listened', 'request_id', 'session_id'], axis = 1)


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

bass_train, bass_test = train_test_split(bassdf, test_size = 0.2, train_size = 0.8, random_state = 13)
bass_x_train = bass_train.iloc[:, 0:2]
bass_y_train = bass_train["Class"].astype(int)
bass_x_test = bass_test.iloc[:, 0:2]
bass_y_test = bass_test["Class"].astype(int)
bass_log_reg = LogisticRegression(multi_class='ovr', solver='liblinear')
bass_log_reg.fit(bass_x_train,bass_y_train)
bass_y_predict = bass_log_reg.predict(bass_x_test)
print(accuracy_score(bass_y_test, bass_y_predict))

tenor_train, tenor_test = train_test_split(tenordf, test_size = 0.2, train_size = 0.8, random_state = 13)
tenor_x_train = tenor_train.iloc[:, 0:3]
tenor_y_train = tenor_train["Class"].astype(int)
tenor_x_test = tenor_test.iloc[:, 0:3]
tenor_y_test = tenor_test["Class"].astype(int)
tenor_log_reg = LogisticRegression(multi_class='ovr', solver='liblinear')
tenor_log_reg.fit(tenor_x_train,tenor_y_train)
tenor_y_predict = tenor_log_reg.predict(tenor_x_test)
print(accuracy_score(tenor_y_test, tenor_y_predict))

alto_train, alto_test = train_test_split(altodf, test_size = 0.2, train_size = 0.8, random_state = 13)
alto_x_train = alto_train.iloc[:, 0:4]
alto_y_train = alto_train["Class"].astype(int)
alto_x_test = alto_test.iloc[:, 0:4]
alto_y_test = alto_test["Class"].astype(int)
alto_log_reg = LogisticRegression(multi_class='ovr', solver='liblinear')
alto_log_reg.fit(alto_x_train,alto_y_train)
alto_y_predict = alto_log_reg.predict(alto_x_test)
print(accuracy_score(alto_y_test, alto_y_predict))

testinput = [67, 62, 60, 62, 67, 69, 66, 67]