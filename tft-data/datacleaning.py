import numpy as np
import pandas as pd

with open('tftdata.txt', 'r') as file:
    data = file.read()
    
data = eval(data)
desc_data = list(map(lambda x: x['description'], data))

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

def removeSubstring(data):
    occurence_of_a = find_indices(list(data), '@')
    occurence_of_a = np.array(occurence_of_a).reshape(-1,2)
    arr_of_substr = []
    for item in occurence_of_a:
        substring = data[item[0]-1:item[1]+1]
        arr_of_substr.append(substring)
    for item in arr_of_substr:
        data = data.replace(item, '')
    return data

arr_of_desc = []
for i in desc_data:
    i = removeSubstring(i)
    arr_of_desc.append(i)

arr_of_desc = eval(str(arr_of_desc).replace("\\n", " "))

for i in range(len(data)):
    data[i]['description'] = arr_of_desc[i]
 
df = pd.DataFrame(data)
df = df.set_index('name')

# df.to_csv('tftdata.csv', sep='\t', encoding='utf-8')