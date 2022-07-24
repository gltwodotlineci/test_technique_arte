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

class Test_cls:
    def __init__(self,step,data):
        self.step = step
        self.data = data
        self.transposed_dt = []
        self.fix_list = []
        self.final_list = []

    def transpos_fc(self):
        length_list = len(self.data) - self.step
        for i in range(1,length_list,self.step):
            down_part_block = i
            up_part_block = i + 14
            self.transposed_dt.append(self.data[down_part_block:up_part_block, 2:].T)
        return np.array(self.transposed_dt)

    def fixing_dt(self):
        for i in self.transpos_fc():
            for j in range(len(i)):
                self.fix_list.append(i[j])
        return np.array(self.fix_list)

print(Test_cls(14,np.array(data_final)).fixing_dt())

