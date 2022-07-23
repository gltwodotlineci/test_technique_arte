import read
from read import data_final
import numpy as np


class Chaine:
    def __init__(self,tf1,france_2,france_3,canal_plus,arte):
        self.tf1 = tf1
        self.france_2 = france_2
        self.france_3 = france_3
        self.canal_plus = canal_plus
        self.arte = arte


print("________________")

x = np.array(data_final)
length_list = len(x)

transposed_dt = []
for i in range(1,length_list,14):
    down_part_block = i
    up_part_block = i + 14
    transposed_dt.append(x[down_part_block:up_part_block, 2:].T)

