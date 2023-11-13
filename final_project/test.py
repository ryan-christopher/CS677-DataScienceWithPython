import pandas as pd
import numpy as np

data = pd.read_json(path_or_buf='final_project/bach-doodle-1k.jsonl', lines=True)
print(data.columns)
data = data.drop(['backend','composition_time', 'country', 'loops_listened', 'request_id', 'session_id'], axis = 1)
print(data)