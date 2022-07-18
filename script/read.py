import os
import csv
import numpy as np

data_final = []
with open('/home/glen/Documents/python_OOP/Arte_proj/data/data.csv', 'r') as f:
    doc_audio_visuel = csv.reader(f)
    for row in doc_audio_visuel:
        data_final.append(row)

lst = []
for i in range(5):
    lst.append(data_final[i+1])

transposed_doc = np.array(lst).T
print(transposed_doc)
print ("______________")
print(lst)

