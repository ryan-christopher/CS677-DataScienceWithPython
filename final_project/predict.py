import pandas as pd
import numpy as np

data = pd.read_json(path_or_buf='final_project/data-test-1.jsonl', lines=True)
data = data.drop(['backend','composition_time', 'country', 'loops_listened', 'request_id', 'session_id'], axis = 1)
#print("Full entry")
#print(data)
#print("input sequence")
noteinput = data['input_sequence']
notevals = {}
inputsequence = []
for note in noteinput[0][0]['notes']:
    notevals[str(note['pitch'])] = []
    inputsequence.append(note['pitch'])
print(notevals)
print(inputsequence)
#for note in data['output_sequence'][0][0]['notes']:
#    print(note['pitch'])  