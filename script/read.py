import os
import csv

data_final = []
with open('/home/glen/Documents/python_OOP/Arte_proj/data/data.csv', 'r') as f:
    doc_audio_visuel = csv.reader(f)
    for row in doc_audio_visuel:
        data_final.append(row)
