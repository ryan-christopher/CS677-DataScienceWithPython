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
    if data['feedback'][0][0] == "2" or data['feedback'][0][0] == "1":

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
                if x < (len(alto)-1):
                    if (alto[x][0] < soprano[x][0]) and alto[x+1][0] < soprano[x][0]:
                        alto.pop(x+1)
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
                if x < (len(tenor)-1):
                    if (tenor[x][0] < soprano[x][0]) and tenor[x+1][0] < soprano[x][0]:
                        tenor.pop(x+1)
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
                if x < (len(bass)-1):
                    if (bass[x][0] < soprano[x][0]) and bass[x+1][0] < soprano[x][0]:
                        bass.pop(x+1)
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
            bassdf = pd.concat([pd.DataFrame([[soprano[x], bass[x-1], bass[x]]], 
                                             columns = bassdf.columns), bassdf])
            bassdf.index += 1
            tenordf = pd.concat([pd.DataFrame([[soprano[x], bass[x], tenor[x-1], tenor[x]]], 
                                              columns = tenordf.columns), tenordf])
            tenordf.index += 1
            altodf = pd.concat([pd.DataFrame([[soprano[x], bass[x], tenor[x], alto[x-1], alto[x]]], 
                                             columns = altodf.columns), altodf])
            altodf.index += 1
      
    return df


data = data.apply(format_output, axis = 1)

bass_train, bass_test = train_test_split(bassdf, test_size = 0.3, train_size = 0.7)
bass_x_train = bass_train.iloc[:, 0:2]
bass_y_train = bass_train["Class"].astype(int)
bass_x_test = bass_test.iloc[:, 0:2]
bass_y_test = bass_test["Class"].astype(int)
bass_log_reg = LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=200)
bass_log_reg.fit(bass_x_train,bass_y_train)
bass_y_predict = bass_log_reg.predict(bass_x_test)
#print("Bass")
#print(accuracy_score(bass_y_test, bass_y_predict))

tenor_train, tenor_test = train_test_split(tenordf, test_size = 0.3, train_size = 0.7)
tenor_x_train = tenor_train.iloc[:, 0:3]
tenor_y_train = tenor_train["Class"].astype(int)
tenor_x_test = tenor_test.iloc[:, 0:3]
tenor_y_test = tenor_test["Class"].astype(int)
tenor_log_reg = LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=200)
tenor_log_reg.fit(tenor_x_train,tenor_y_train)
tenor_y_predict = tenor_log_reg.predict(tenor_x_test)
#print("Tenor")
#print(accuracy_score(tenor_y_test, tenor_y_predict))

first_alto_train, first_alto_test = train_test_split(altodf, test_size = 0.3, train_size = 0.7)
first_alto_x_train = first_alto_train.iloc[:, 0:3]
first_alto_y_train = first_alto_train["Class"].astype(int)
first_alto_x_test = first_alto_test.iloc[:, 0:3]
first_alto_y_test = first_alto_test["Class"].astype(int)
first_alto_log_reg = LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=200)
first_alto_log_reg.fit(first_alto_x_train,first_alto_y_train)
first_alto_y_predict = first_alto_log_reg.predict(first_alto_x_test)
#print("First alto")
#print(accuracy_score(first_alto_y_test, first_alto_y_predict))

alto_train, alto_test = train_test_split(altodf, test_size = 0.3, train_size = 0.7)
alto_x_train = alto_train.iloc[:, 0:4]
alto_y_train = alto_train["Class"].astype(int)
alto_x_test = alto_test.iloc[:, 0:4]
alto_y_test = alto_test["Class"].astype(int)
alto_log_reg = LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=200)
alto_log_reg.fit(alto_x_train,alto_y_train)
alto_y_predict = alto_log_reg.predict(alto_x_test)
#print("Alto")
#print(accuracy_score(alto_y_test, alto_y_predict))


def generate(sequence):
    soprano = sequence
    alto, tenor, bass = [], [], []

    bass.append(bass_log_reg.predict(pd.DataFrame([[soprano[0], soprano[0]]], 
                                                  columns = ["Soprano", "Prev"]))[0] - 12)
    tenor.append(tenor_log_reg.predict(pd.DataFrame([[soprano[0], bass[0], soprano[0]]], 
                                                    columns = ["Soprano", "Bass", "Prev"]))[0] - 12)
    alto.append(first_alto_log_reg.predict(pd.DataFrame([[soprano[0], bass[0], tenor[0]]], 
                                                        columns = ["Soprano", "Bass", "Tenor"]))[0] - 12)

    for x in range(1, len(soprano)):
        print("Soprano", soprano[x-1])
        print("Alto", alto[x-1])
        print("Tenor", tenor[x-1])
        print("Bass", bass[x-1])
        bass.append(bass_log_reg.predict(pd.DataFrame([[soprano[x], bass[x-1]]], 
                                                      columns = ["Soprano", "Prev"]))[0] - 12)
        tenor.append(tenor_log_reg.predict(pd.DataFrame([[soprano[x], bass[x], tenor[x-1]]], 
                                                        columns = ["Soprano", "Bass", "Prev"]))[0] - 12)
        alto.append(alto_log_reg.predict(pd.DataFrame([[soprano[x], bass[x], tenor[x], alto[x-1]]], 
                                                      columns = ["Soprano", "Bass", "Tenor", "Prev"]))[0] - 12)

    print(soprano)
    print(alto)
    print(tenor)
    print(bass)
    return alto, tenor, bass
